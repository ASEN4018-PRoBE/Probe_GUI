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
            self.dmm = serial.Serial(port.name)
        else:
            global_vars.pop_critical("Connection to Isolation Tester Failed! Please try to reconnect.")
        