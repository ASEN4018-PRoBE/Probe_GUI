import pyvisa

import global_vars

class ISOInterface:
    def __init__(self, iso_name):
        rm = pyvisa.ResourceManager()
        try:
            self.iso = rm.open_resource(iso_name)
        except:
            global_vars.pop_critical("Connection to Isolation Tester Failed")
            quit()
        self.iso.write_termination = "\n"
        self.iso.read_termination = "\n"