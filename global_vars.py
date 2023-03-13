from PyQt6.QtWidgets import QMessageBox

software_test = True # set to True if devices not connected, False to run software test

theme = ("light","dark")[1]

unit_conversion = {"m":10**(-3), "k":10**3, "K":10**3, "M":10**6, "G":10**9}

# MCU setup
mcu_pid = 0000
mcu_vid = 0000

# DMM setup
dmm_pid = 9123 # verified (may be identified by wire, not device)
dmm_vid = 1659 # verified (may be identified by wire, not device)
units_voltage_dmm = "V"
units_resistance_dmm = "Ohm"

# ISO setup
iso_pid = 0000
iso_vid = 0000
iso_test_voltage = "100" # voltage applied across pins when testing
iso_resistance_range = "20" # [MOhm] must be of 2*10^N
units_resistance_iso = "MOhm"

test_functions = ["Power Continuity", "Positive Circuit Continuity", "Negative Circuit Continuity", "Inline-Resistor", "Isolation Chasis", "Isolation"]

voltage_tests = ["Power Continuity"]
resistance_tests = ["Positive Circuit Continuity", "Negative Circuit Continuity", "Inline-Resistor", "Isolation Chasis", "Isolation"]
isolation_tests = ["Isolation Chasis", "Isolation"]

pins = ["J01-1", "J01-2", "J01-3", "J01-4", "J01-5", "J01-6", "J01-7", "J01-8", "J01-9", "J01-10", "J01-11", "J01-12", "J01-13", "J01-14", "J01-15", "J01-16", "J01-17", "J01-18", "J01-19", "J01-20", "J01-21", "J01-22", "J01-23", "J01-24", "J01-25", "J01-26", "J01-27", "J01-28", "J01-29", "J01-30", "J01-31", "J01-32", "J01-33", "J01-34", "J01-35", "J01-36", "J01-37", "J02-1", "J02-2", "J02-3", "J02-4", "J02-5", "J02-6", "J02-7", "J02-8", "J02-9", "J02-10", "J02-11", "J02-12", "J02-13", "J02-14", "J02-15", "J02-16", "J02-17", "J02-18", "J02-19", "J02-20", "J02-21", "J02-22", "J02-23", "J02-24", "J02-25"]

def pop_information(message:str):
    QMessageBox.information(None,"",message)

def pop_critical(message:str):
    QMessageBox.critical(None,"",message)