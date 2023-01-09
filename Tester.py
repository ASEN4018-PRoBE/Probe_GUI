import global_vars
from Storage import Storage
from interfaces import DMMInterface, ISOInterface, MCUInterface

class Tester:
    def __init__(self, test_config):
        self.test_config = test_config
        self.test_storage = Storage(test_config) # to be populated
        arduino_vid = global_vars.arduino_vid
        arduino_pid = global_vars.arduino_pid
        dmm_name = global_vars.dmm_name
        iso_name = global_vars.iso_name
        self.mcu = MCUInterface.MCUInterface(arduino_vid,arduino_pid)
        self.dmm = DMMInterface.DMMInterface(dmm_name)
        self.iso = ISOInterface.ISOInterface(iso_name)
        self.status = 0 # 0:stopped, 1:paused, 2:started
        self.time_remain = 0

    def start(self):
        for test_function in global_vars.test_functions:
            duration = float(self.test_config[test_function]["Duration"])
            self.time_remain += duration
            pass_criteria = self.test_config[test_function]["Pass Criteria"]
            for pins in self.test_config[test_function]["Pins"]:
                pin1 = pins["Pin 1"]
                pin2 = pins["Pin 2"]
                success = None
                if test_function in global_vars.voltage_tests:
                    success = self.switch(pin1, pin2, None, None)
                elif test_function in global_vars.resistance_tests:
                    success = self.switch(pin1, pin2, pin1, pin2)

    # pcb1: v-, pcb2: v+, pcb3: sense-, pcb4: sense+
    def switch(self, pin_pcb1, pin_pcb2, pin_pcb3, pin_pcb4, duration) -> bool:
        raise NotImplementedError()

    def switch_reset() -> bool: # reset all switches
        raise NotImplementedError()

    def get_pass_fail(self, pass_criteria:str):
        if len(self.time)==0: raise IndexError("empty pin reading array")
        low,high,units = pass_criteria.replace("[","").replace("]","").split(" ")
        if units==self.units:
            low,high = float(low),float(high)
            return low<=self.reading[-1] and self.reading[-1]<=high
        else:
            raise NotImplementedError("unit conversion not implemented")