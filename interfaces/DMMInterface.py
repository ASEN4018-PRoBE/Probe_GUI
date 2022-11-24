import pyvisa

class DMMInterface:
    def __init__(self, dmm_name):
        rm = pyvisa.ResourceManager()
        self.dmm = rm.open_resource(dmm_name)
        self.dmm.write_termination = "\n"
        self.dmm.read_termination = "\n"

    def voltage(self):
        return self.dmm.query(":MEASure:VOLTage:DC?")

    def resistance(self):
        return self.dmm.query(":MEASure:RESistance?")

    