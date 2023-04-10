import time
from PyQt6 import QtGui, QtWidgets
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
        self.is_running = True

    def run(self):
        global index_test_function, index_pins
        while self.is_running:
            test_function = global_vars.test_functions[index_test_function]
            pass_criteria = self.test_config[test_function]["Pass Criteria"]
            duration = float(self.test_config[test_function]["Duration"])
            if index_pins>=len(self.test_config[test_function]["Pins"]): break
            pins = self.test_config[test_function]["Pins"][index_pins]
            pin1 = pins["Pin 1"]
            pin2 = pins["Pin 2"]

            readings = []
            t = []
            
            # switch on pins
            if test_function in global_vars.voltage_tests:
                units = global_vars.units_voltage_dmm
                self.mcu.switch(pin1, pin2, wire_type=2)
            elif test_function in global_vars.resistance_tests:
                if index_pins==0 and index_test_function!=0:
                    time_start = time.time() # delay when switching to a new test type
                    while (time.time()-time_start)<=2:
                        if not self.is_running: return
                        time.sleep(0.5)
                units = global_vars.units_resistance_dmm
                self.mcu.switch(pin1, pin2, wire_type=4)

            # take DMM measurement
            time_start = time.time()
            while (time.time()-time_start)<=duration:
                if not self.is_running:
                    print("stop clicked, returning")
                    return
                if test_function in global_vars.voltage_tests:
                    readings.append(self.dmm.voltage())
                elif test_function in global_vars.resistance_tests: # four wire measurement
                    if test_function in global_vars.continuity_tests:
                        readings.append(self.dmm.resistance(True))
                    else:
                        readings.append(self.dmm.resistance())
                t.append(time.time()-time_start)

            result_dict = {
                "test_function": test_function,
                "pin1": pin1, "pin2": pin2,
                "units": units,
                "t": t, "readings": readings,
                "pass_criteria": pass_criteria
            }
            self.result.emit(result_dict)

            index_pins += 1 # while loop control
            if index_pins==len(self.test_config[test_function]["Pins"]):
                index_test_function += 1
                index_pins = 0
                if index_test_function==len(global_vars.test_functions):
                    self.mcu.disconnect()
                    # set index_test_function to first occuring index of isolation_tests
                    index_test_function = global_vars.test_functions.index(global_vars.isolation_tests[0])
                    return
    
    def stop(self):
        self.is_running = False

# class for multi-threading isolation test
class ISOTestRunnerThread(QThread):
    result = pyqtSignal(dict)

    def __init__(self, test_config):
        super(QThread, self).__init__()
        self.test_config = test_config
        self.mcu = MCUInterface.MCUInterface()
        self.iso = ISOInterface.ISOInterface()
        self.is_running = True
    
    def run(self):
        global index_test_function, index_pins
        while self.is_running:
            while global_vars.test_functions[index_test_function] not in global_vars.isolation_tests:
                index_test_function += 1
            test_function = global_vars.test_functions[index_test_function]
            pass_criteria = self.test_config[test_function]["Pass Criteria"]
            duration = float(self.test_config[test_function]["Duration"])
            if index_pins>=len(self.test_config[test_function]["Pins"]): break
            pins = self.test_config[test_function]["Pins"][index_pins]
            pin1 = pins["Pin 1"]
            pin2 = pins["Pin 2"]

            units = global_vars.units_resistance_iso
            self.mcu.switch(pin1, pin2, wire_type=2)

            # take ISO measurement
            time_start = time.time()
            while (time.time()-time_start)<=duration:
                if not self.is_running: return
                time.sleep(0.5)
            reading = self.iso.resistance(duration) # take reading only once, different from DMM

            result_dict = {
                "test_function": test_function,
                "pin1": pin1, "pin2": pin2,
                "units": units,
                "reading": reading,
                "pass_criteria": pass_criteria
            }
            self.result.emit(result_dict)

            index_pins += 1 # while loop control
            if index_pins==len(self.test_config[test_function]["Pins"]):
                index_test_function += 1
                index_pins = 0
                if index_test_function==len(global_vars.test_functions):
                    self.mcu.disconnect()
                    index_test_function = 0
                    break # done with iso test quit runner thread
        
    def stop(self):
        self.is_running = False

