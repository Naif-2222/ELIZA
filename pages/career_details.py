# Define patterns and responses
patterns = [
    # Greetings
    (r"hi|hello|hey", [
        "Hello! How can I assist you with your career today?",
        "Hi there! What's on your mind regarding your career?",
        "Hey! How can I help you achieve your career goals?"
    ]),
    (r"how are you", [
        "I'm here to guide you in your career. How are you feeling about your career today?",
        "I'm just a chatbot, but I'm ready to help. How are you doing?"]),
        
    # Job Searching
    # Captures phrases related to looking for or searching for jobs
    (r"find|search|looking for", ["Job searching can be challenging. What type of role are you looking for?"]),
    
    # Career Change
    # Captures phrases indicating someone wants to change or switch careers
    (r"change|switch|new career", ["Why do you want to make a career change?"]),

    # General Job-Related Inquiry
    # Captures general terms like "job" or "work" to inquire about career-related questions
    (r"job|work", ["What specific career-related questions do you have?"]),

    # Skills and Strengths
    # Captures discussions about skills and strengths (critical for self-assessment and career progression)
    (r"skills|strengths", ["Identifying your strengths is crucial. What do you consider your top skills?"]),

    # Skill-Specific Inquiries
    # Captures mentions of specific technical and soft skills, prompting questions about their value
    (r"\b(?:python|java|javascript|sql|excel|communication|leadership|project management|teamwork|negotiation|design|marketing|analytical|management)\b", 
     ["How much do you think you will be paid for this skill?"]),


    # Career Level (Senior, Manager, Junior)
    # Captures various career levels (e.g., senior, junior, or manager)
    (r"senior|manager|junior|entry level|chief", ["Why are you aiming for this level?"]),

    # Salary Expectations
    # Captures queries related to salary or compensation
    (r"salary|money", ["What are your salary expectations?"]),

    # Salary Range
    # Captures numeric salary expectations or salary discussions with an optional comma for formatting
    (r"(\d{1,3}(?:,\d{3})*)(.*)", ["Why do you think you deserve this amount?"]),
        
    # overwhelm & Stress
    # Captures discussions about work-life balance, stress, or feeling overwhelmed
    (r"\bstress(ed|ing|ful|es)?\b|\boverwhelm(ed|ing|ing)?\b", ["Why do you feel that way?"])

    # Lack of Growth/Opportunity
    # A broader pattern for capturing multiple phrases regarding stagnation or lack of progression
    (r"(no growth|no promotion|lack of opportunity|no advancement|stagnant career|limited development|no progression|career plateau|no personal growth|no skill improvement)", 
     ["What steps do you think you could take to overcome this?"]),

    # Courses and Certifications
    # Captures mentions of professional development through courses or certifications
    (r"courses|certifications|learning|training|education|upskilling|reskilling", ["What skills are you aimming to enchance?"]),

    # Job Dissatisfaction
    # Captures feelings of unhappiness, dissatisfaction, or lack of fulfillment in a job
    (r"unhappy|dissatisfied|not fulfilled", ["Job satisfaction is important for long-term happiness. What make you feel that way?"]),

    # Workplace Conflict
    # Captures discussions about conflicts with bosses, coworkers, or workplace issues
    
    # Workplace Conflict
    # Captures discussions about conflicts with bosses, coworkers, or workplace issues
    (r"\b(boss|supervisor|manager|team|coworker|colleague|client|customer|partner)\s*(conflict|disagreement|issue|problem|fight|dispute|frustration)\b", 
    ["What do you think might help resolve this?"])

    # Yes Response
    # Captures a positive "yes" response
    (r"yes", ['Can you tell me more about what you have in mind?']),

    # No Response
    # Captures a negative "no" response, encouraging deeper inquiry
    (r"no", ['Why not?']),

    # End of Conversation
    # Captures exit or goodbye phrases to gracefully end the conversation
    (r"(quit|exit|bye)", ["Goodbye! Best of luck with your career. Feel free to reach out anytime."]),
    
    # Default Catch-All
    # Captures any other input that doesn’t match the above patterns, encouraging the user to elaborate
    (r".*", ["I'm not sure I understand. Can you tell me more about what you're looking for?"])
]
