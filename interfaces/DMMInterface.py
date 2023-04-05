import time, random, serial
import serial.tools.list_ports as stl

import global_vars

class DMMInterface:
    def __init__(self):
        self.dmm = None
        self.delay = 0.5 # [s]
    
    def connect(self, verbal=False):
        port = None
        for p in stl.comports():
            if p.pid==global_vars.dmm_pid and p.vid==global_vars.dmm_vid:
                port = p
        if port is not None:
            self.dmm = serial.Serial(port.name)
            return True
        else:
            if verbal: global_vars.pop_critical("Connection to Digital Multimeter Failed! Please try to reconnect.")
            return False

    def voltage(self) -> float:
        if not global_vars.software_test:
            if self.dmm is None:
                self.connect(True)
            self.dmm.write(":MEASure:VOLTage:DC?\r\n".encode())
            time.sleep(self.delay) # wait self.delay seconds for measurement to be ready
            res = self.dmm.read_all().decode()
            if res=="": return -1.0 # unsuccessful read
            return float(res.split("\n")[-2])
        else:
            time.sleep(self.delay)
            return random.random()       

    def resistance(self) -> float:
        if not global_vars.software_test:
            if self.dmm is None:
                self.connect()
            self.dmm.write(":MEASure:FRESistance?\r\n".encode())
            time.sleep(self.delay)
            res = self.dmm.read_all().decode()
            if res=="": return -1.0
            return float(res.split("\n")[-2])
        else:
            time.sleep(self.delay)
            return random.random()