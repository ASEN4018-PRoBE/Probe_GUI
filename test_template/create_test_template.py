import json
import pandas as pd

power_continuity_columns = ["Pin 1", "Pin 2"]
power_continuity_data = [["J01-1", "J01-11"]]
power_continuity = pd.DataFrame(power_continuity_data, columns=power_continuity_columns)


positive_circuit_continuity_columns = ["Pin 1", "Pin 2"]
positive_circuit_continuity_data = [
    ["J01-1", "J01-2"],
    ["J01-1", "J01-3"],
    ["J01-1", "J01-4"],
    ["J01-1", "J01-5"],
    ["J01-1", "J01-6"],
    ["J01-1", "J01-7"],
    ["J01-1", "J01-8"],
    ["J01-1", "J01-9"],
    ["J01-1", "J01-20"],
    ["J01-1", "J01-21"],
    ["J01-1", "J01-22"],
    ["J01-1", "J01-23"],
    ["J01-1", "J01-24"],
    ["J01-1", "J01-25"],
    ["J01-1", "J01-26"],
    ["J01-1", "J01-27"],
    ["J01-1", "J01-28"],
]
positive_circuit_continuity = pd.DataFrame(positive_circuit_continuity_data, columns=positive_circuit_continuity_columns)


negative_circuit_continuity_columns = ["Pin 1", "Pin 2"]
negative_circuit_continuity_data = [
    ["J01-11", "J01-12"],
    ["J01-11", "J01-13"],
    ["J01-11", "J01-14"],
    ["J01-11", "J01-15"],
    ["J01-11", "J01-16"],
    ["J01-11", "J01-17"],
    ["J01-11", "J01-18"],
    ["J01-11", "J01-19"],
    ["J01-11", "J01-29"],
    ["J01-11", "J01-30"],
    ["J01-11", "J01-31"],
    ["J01-11", "J01-32"],
    ["J01-11", "J01-33"],
    ["J01-11", "J01-34"],
    ["J01-11", "J01-35"],
    ["J01-11", "J01-36"],
    ["J01-11", "J01-37"],
]
negative_circuit_continuity = pd.DataFrame(negative_circuit_continuity_data, columns=negative_circuit_continuity_columns)


inline_resistor_columns = ["Pin 1", "Pin 2"]
inline_resistor_data = [
    ["J01-1", "J02-2"],
    ["J01-1", "J02-14"],
    ["J01-11", "J02-12"],
    ["J01-11", "J02-25"],
]
inline_resistor = pd.DataFrame(inline_resistor_data, columns=inline_resistor_columns)


isolation_chasis_columns = ["Pin 1", "Pin 2"]
isolation_chasis_data = [
    ["TP1", "J01-1"],
    ["TP1", "J01-10"],
    ["TP1", "J02-1"],
    ["TP1", "J02-3"],
    ["TP1", "J02-4"],
    ["TP1", "J02-5"],
    ["TP1", "J02-6"],
    ["TP1", "J02-7"],
    ["TP1", "J02-8"],
    ["TP1", "J02-9"],
    ["TP1", "J02-10"],
    ["TP1", "J02-11"],
    ["TP1", "J02-13"],
    ["TP1", "J02-15"],
    ["TP1", "J02-16"],
    ["TP1", "J02-17"],
    ["TP1", "J02-18"],
    ["TP1", "J02-19"],
    ["TP1", "J02-24"],
]
isolation_chasis = pd.DataFrame(isolation_chasis_data, columns=isolation_chasis_columns)


