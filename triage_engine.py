# triage_engine.py
# Evaluates patient data and returns
# category, short result, reason, score, main_system, department.

import triage_rules

def normalize_symptoms(symptoms):
    cleaned = []
    i = 0
    while i < len(symptoms):
        s = symptoms[i].lower().strip()
        if s != "":
            cleaned.append(s)
        i = i + 1
    return cleaned

def count_matches(symptoms, group_list):
    count = 0
    i = 0
    while i < len(group_list):
        g = group_list[i]
        j = 0
        while j < len(symptoms):
            s = symptoms[j]
            if g == s or g in s:
                count = count + 1
            j = j + 1
        i = i + 1
    return count

def get_main_system(symptoms):
    cardiac_count = count_matches(symptoms, triage_rules.CARDIAC_SYMPTOMS)
    resp_count = count_matches(symptoms, triage_rules.RESPIRATORY_SYMPTOMS)
    neuro_count = count_matches(symptoms, triage_rules.NEUROLOGICAL_SYMPTOMS)
    gi_count = count_matches(symptoms, triage_rules.GI_SYMPTOMS)
    gen_count = count_matches(symptoms, triage_rules.GENERAL_SYMPTOMS)

    main_system = "general"
    max_count = gen_count

    if cardiac_count > max_count:
        main_system = "cardiac"
        max_count = cardiac_count
    if resp_count > max_count:
        main_system = "respiratory"
        max_count = resp_count
    if neuro_count > max_count:
        main_system = "neurological"
        max_count = neuro_count
    if gi_count > max_count:
        main_system = "gastrointestinal"
        max_count = gi_count

    return main_system

def get_department(main_system):
    if main_system == "cardiac":
        return "Cardiology"
    elif main_system == "respiratory":
        return "Pulmonology"
    elif main_system == "neurological":
        return "Neurology"
    elif main_system == "gastrointestinal":
        return "Gastroenterology"
    else:
        return "General Medicine"

def evaluate_triage(data):
    symptoms = normalize_symptoms(data["symptoms"])
    bp_sys = data["bp_sys"]
    bp_dia = data["bp_dia"]
    spo2 = data["spo2"]
    age = data["age"]
    duration = data["duration_days"]

    main_system = get_main_system(symptoms)
    department = get_department(main_system)

    score = 0
    urgent_flag = False

    score = score + count_matches(symptoms, triage_rules.CARDIAC_SYMPTOMS) * 2
    score = score + count_matches(symptoms, triage_rules.RESPIRATORY_SYMPTOMS) * 2
    score = score + count_matches(symptoms, triage_rules.NEUROLOGICAL_SYMPTOMS) * 3

    infection_count = count_matches(symptoms, triage_rules.INFECTION_SYMPTOMS)
    score = score + infection_count

    if bp_sys > 180 or bp_dia > 110:
        urgent_flag = True
        score = score + 4
    elif bp_sys > 160 or bp_dia > 100:
        score = score + 2

    if spo2 < 90:
        urgent_flag = True
        score = score + 4
    elif spo2 < 94:
        score = score + 2

    if age >= 65:
        score = score + 2
    if duration > 3:
        score = score + 1

    if urgent_flag or score >= 9:
        category = "URGENT"
    elif score >= 5:
        category = "MODERATE"
    else:
        category = "MILD"

    if category == "URGENT":
        if main_system == "cardiac":
            result = "URGENT - Possible cardiac emergency."
            reason = "Heart related symptoms with high risk score."
        elif main_system == "respiratory":
            result = "URGENT - Serious breathing problem."
            reason = "Breathing symptoms with abnormal vital signs."
        elif main_system == "neurological":
            result = "URGENT - Possible brain or nerve emergency."
            reason = "Neurological signs with high risk."
        else:
            result = "URGENT - Immediate medical attention needed."
            reason = "High overall risk based on symptoms and vitals."
    elif category == "MODERATE":
        if infection_count > 0:
            result = "MODERATE - Likely infection. Doctor visit suggested."
            reason = "Symptoms suggest infection that needs review."
        else:
            result = "MODERATE - Medical consultation recommended."
            reason = "Some risk factors present that require evaluation."
    else:
        result = "MILD - Self-care and observation may be enough."
        reason = "Low risk score and no strong danger signs."

    return category, result, reason, score, main_system, department
