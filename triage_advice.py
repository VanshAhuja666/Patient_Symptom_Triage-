# triage_advice.py
# Returns simple advice text based on category and main system.

def get_advice(category, main_system):
    if category == "URGENT":
        if main_system == "cardiac":
            return (
                "Advice:\n"
                "- Do not ignore chest pain or pressure.\n"
                "- Avoid physical activity.\n"
                "- Seek emergency medical help immediately.\n"
            )
        elif main_system == "respiratory":
            return (
                "Advice:\n"
                "- Sit upright and try to stay calm.\n"
                "- Avoid smoke and dust.\n"
                "- Seek emergency care if breathing worsens.\n"
            )
        elif main_system == "neurological":
            return (
                "Advice:\n"
                "- Do not drive yourself.\n"
                "- Stay with someone who can observe you.\n"
                "- Seek urgent medical care.\n"
            )
        else:
            return (
                "Advice:\n"
                "- Symptoms appear serious.\n"
                "- Do not delay medical help.\n"
                "- Visit the nearest hospital or emergency unit.\n"
            )

    elif category == "MODERATE":
        if main_system == "gastrointestinal":
            return (
                "Advice:\n"
                "- Take small, frequent sips of water.\n"
                "- Avoid oily and heavy food.\n"
                "- Visit a doctor if pain or vomiting continues.\n"
            )
        else:
            return (
                "Advice:\n"
                "- Monitor your symptoms.\n"
                "- Take rest and maintain hydration.\n"
                "- Plan a doctor visit if there is no improvement.\n"
            )

    else:  
        return (
            "Advice:\n"
            "- Take rest and drink enough water.\n"
            "- Watch your symptoms for any change.\n"
            "- Seek help if symptoms become worse or last too long.\n"
        )
