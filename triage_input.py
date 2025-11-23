# triage_input.py
# This module takes input from the user and returns a dictionary.

def get_integer_input(message):
    # Helper to safely read an integer
    while True:
        text = input(message)
        if text.isdigit():
            return int(text)
        else:
            print("Please enter a valid number (only digits).")

def get_patient_info():
    print("Enter patient details:")

    name = input("Name: ")

    age = get_integer_input("Age: ")

    print("Enter symptoms separated by comma (,):")
    symptoms_input = input("Symptoms: ")

    # convert to lower case for easy matching
    symptoms_input = symptoms_input.lower()

    # split into list by comma
    raw_list = symptoms_input.split(",")

    # clean spaces around each symptom
    symptoms = []
    i = 0
    while i < len(raw_list):
        cleaned = raw_list[i].strip()
        if cleaned != "":
            symptoms.append(cleaned)
        i = i + 1

    duration_days = get_integer_input("Duration of symptoms (in days): ")

    print("Enter vital signs:")
    bp_sys = get_integer_input("BP Systolic: ")
    bp_dia = get_integer_input("BP Diastolic: ")
    spo2 = get_integer_input("Oxygen Saturation (%): ")

    # put everything into a dictionary
    data = {}
    data["name"] = name
    data["age"] = age
    data["symptoms"] = symptoms
    data["duration_days"] = duration_days
    data["bp_sys"] = bp_sys
    data["bp_dia"] = bp_dia
    data["spo2"] = spo2

    return data
