import pyvisa

import global_vars

class DMMInterface:
    def __init__(self, dmm_name):
        rm = pyvisa.ResourceManager()
        try:
            self.dmm = rm.open_resource(dmm_name)
        except:
            global_vars.pop_critical("Connection to Digital Multimeter Failed")
            quit()
        self.dmm.write_termination = "\n"
        self.dmm.read_termination = "\n"
        self.units_voltage = "V"
        self.units_resistance = "Ohm"

    def voltage(self):
        return self.dmm.query(":MEASure:VOLTage:DC?")

    def resistance(self):
        return self.dmm.query(":MEASure:RESistance?")

    