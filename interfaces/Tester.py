import time, numpy
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot

import global_vars
from interfaces import DMMInterface, ISOInterface, MCUInterface

index_test_function = 0
index_pins = 0

class TestRunnerThread(QThread):
    def __init__(self, test_config):
        super(QThread, self).__init__()
        self.test_config = test_config
        self.mcu = MCUInterface.MCUInterface(global_vars.arduino_vid, global_vars.arduino_pid)
        self.dmm = DMMInterface.DMMInterface(global_vars.dmm_name)
        self.iso = ISOInterface.ISOInterface(global_vars.iso_name)
        self.result = pyqtSignal(dict)

    def run(self):
        global index_test_function, index_pins
        while True:
            test_function = global_vars.test_functions[index_test_function]
            pass_criteria = self.test_config[test_function]["Pass Criteria"]
            duration = float(self.test_config[test_function]["Duration"])
            pins = self.test_config[test_function]["Pins"][index_pins]
            pin1 = pins["Pin 1"]
            pin2 = pins["Pin 2"]

            time_start = time.time()
            reading = numpy.array([])
            t = numpy.array([])
            units = self.dmm.units_voltage if (test_function in global_vars.voltage_tests) else self.dmm.units_resistance
            while (time.time()-time_start)<=duration:
                if test_function in global_vars.voltage_tests:
                    if self.mcu.switch(pin1, pin2, None, None):
                        numpy.append(reading, self.dmm.voltage())
                elif test_function in global_vars.resistance_tests: # four wire meas
                    if self.mcu.switch(pin1, pin2, pin1, pin2):
                        numpy.append(reading, self.dmm.resistance)
                numpy.append(t, time.time()-time_start)

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
                    return # complete and stop

class Tester:
    def __init__(self, test_config, main_window):
        self.test_config = test_config
        self.main_window = main_window
        self.test_storage = Storage(test_config) # to be populated
        self.test_runner = TestRunnerThread(test_config)
        self.test_runner.result.connect(self.proceess_test_runner_result)

    def start(self):
        self.test_runner.start()
    
    def pause(self):
        self.test_runner.terminate()

    def stop(self):
        self.test_runner.terminate()
        global index_test_function, index_pins
        index_test_function = 0
        index_pins = 0
    
    @pyqtSlot(dict)
    def proceess_test_runner_result(self, result:dict):
        test_function = result["test_function"]
        pin1 = result["pin1"]
        pin2 = result["pin2"]
        units = result["units"]
        t = result["t"]
        reading = result["reading"]
        pass_criteria = result["pass_criteria"]
        pin_reading = PinReading(pin1,pin2,units)
        pin_reading.time = t
        pin_reading.reading = reading
        pin_reading.pass_fail = self.get_pass_fail(reading,units,pass_criteria)
        self.test_storage.storage[test_function].pin_readings.append()
        self.main_window.test_results_page.element_dict[test_function].append_test_result(pin1,pin2,reading[-1],pin_reading.pass_fail)

    def get_pass_fail(self, reading, reading_units, pass_criteria:str) -> bool:
        low,high,units = pass_criteria.replace("[","").replace("]","").split(" ")
        low,high = float(low),float(high)
        if reading_units==units:
            return low<=reading and reading<=high
        else:
            raise NotImplementedError("unit conversion not implemented")

class Storage:
    def __init__(self, test_config):
        self.storage = dict()
        for test_function in global_vars.test_functions:
            duration = float(test_config[test_function]["Duration"])
            pass_criteria = test_config[test_function]["Pass Criteria"]
            self.storage[test_function] = FunctionStorage(test_function,duration,pass_criteria)

    def get_reading(self, function_name, pin1, pin2):
        if function_name not in self.storage: return False
        pin_reading = self.storage[function_name].search_pins(pin1,pin2)
        return (pin_reading.time, pin_reading.reading)

class FunctionStorage:
    def __init__(self, function_name:str, duration:float, pass_criteria:str, pin_readings=[]):
        self.function_name = function_name
        self.duration = duration
        self.pass_criteria = pass_criteria # eg: [24.0 33.6] V
        self.pin_readings = pin_readings # list[PinReading]

    def search_pins(self, pin1, pin2): # returns the PinReading match in self.pin_readings
        for pin_reading in self.pin_readings:
            if pin_reading.pin1==pin1 and pin_reading.pin2==pin2:
                return pin_reading
        return None

class PinReading:
    def __init__(self, pin1:str, pin2:str, units:str):
        self.pin1 = pin1
        self.pin2 = pin2
        self.units = units
        self.time = numpy.array([])
        self.reading = numpy.array([])
        self.pass_fail = None
        self.isolation_pass_fail = None