import re
from helpers import correct_spelling
from career_details import patterns

# A dictionary to store the last used response for each pattern
response_history = {pattern: None for pattern, _ in patterns}

def response_generation(user_input):
    """
    Matches the user input with the patterns and generates an appropriate response.
    Ensures no immediate repetition of responses.
    """
    # Correct any spelling mistakes in the input
    user_input =re.sub(r"[^\w\s]","",user_input)
    user_input = correct_spelling(user_input)
    
    matches = []
    
    for pattern, responses in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        
        if match:
            matches.append((pattern, responses, match))
    
    # If no matches were found, return a default response
    if not matches:
        return "I'm not sure I understand. Could you explain further?"
    
    # Find the match with the longest length
    longest_match = max(matches, key=lambda x: len(x[2].group(0)))
    pattern, responses, match_obj = longest_match
    
    # Select a response that is not the same as the last one
    available_responses = [resp for resp in responses if resp != response_history[pattern]]
    if not available_responses:  # If all responses have been used, reset the history
        available_responses = responses
    
    matched_response = available_responses[0]  # Pick the first non-repeating response
    response_history[pattern] = matched_response  # Update the history with the selected response
    
    # If the match contains groups (capturing groups), format the response
    if match_obj.groups():
        return matched_response.format(*match_obj.groups())
    else:
        return matched_response
