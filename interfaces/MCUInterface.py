import time, serial, json
import serial.tools.list_ports as stl

import global_vars

class MCUInterface:
    def __init__(self):
        self.mcu = None
    
    def connect(self):
        port = None
        for p in stl.comports():
            if p.pid==global_vars.mcu_pid and p.vid==global_vars.mcu_vid:
                port = p
        if port is not None:
            self.mcu = serial.Serial(port.name)
        else:
            global_vars.pop_critical("Cannot connect to ProBE Box!")
    
    def disconnect(self):
        if self.mcu is not None: self.mcu.close()

    def send_command(self, command):
        self.mcu.write((command+"\n").encode())

    def read(self):
        return self.mcu.read_all().decode("utf-8")

    # pcb1: v-, pcb2: v+, pcb3: sense-, pcb4: sense+
    # return True if received ack from arduino
    def switch(self, pin1, pin2, wire_type) -> bool:
        if not global_vars.software_test:
            if self.mcu is None: self.connect()
            command = {
                "command": "switch",
                "wire_type": 2,
                "pin1": global_vars.pin_map[pin1],
                "pin2": global_vars.pin_map[pin2]
            }
            if wire_type==2:
                self.mcu.write(json.dumps(command))
            elif wire_type==4:
                command["wire_type"] = 4
                self.mcu.write(json.dumps(command))
        else:
            time.sleep(0.5)
        return True

    def switch_reset(self) -> bool: # reset all switches
        if not global_vars.software_test:
            if self.mcu is None: self.connect()
        else:
            time.sleep(0.5)
        return True