class TestController:
    def __init__(self, test_config, main_window):
        self.test_config = test_config
        self.main_window = main_window
        self.test_storage = TestStorage.TestStorage(test_config)
        self.is_iso_running = False

        self.reset_progress_tracker()

    def start(self) -> bool:
        if not self.is_iso_running:
            print("start dmm runner thread")
            self.test_runner = DMMTestRunnerThread(self.test_config)
            self.test_runner.result.connect(self.process_dmm_test_runner_result)
            self.test_runner.finished.connect(self.start_iso)
        else:
            print("start iso runner thread")
            self.test_runner = ISOTestRunnerThread(self.test_config)
            self.test_runner.result.connect(self.process_iso_test_runner_result)
            self.test_runner.finished.connect(self.finished_iso)

        self.test_runner.start()
        self.update_status_bar()
        self.main_window.navigation_pane.btn_start.setIcon(QtGui.QIcon("images/pause.svg"))
        self.main_window.navigation_pane.btn_start.clicked.disconnect()
        self.main_window.navigation_pane.btn_start.clicked.connect(self.pause)

        global index_test_function, index_pins
        if index_test_function==0 and index_pins==0:
            return True # return True if it is start of the entire test
        else:
            return False

    def start_iso(self):
        global index_test_function, index_pins
        if index_test_function==global_vars.test_functions.index(global_vars.isolation_tests[0]) and index_pins==0:
            self.show_iso_dialog()
            self.test_runner = ISOTestRunnerThread(self.test_config)
            self.test_runner.result.connect(self.process_iso_test_runner_result)
            self.test_runner.finished.connect(self.finished_iso)
            self.test_runner.start()
            self.is_iso_running = True
            self.update_status_bar()
        self.update_progress_bar()

    def show_iso_dialog(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msgBox.setWindowTitle("DMM Test Completed!")
        msgBox.setText("DMM portion compleleted, connect ISO before clicking OK!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)

        returnValue = msgBox.exec()
        if returnValue != QtWidgets.QMessageBox.StandardButton.Ok: self.show_iso_dialog()
    
    def finished_iso(self):
        global index_test_function, index_pins
        if index_test_function==0 and index_pins==0:
            self.main_window.status_bar.set_message("Test Completed")
            global_vars.pop_information("All tests completed! Click export to save all data.")
    
    def pause(self):
        print("pause")
        self.test_runner.stop()
        self.test_runner.quit()
        self.test_runner.wait()
        self.main_window.status_bar.set_message("Test Paused")
        self.main_window.navigation_pane.btn_start.setIcon(QtGui.QIcon("images/play.svg"))
        self.main_window.navigation_pane.btn_start.clicked.disconnect()
        self.main_window.navigation_pane.btn_start.clicked.connect(self.main_window.start_test)

    def stop(self):
        # same as pause, but also clearing indices
        global index_test_function, index_pins
        index_test_function = 0
        index_pins = 0
        self.reset_progress_tracker()
        self.pause()
        self.test_storage = TestStorage.TestStorage(self.test_config)
        self.is_iso_running = False
        self.main_window.status_bar.set_message("Test Stopped")
    
    def process_dmm_test_runner_result(self, result:dict):
        test_function = result["test_function"]
        pin1 = result["pin1"]
        pin2 = result["pin2"]
        units = result["units"]
        t = result["t"]
        readings = result["readings"]
        pass_criteria = result["pass_criteria"]
        pin_reading = TestStorage.PinReading(pin1,pin2,units)
        pin_reading.time = t
        pin_reading.reading = readings
        pin_reading.pass_fail = self.get_pass_fail(readings[-1],units,pass_criteria)
        self.test_storage.storage[test_function].pin_readings.append(pin_reading)
        self.main_window.test_results_page.element_dict[test_function].append_test_result(
            pin1, pin2, "{0:.3f}".format(readings[-1])+" "+units, pin_reading.pass_fail
        )
        self.update_status_bar()
        self.processed_pin_combs += 1
        self.update_progress_bar()

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
        pin_reading.iso_reading = "{0:.3f}".format(reading)
        pin_reading.pass_fail = pin_reading.pass_fail and pass_fail
        test_result_row = self.main_window.test_results_page.element_dict[test_function].get_test_result_row_iso(pin1,pin2)
        iso_result = "{0:.3f}".format(reading)+" "+units
        if test_result_row is None:
            self.main_window.test_results_page.element_dict[test_function].append_test_result(
                pin1, pin2, iso_result, pass_fail
            )
        else:
            self.main_window.test_results_page.element_dict[test_function].set_test_result_row_iso(
                pin1, pin2, iso_result, pass_fail
            )
        self.update_status_bar()
        self.processed_pin_combs += 1
        self.update_progress_bar()

    def get_pass_fail(self, reading, reading_units, pass_criteria:str) -> bool:
        low, high, units = pass_criteria.replace("[","").replace("]","").split(" ")
        low, high = float(low),float(high)
        value = reading
        if reading_units!=units:
            low *= global_vars.unit_conversion[units[0]]
            high *= global_vars.unit_conversion[units[0]]
        return low<=value and value<=high
    
    def update_status_bar(self):
        global index_test_function, index_pins
        test_function = global_vars.test_functions[index_test_function]
        if isinstance(self.test_runner,ISOTestRunnerThread):
            test_function = global_vars.test_functions[index_test_function]
        if index_pins>=len(self.test_config[test_function]["Pins"]): return
        pins = self.test_config[test_function]["Pins"][index_pins]
        pin1 = pins["Pin 1"]
        pin2 = pins["Pin 2"]
        self.main_window.status_bar.set_message("Test Running", test_function, pin1, pin2)
    
    def update_progress_bar(self):
        self.main_window.status_bar.progress_bar.setValue(int(100*self.processed_pin_combs/self.total_pin_combs))

    def reset_progress_tracker(self):
        self.processed_pin_combs = 0
        self.total_pin_combs = 0
        for test_function in global_vars.test_functions+global_vars.isolation_tests:
            self.total_pin_combs += len(self.test_config[test_function]["Pins"])