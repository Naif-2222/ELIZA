import re
import random
from helpers import correct_spelling
from career_details import patterns

def response_generation(user_input):
    """
    Matches the user input with the patterns and generates an appropriate response.
    Corrects minor spelling errors.
    """
    # Correct any spelling mistakes in the input
    user_input = correct_spelling(user_input)
    matches = []
    
    for pattern, responses in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        
        if match:
            matches.append((match.group(), responses, match))
    
    # If no matches were found, return a default response
    if not matches:
        return "I`m not sure I understand. Could you explain further?"
    
    # Find the match with the longest length
    longest_match = max(matches, key=lambda x: len(x[0]))
    matched_response = random.choice(longest_match[1])
    
    # If the match contains groups (capturing groups), format the response
    if longest_match[2].groups():
        return matched_response.format(*longest_match[2].groups())
    else:
        return matched_response
