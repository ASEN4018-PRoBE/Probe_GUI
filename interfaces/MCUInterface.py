import serial
import serial.tools.list_ports as stl

class MCUInterface:
    def __init__(self, vid, pid):
        self.vid = vid
        self.pid = pid
        self.ser = serial.Serial()
        self.ser.timeout = 0
        self.ser.baudrate = 115200
    
    def connect(self):
        port = None
        for p in stl.comports():
            if p.pid==self.pid and p.vid==self.vid:
                port = p
                break
        if port is None:
            return
        self.ser.port = port.name
        self.ser.open()

    def send_command(self, command):
        self.ser.write(bytearray((command+"\n").encode()))

    def read(self):
        return self.ser.read_all().decode("utf-8")