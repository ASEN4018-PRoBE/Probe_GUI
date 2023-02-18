import global_vars

class Storage:
    def __init__(self, test_config):
        self.storage:dict[str,FunctionStorage] = dict()
        for test_function in global_vars.test_functions:
            duration = float(test_config[test_function]["Duration"])
            pass_criteria = test_config[test_function]["Pass Criteria"]
            self.storage[test_function] = FunctionStorage(test_function,duration,pass_criteria)

    def get_reading(self, function_name, pin1, pin2):
        if function_name not in self.storage: return None
        pin_reading = self.storage[function_name].search_pins(pin1,pin2)
        return (pin_reading.time, pin_reading.reading)

    # returns dict with test_function as key, string of csv as value
    def to_csv(self) -> dict:
        dict_csv_str = dict()
        for test_function in global_vars.test_functions:
            units = global_vars.units_voltage
            if test_function in global_vars.resistance_tests:
                units = global_vars.units_resistance
            csv_str = f"Pin1, Pin2, DMM_result [{units}], ISO_result, Pass/Fail\n"
            for pr in self.storage[test_function].pin_readings:
                str_iso = ["Fail","Pass"][pr.pass_fail]
                str_pass = ["Fail","Pass"][pr.pass_fail]
                csv_str += f"{pr.pin1},{pr.pin2},{pr.reading[-1]},{str_iso},{str_pass}\n"
            dict_csv_str[test_function] = csv_str
        return dict_csv_str

class PinReading:
    def __init__(self, pin1:str, pin2:str, units:str):
        self.pin1 = pin1
        self.pin2 = pin2
        self.units = units
        self.time = []
        self.reading = []
        self.iso_pass_fail = None
        self.pass_fail = None

class FunctionStorage:
    def __init__(self, function_name:str, duration:float, pass_criteria:str, pin_readings:list[PinReading]=[]):
        self.function_name = function_name
        self.duration = duration
        self.pass_criteria = pass_criteria # eg: [24.0 33.6] V
        self.pin_readings = pin_readings # list[PinReading]

    def search_pins(self, pin1, pin2): # returns PinReading match in self.pin_readings
        for pin_reading in self.pin_readings:
            if pin_reading.pin1==pin1 and pin_reading.pin2==pin2:
                return pin_reading
        return None