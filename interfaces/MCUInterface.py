import time, serial
import serial.tools.list_ports as stl

import global_vars

class MCUInterface:
    def __init__(self, vid, pid):
        self.vid = vid
        self.pid = pid
        self.ser = serial.Serial()
        self.ser.timeout = 0
        self.ser.baudrate = 115200
    
        port = None
        for p in stl.comports():
            if p.pid==self.pid and p.vid==self.vid:
                port = p
                break
        if port is None:
            global_vars.pop_critical("Cannot connect to ProBE Box!")
        else:
            self.ser.port = port.name
            self.ser.open()

    def send_command(self, command):
        self.ser.write((command+"\n").encode())

    def read(self):
        return self.ser.read_all().decode("utf-8")

    # pcb1: v-, pcb2: v+, pcb3: sense-, pcb4: sense+
    # return True if received ack from arduino
    def switch(self, pin_pcb1, pin_pcb2, pin_pcb3, pin_pcb4, duration) -> bool:
        time.sleep(1)
        return True
        raise NotImplementedError()

    def switch_reset() -> bool: # reset all switches
        time.sleep(1)
        return True
        raise NotImplementedError()