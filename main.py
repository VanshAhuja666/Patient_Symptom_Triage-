# main.py
# Main program for Patient Symptom Triage System

from triage_input import get_patient_info
from triage_engine import evaluate_triage
from triage_advice import get_advice

# statistics counters (in memory only)
total_patients = 0
urgent_count = 0
moderate_count = 0
mild_count = 0

def run_new_triage():
    global total_patients, urgent_count, moderate_count, mild_count

    data = get_patient_info()

    category, result, reason, score, main_system, department = evaluate_triage(data)

    print("\nTriage Result:", result)
    print("Category:", category)
    print("Main System:", main_system)
    print("Recommended Department:", department)
    print("Risk Score:", score)
    print("Reason:", reason)

    advice = get_advice(category, main_system)
    print("\n" + advice)

    # update in-memory statistics
    total_patients = total_patients + 1
    if category == "URGENT":
        urgent_count = urgent_count + 1
    elif category == "MODERATE":
        moderate_count = moderate_count + 1
    elif category == "MILD":
        mild_count = mild_count + 1

def show_statistics():
    print("\n=== Simple Statistics (current session) ===")
    print("Total patients triaged:", total_patients)
    print("URGENT cases:", urgent_count)
    print("MODERATE cases:", moderate_count)
    print("MILD cases:", mild_count)

def main():
    while True:
        print("\n=== Patient Symptom Triage System ===")
        print("1. New Triage")
        print("2. View Simple Statistics")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            run_new_triage()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
