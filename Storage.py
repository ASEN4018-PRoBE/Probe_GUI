import numpy
import global_vars

class PinReading:
    def __init__(self, pin1:str, pin2:str, units:str, start_timestamp:float):
        self.pin1 = pin1
        self.pin2 = pin2
        self.units = units
        self.start_timestamp = start_timestamp
        self.time = numpy.array([])
        self.reading = numpy.array([])
        self.pass_fail = None
        self.isolation_pass_fail = None

class FunctionStorage:
    def __init__(self, function_name:str, duration:float, pass_criteria:str, pin_readings:list[PinReading]=[]):
        self.function_name = function_name
        self.duration = duration
        self.pass_criteria = pass_criteria # for example: [24.0 33.6] V
        self.pin_readings = pin_readings

    def search_pins(self, pin1, pin2) -> PinReading:
        for pin_reading in self.pin_readings:
            if pin_reading.pin1==pin1 and pin_reading.pin2==pin2:
                return pin_reading
        return None

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