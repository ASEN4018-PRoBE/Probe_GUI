import time, random, pyvisa

import global_vars

class DMMInterface:
    def __init__(self, dmm_name):
        self.dmm_name = dmm_name
        self.rm = pyvisa.ResourceManager()
        self.dmm = None
        
        self.units_voltage = global_vars.units_voltage
        self.units_resistance = global_vars.units_resistance
    
    def connect(self):
        try:
            self.dmm = self.rm.open_resource(self.dmm_name)
            self.dmm.write_termination = "\n"
            self.dmm.read_termination = "\n"
        except:
            global_vars.pop_critical("Connection to Isolation Tester Failed! Please try to reconnect.")

    def voltage(self):
        if self.dmm is None:
            time.sleep(0.5)
            return random.random()
        return self.dmm.query(":MEASure:VOLTage:DC?")

    def resistance(self):
        if self.dmm is None:
            time.sleep(0.5)
            return random.random()
        return self.dmm.query(":MEASure:RESistance?")

    