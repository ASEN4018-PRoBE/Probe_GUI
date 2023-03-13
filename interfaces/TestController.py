import time
from PyQt6 import QtGui
from PyQt6.QtCore import QThread, pyqtSignal

import global_vars
from interfaces import DMMInterface, ISOInterface, MCUInterface, TestStorage

index_test_function = 0
index_pins = 0

# class for multi-threading digital multi-meter tests
class DMMTestRunnerThread(QThread):
    result = pyqtSignal(dict)

    def __init__(self, test_config):
        super(QThread, self).__init__()
        self.test_config = test_config
        self.mcu = MCUInterface.MCUInterface()
        self.dmm = DMMInterface.DMMInterface()

    def run(self):
        global index_test_function, index_pins
        while True:
            test_function = global_vars.test_functions[index_test_function]
            pass_criteria = self.test_config[test_function]["Pass Criteria"]
            duration = float(self.test_config[test_function]["Duration"])
            pins = self.test_config[test_function]["Pins"][index_pins]
            pin1 = pins["Pin 1"]
            pin2 = pins["Pin 2"]

            reading = []
            t = []
            
            # switch on pins
            if test_function in global_vars.voltage_tests:
                units = global_vars.units_voltage_dmm
                self.mcu.switch(pin1, pin2, None, None)
            elif test_function in global_vars.resistance_tests:
                units = global_vars.units_resistance_dmm
                self.mcu.switch(pin1, pin2, pin1, pin2)
            
            # take DMM measurement
            time_start = time.time()
            while (time.time()-time_start)<=duration:
                if test_function in global_vars.voltage_tests:
                    reading.append(self.dmm.voltage())
                elif test_function in global_vars.resistance_tests: # four wire measurement
                    reading.append(self.dmm.resistance())
                t.append(time.time()-time_start)

            result_dict = {
                "test_function":test_function,
                "pin1":pin1, "pin2":pin2,
                "units":units,
                "t":t, "reading":reading,
                "pass_criteria":pass_criteria
            }
            self.result.emit(result_dict)

            index_pins += 1 # while loop control
            if index_pins==len(self.test_config[test_function]["Pins"]):
                index_test_function += 1
                index_pins = 0
                if index_test_function==len(global_vars.test_functions):
                    self.mcu.disconnect()
                    index_test_function = 0
                    break # break and do isolation tests

# class for multi-threading isolation test
class ISOTestRunnerThread(QThread):
    result = pyqtSignal(dict)

    def __init__(self, test_config):
        super(QThread, self).__init__()
        self.test_config = test_config
        self.mcu = MCUInterface.MCUInterface()
        self.iso = ISOInterface.ISOInterface()
    
    def run(self):
        global index_test_function, index_pins
        while True:
            test_function = global_vars.isolation_tests[index_test_function]
            pass_criteria = self.test_config[test_function]["Pass Criteria"]
            duration = float(self.test_config[test_function]["Duration"])
            pins = self.test_config[test_function]["Pins"][index_pins]
            pin1 = pins["Pin 1"]
            pin2 = pins["Pin 2"]

            units = global_vars.units_resistance_iso
            self.mcu.switch(pin1, pin2, None, None)

            # take ISO measurement
            time_start = time.time()
            time.sleep(duration)
            reading = self.iso.resistance() # take reading only once, different from DMM read

            result_dict = {
                "test_function":test_function,
                "pin1":pin1, "pin2":pin2,
                "units":units,
                "reading":reading,
                "pass_criteria":pass_criteria
            }
            self.result.emit(result_dict)

            index_pins += 1 # while loop control
            if index_pins==len(self.test_config[test_function]["Pins"]):
                index_test_function += 1
                index_pins = 0
                if index_test_function==len(global_vars.isolation_tests):
                    self.mcu.disconnect()
                    index_test_function = 0
                    break # done with iso test quit runner thread

