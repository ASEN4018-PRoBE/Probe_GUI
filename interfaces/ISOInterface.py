import pyvisa

class ISOInterface:
    def __init__(self, iso_name):
        rm = pyvisa.ResourceManager()
        self.iso = rm.open_resource(iso_name)
        self.iso.write_termination = "\n"
        self.iso.read_termination = "\n"