isolation_columns = ["Pin 1", "Pin 2"]
isolation_data = [
    ["J01-1", "J01-10"],
    ["J01-1", "J02-7"],
    ["J01-1", "J02-8"],
    ["J01-1", "J02-9"],
    ["J01-1", "J02-10"],
    ["J02-1", "J02-2"],
    ["J02-1", "J02-3"],
    ["J02-1", "J02-4"],
    ["J02-1", "J02-5"],
    ["J02-1", "J02-6"],
    ["J02-1", "J02-7"],
    ["J02-1", "J02-8"],
    ["J02-1", "J02-9"],
    ["J02-1", "J02-10"],
    ["J02-1", "J02-11"],
    ["J02-1", "J02-13"],
    ["J02-1", "J02-15"],
    ["J02-1", "J02-16"],
    ["J02-1", "J02-17"],
    ["J02-1", "J02-18"],
    ["J02-1", "J02-19"],
    ["J02-1", "J02-24"],

    ["J02-3", "J02-2"],
    ["J02-3", "J02-4"],
    ["J02-3", "J02-5"],
    ["J02-3", "J02-6"],
    ["J02-3", "J02-7"],
    ["J02-3", "J02-8"],
    ["J02-3", "J02-9"],
    ["J02-3", "J02-10"],
    ["J02-3", "J02-11"],
    ["J02-3", "J02-13"],
    ["J02-3", "J02-15"],
    ["J02-3", "J02-16"],
    ["J02-3", "J02-17"],
    ["J02-3", "J02-18"],
    ["J02-3", "J02-19"],
    ["J02-3", "J02-24"],

    ["J02-4", "J02-2"],
    ["J02-4", "J02-5"],
    ["J02-4", "J02-6"],
    ["J02-4", "J02-7"],
    ["J02-4", "J02-8"],
    ["J02-4", "J02-9"],
    ["J02-4", "J02-10"],
    ["J02-4", "J02-11"],
    ["J02-4", "J02-13"],
    ["J02-4", "J02-15"],
    ["J02-4", "J02-16"],
    ["J02-4", "J02-17"],
    ["J02-4", "J02-18"],
    ["J02-4", "J02-19"],
    ["J02-4", "J02-24"],

    ["J02-5", "J02-2"],
    ["J02-5", "J02-6"],
    ["J02-5", "J02-7"],
    ["J02-5", "J02-8"],
    ["J02-5", "J02-9"],
    ["J02-5", "J02-10"],
    ["J02-5", "J02-11"],
    ["J02-5", "J02-13"],
    ["J02-5", "J02-15"],
    ["J02-5", "J02-16"],
    ["J02-5", "J02-17"],
    ["J02-5", "J02-18"],
    ["J02-5", "J02-19"],
    ["J02-5", "J02-24"],

    ["J02-6", "J02-2"],
    ["J02-6", "J02-7"],
    ["J02-6", "J02-8"],
    ["J02-6", "J02-9"],
    ["J02-6", "J02-10"],
    ["J02-6", "J02-11"],
    ["J02-6", "J02-13"],
    ["J02-6", "J02-15"],
    ["J02-6", "J02-16"],
    ["J02-6", "J02-17"],
    ["J02-6", "J02-18"],
    ["J02-6", "J02-19"],
    ["J02-6", "J02-24"],

    ["J02-7", "J02-8"],
    ["J02-7", "J02-9"],
    ["J02-7", "J02-10"],

    ["J02-8", "J02-9"],
    ["J02-8", "J02-10"],

    ["J02-9", "J02-10"],

    ["J02-11", "J02-2"],
    ["J02-11", "J02-7"],
    ["J02-11", "J02-8"],
    ["J02-11", "J02-9"],
    ["J02-11", "J02-10"],
    ["J02-11", "J02-13"],
    ["J02-11", "J02-15"],
    ["J02-11", "J02-16"],
    ["J02-11", "J02-17"],
    ["J02-11", "J02-18"],
    ["J02-11", "J02-19"],
    ["J02-11", "J02-24"],

    ["J02-13", "J02-2"],
    ["J02-13", "J02-7"],
    ["J02-13", "J02-8"],
    ["J02-13", "J02-9"],
    ["J02-13", "J02-10"],
    ["J02-13", "J02-15"],
    ["J02-13", "J02-16"],
    ["J02-13", "J02-17"],
    ["J02-13", "J02-18"],
    ["J02-13", "J02-19"],
    ["J02-13", "J02-24"],

    ["J02-15", "J02-2"],
    ["J02-15", "J02-7"],
    ["J02-15", "J02-8"],
    ["J02-15", "J02-9"],
    ["J02-15", "J02-10"],
    ["J02-15", "J02-16"],
    ["J02-15", "J02-17"],
    ["J02-15", "J02-18"],
    ["J02-15", "J02-19"],
    ["J02-15", "J02-24"],

    ["J02-16", "J02-2"],
    ["J02-16", "J02-7"],
    ["J02-16", "J02-8"],
    ["J02-16", "J02-9"],
    ["J02-16", "J02-10"],
    ["J02-16", "J02-17"],
    ["J02-16", "J02-18"],
    ["J02-16", "J02-19"],
    ["J02-16", "J02-24"],

    ["J02-17", "J02-2"],
    ["J02-17", "J02-7"],
    ["J02-17", "J02-8"],
    ["J02-17", "J02-9"],
    ["J02-17", "J02-10"],
    ["J02-17", "J02-18"],
    ["J02-17", "J02-19"],
    ["J02-17", "J02-24"],

    ["J02-18", "J02-2"],
    ["J02-18", "J02-7"],
    ["J02-18", "J02-8"],
    ["J02-18", "J02-9"],
    ["J02-18", "J02-10"],
    ["J02-18", "J02-19"],
    ["J02-18", "J02-24"],

    ["J02-19", "J02-2"],
    ["J02-19", "J02-7"],
    ["J02-19", "J02-8"],
    ["J02-19", "J02-9"],
    ["J02-19", "J02-10"],
    ["J02-19", "J02-24"],

    ["J02-24", "J02-2"],
    ["J02-24", "J02-7"],
    ["J02-24", "J02-8"],
    ["J02-24", "J02-9"],
    ["J02-24", "J02-10"],
]
isolation = pd.DataFrame(isolation_data, columns=isolation_columns)

# convert all dataframes into a single json file for saving/loading purposes
df_dict = {
    "Battery Name": "8s16p Battery",
    "Power Continuity": {
        "Duration": "5",
        "Pass Criteria": "[24.0 33.6] V",
        "Pins": power_continuity.to_dict("records"),
    }, 
    "Positive Circuit Continuity": {
        "Duration": "5",
        "Pass Criteria": "[0 1] Ohm",
        "Pins": positive_circuit_continuity.to_dict("records"),
    }, 
    "Negative Circuit Continuity": {
        "Duration": "5",
        "Pass Criteria": "[0 1] Ohm",
        "Pins": negative_circuit_continuity.to_dict("records"),
    }, 
    "Inline-Resistor": {
        "Duration": "5",
        "Pass Criteria": "[9990 10010] Ohm",
        "Pins": inline_resistor.to_dict("records"),
    }, 
    "Isolation Chasis": {
        "Duration": "5",
        "Pass Criteria": "[10 inf] MOhm",
        "Pins": isolation_chasis.to_dict("records"),
    }, 
    "Isolation": {
        "Duration": "5",
        "Pass Criteria": "[10 inf] MOhm",
        "Pins": isolation.to_dict("records"),
    }}
with open("test_template.json", 'w') as outfile:
    outfile.write(json.dumps(df_dict,indent=4))