class TestController:
    def __init__(self, test_config, main_window):
        self.test_config = test_config
        self.main_window = main_window
        self.test_storage = TestStorage.TestStorage(test_config)
        self.test_runner = DMMTestRunnerThread(test_config)
        self.test_runner.result.connect(self.process_dmm_test_runner_result)
        self.test_runner.finished.connect(self.start_iso)

    def start(self):
        self.test_runner.start()
        
        self.update_status_bar()
        self.main_window.navigation_pane.btn_start.setIcon(QtGui.QIcon("images/pause.svg"))
        self.main_window.navigation_pane.btn_start.clicked.connect(self.pause)

    def start_iso(self):
        self.test_runner = ISOTestRunnerThread(self.test_config)
        self.test_runner.result.connect(self.process_iso_test_runner_result)
    
    def pause(self):
        self.test_runner.terminate()
        self.main_window.status_bar.set_message(False,"n/a","n/a","n/a")
        self.main_window.navigation_pane.btn_start.setIcon(QtGui.QIcon("images/play.svg"))
        self.main_window.navigation_pane.btn_start.clicked.connect(self.start)

    def stop(self):
        self.test_runner.terminate()
        global index_test_function, index_pins
        index_test_function = 0
        index_pins = 0
    
    def process_dmm_test_runner_result(self, result:dict):
        test_function = result["test_function"]
        pin1 = result["pin1"]
        pin2 = result["pin2"]
        units = result["units"]
        t = result["t"]
        reading = result["reading"]
        pass_criteria = result["pass_criteria"]
        pin_reading = TestStorage.PinReading(pin1,pin2,units)
        pin_reading.time = t
        pin_reading.reading = reading
        pin_reading.pass_fail = self.get_pass_fail(reading,units,pass_criteria)
        self.test_storage.storage[test_function].pin_readings.append(pin_reading)
        self.main_window.test_results_page.element_dict[test_function].append_test_result(
            pin1, pin2, "{0:.3f}".format(reading[-1])+" "+units, pin_reading.pass_fail
        )
        self.update_status_bar()

    def process_iso_test_runner_result(self, result:dict):
        test_function = result["test_function"]
        pin1 = result["pin1"]
        pin2 = result["pin2"]
        units = result["units"]
        reading = result["reading"]
        pass_criteria = result["pass_criteria"]
        pass_fail = self.get_pass_fail(reading,units,pass_criteria)
        pin_reading = self.test_storage.get_reading(test_function,pin1,pin2)
        if pin_reading is None:
            pin_reading = TestStorage.PinReading(pin1,pin2,units)
            self.test_storage.storage[test_function].pin_readings.append(pin_reading)
        pin_reading.iso_reading = reading
        pin_reading.pass_fail = pin_reading.pass_fail and pass_fail
        test_result_row = self.main_window.test_results_page.element_dict[test_function].get_test_result_row(pin1,pin2)
        iso_result = "{0:.3f}".format(reading[-1])+" "+units
        if test_result_row is None:
            self.main_window.test_results_page.element_dict[test_function].append_test_result(
                pin1, pin2, "n/a", pass_fail
            )
        else:
            self.main_window.test_results_page.element_dict[test_function].set_test_result_row_iso(
                pin1, pin2, reading, pass_fail
            )
        self.update_status_bar()

    def get_pass_fail(self, reading, reading_units, pass_criteria:str) -> bool:
        low,high,units = pass_criteria.replace("[","").replace("]","").split(" ")
        low,high = float(low),float(high)
        value = reading[-1]
        if reading_units!=units:
            value *= global_vars.unit_conversion[units[0]]
        return low<=value and value<=high
    
    def update_status_bar(self):
        global index_test_function, index_pins
        test_function = global_vars.test_functions[index_test_function]
        if isinstance(self.test_runner,ISOTestRunnerThread):
            test_function = global_vars.isolation_tests[index_test_function]
        pins = self.test_config[test_function]["Pins"][index_pins]
        pin1 = pins["Pin 1"]
        pin2 = pins["Pin 2"]
        self.main_window.status_bar.set_message(True,test_function,pin1,pin2)