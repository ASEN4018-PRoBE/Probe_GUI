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
            self.mcu = serial.Serial(global_vars.port_prefix+port.name)
            time.sleep(1)
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
            if global_vars.use_battery_pins:
                pin1 = global_vars.pin_battery_to_pcb(pin1)
                pin2 = global_vars.pin_battery_to_pcb(pin2)
            if self.mcu is None: self.connect()
            command = ["2", pin1, pin2]
            if wire_type==4:
                command[0] = "4"
            self.mcu.write(",".join(command).encode())
        else:
            time.sleep(0.5)
        return True

    def switch_reset(self) -> bool: # reset all switches
        if not global_vars.software_test:
            if self.mcu is None: self.connect()
            self.mcu.write("1") # 1 for pins reset
        else:
            time.sleep(0.5)
        return True

    def switch_info(self):
        print(self.read().split("\n")[-1])