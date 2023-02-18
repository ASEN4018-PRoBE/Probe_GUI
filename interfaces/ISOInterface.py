import pyvisa

import global_vars

class ISOInterface:
    def __init__(self, iso_name):
        self.iso_name = iso_name
        self.rm = pyvisa.ResourceManager()
        self.iso = None

    def connect(self):
        try:
            self.iso = self.rm.open_resource(self.iso_name)
            self.iso.write_termination = "\n"
            self.iso.read_termination = "\n"
        except:
            global_vars.pop_critical("Cannot connect to Isolation Tester!")
        