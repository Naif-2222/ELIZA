import re

def correct_spelling(input_text):
    """
    A simple spelling correction function to handle minor misspellings.
    """
    corrections = {
        "jop": "job",
        "carreer": "career",
        "intreview": "interview",
        "strenghts": "strengths",
        "degre": "degree",
        "majar": "major"
    }
    for wrong, correct in corrections.items():
        input_text = re.sub(rf"\b{wrong}\b", correct, input_text, flags=re.IGNORECASE)
    return input_text
