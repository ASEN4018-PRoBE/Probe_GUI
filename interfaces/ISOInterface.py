import time, random, serial
import serial.tools.list_ports as stl

import global_vars

class ISOInterface:
    def __init__(self):
        self.iso = None

    def connect(self):
        port = None
        for p in stl.comports():
            if p.pid==global_vars.iso_pid and p.vid==global_vars.iso_vid:
                port = p
        if port is not None:
            self.dmm = serial.Serial(port.name)#shoud be self.iso?
        else:
            global_vars.pop_critical("Connection to Isolation Tester Failed! Please try to reconnect.")

    def ISOtest(self) -> float:
        if not global_vars.software_test:
            if self.iso is None:
                self.connect()
            #for _ in range(2):
            self.iso.write(":VOLTage 100\n".encode())# setup test voltage
            time.sleep(self.delay) # wait self.delay seconds to send next command
            self.iso.write(":MOHM:RANGe 20M\n".encode())# setup resistance range
            time.sleep(self.delay) # wait self.delay seconds to send next command
            self.iso.write(":STARt\n".encode())# start test
            time.sleep(self.delay) # wait self.delay seconds for measurement to be ready
            self.iso.write(":STOP\n".encode())# stop test
            res = self.iso.read_all().decode("utf-8")
            if res=="": return -1.0 # unsuccessful read
            return float(res.split("\n")[-2])
        else:
            return random.random()       
        