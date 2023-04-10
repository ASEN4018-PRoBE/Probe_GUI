import time, random, serial
import serial.tools.list_ports as stl

import global_vars

class ISOInterface:
    def __init__(self):
        self.iso = None
        self.delay = 0.2 # [s]

    def connect(self, verbal=False) -> bool:
        port = None
        for p in stl.comports():
            if p.seial_number==global_vars.iso_serial_number:
                port = p
        if port is not None:
            self.iso = serial.Serial(global_vars.port_prefix+port.name)

            self.iso.write(f":VOLTage {global_vars.iso_test_voltage}\n".encode()) # setup test voltage
            time.sleep(self.delay) # wait self.delay seconds to send next command

            self.iso.write(f":MOHM:RANGe {global_vars.iso_resistance_range}M\n".encode()) # setup resistance range
            time.sleep(self.delay)
            return True

        else:
            if verbal: global_vars.pop_critical("Connection to Isolation Tester Failed! Please try to reconnect.")
            return False

    def resistance(self, duration) -> float:
        if not global_vars.software_test:
            if self.iso is None:
                self.connect(True)

            self.iso.write(":STARt\n".encode()) # start test

            time.sleep(duration) # sleep for the specified duration

            self.iso.write(":STOP\n".encode()) # stop test

            res = self.iso.read_all().decode()
            time.sleep(self.delay)
            if res=="": return -1.0 # unsuccessful read
            return float(res.replace("\r\n",""))
        else:
            time.sleep(duration)
            return random.random()       
        