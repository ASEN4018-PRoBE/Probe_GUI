import time, random, serial
import serial.tools.list_ports as stl

import global_vars

class ISOInterface:
    def __init__(self):
        self.iso = None
        self.delay = 0.3 # [s]

    def connect(self):
        port = None
        for p in stl.comports():
            if p.pid==global_vars.iso_pid and p.vid==global_vars.iso_vid:
                port = p
        if port is not None:
            self.iso = serial.Serial(port.name)

            self.iso.write(f":VOLTage {global_vars.iso_test_voltage}\n".encode()) # setup test voltage
            time.sleep(self.delay) # wait self.delay seconds to send next command

            self.iso.write(f":MOHM:RANGe {global_vars.iso_resistance_range}M\n".encode()) # setup resistance range
            time.sleep(self.delay)

        else:
            global_vars.pop_critical("Connection to Isolation Tester Failed! Please try to reconnect.")

    def resistance(self, duration) -> float:
        if not global_vars.software_test:
            if self.iso is None:
                self.connect()

            self.iso.write(":STARt\n".encode()) # start test
            time.sleep(self.delay)

            self.iso.write(":STOP\n".encode()) # stop test
            time.sleep(self.delay)

            res = self.iso.read_all().decode("utf-8")
            time.sleep(self.delay)
            if res=="": return -1.0 # unsuccessful read
            return float(res.replace("\r","").replace("\n",""))
        else:
            return random.random()       
        