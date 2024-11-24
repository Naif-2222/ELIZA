import re

def correct_spelling(input_text):
    """
    A simple spelling correction function to handle minor misspellings.
    """
    # First, normalize repeated letters (e.g., "helloooo" -> "hello")
    input_text = re.sub(r'(\w)\1{2,}', r'\1', input_text)  # Matches 3+ repeated letters

    corrections = {
        "jop": "job",
        "jpb": "job",
        "jobb": "job",
        "carreer": "career",
        "carrer": "career",
        "carear": "career",
        "intreview": "interview",
        "interveiw": "interview",
        "intervview": "interview",
        "strenghts": "strengths",
        "strenths": "strengths",
        "stregnths": "strengths",
        "degre": "degree",
        "degee": "degree",
        "dgree": "degree",
        "majar": "major",
        "majjor": "major",
        "specilization": "specialization",
        "speclization": "specialization",
        "skils": "skills",
        "skilz": "skills",
        "sallery": "salary",
        "salery": "salary",
        "slaray": "salary",
        "oppertunity": "opportunity",
        "opurtunity": "opportunity",
        "oppurtunity": "opportunity",
        "opertunity": "opportunity",
        "dissatisfiedd": "dissatisfied",
        "unhapppy": "unhappy",
        "maneger": "manager",
        "managr": "manager",
        "supervizor": "supervisor",
        "superviser": "supervisor",
        "teem": "team",
        "coworkr": "coworker",
        "collegue": "colleague",
        "collaegue": "colleague"
    }
    for wrong, correct in corrections.items():
        input_text = re.sub(rf"\b{wrong}\b", correct, input_text, flags=re.IGNORECASE)
    return input_text
