import time, random, pyvisa

import global_vars

class DMMInterface:
    def __init__(self, dmm_name):
        rm = pyvisa.ResourceManager()
        self.dmm = None
        try:
            self.dmm = rm.open_resource(dmm_name)
            self.dmm.write_termination = "\n"
            self.dmm.read_termination = "\n"
        except:
            global_vars.pop_critical("Connection to Digital Multimeter Failed")
        self.units_voltage = "V"
        self.units_resistance = "Ohm"

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

    