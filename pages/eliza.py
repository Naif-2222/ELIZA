import re
import random
from helpers import correct_spelling
from career_details import patterns

def response_generation(user_input):
    """
    Matches the user input with the patterns and generates an appropriate response.
    Corrects minor spelling errors.
    """
    user_input = re.sub(r"[^\w\s]", "", user_input)
    user_input = correct_spelling(user_input)
    for pattern, responses in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            if match.groups():
                return random.choice(responses).format(*match.groups())
            return random.choice(responses)
    return "I’m not sure I understand. Could you explain further?"