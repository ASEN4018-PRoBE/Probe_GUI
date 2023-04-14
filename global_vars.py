from sys import platform
from PyQt6.QtWidgets import QMessageBox

software_test = False # set to True if devices not connected, False to run software test
use_battery_pins = True # set to true if naming pins through J0X-XX

theme = ("light","dark")[1]

def pin_battery_to_pcb(pin_battery:str) -> str:
    if pin_battery=="TP1": return "63"
    p1, p2 = pin_battery.split("-")
    if p1=="J01": 
        return p2
    else:
        return str(int(p2)+37)

unit_standard = ["V", "Ohm"]
unit_conversion = {"m":10**(-3), "k":10**3, "K":10**3, "M":10**6, "G":10**9}

port_prefix = ""
if platform!="win32" and platform != "darwin":
    port_prefix = "/dev/"

# MCU setup
mcu_pid = 88
mcu_vid = 9025

# DMM setup
dmm_serial_number = "BFCVX11A920"
units_voltage_dmm = "V"
units_resistance_dmm = "Ohm"

# ISO setup
iso_serial_number = "DRCLB11A920"
iso_test_voltage = "100" # voltage applied across pins when testing
iso_resistance_range = "20" # [MOhm] must be of 2*10^N
units_resistance_iso = "Ohm"

precision_format = "{0:.2e}"

test_functions = ["Power Continuity", "Positive Circuit Continuity", "Negative Circuit Continuity", "Inline-Resistor", "Isolation Chasis", "Isolation"]

voltage_tests = ["Power Continuity"]
resistance_tests = ["Positive Circuit Continuity", "Negative Circuit Continuity", "Inline-Resistor", "Isolation Chasis", "Isolation"]
continuity_tests = ["Positive Circuit Continuity", "Negative Circuit Continuity"]
isolation_tests = ["Isolation Chasis", "Isolation"]

pins = ["J01-1", "J01-2", "J01-3", "J01-4", "J01-5", "J01-6", "J01-7", "J01-8", "J01-9", "J01-10", "J01-11", "J01-12", "J01-13", "J01-14", "J01-15", "J01-16", "J01-17", "J01-18", "J01-19", "J01-20", "J01-21", "J01-22", "J01-23", "J01-24", "J01-25", "J01-26", "J01-27", "J01-28", "J01-29", "J01-30", "J01-31", "J01-32", "J01-33", "J01-34", "J01-35", "J01-36", "J01-37", "J02-1", "J02-2", "J02-3", "J02-4", "J02-5", "J02-6", "J02-7", "J02-8", "J02-9", "J02-10", "J02-11", "J02-12", "J02-13", "J02-14", "J02-15", "J02-16", "J02-17", "J02-18", "J02-19", "J02-20", "J02-21", "J02-22", "J02-23", "J02-24", "J02-25"]

def pop_information(message:str):
    QMessageBox.information(None,"",message)

def pop_critical(message:str):
    QMessageBox.critical(None,"",message)