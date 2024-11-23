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
        "I'm just a chatbot, but I'm ready to help. How are you doing?"
    ]),

    # Career or Job
    (r"need a (job|career)", [
        "What type of job are you looking for?",
        "Can you share your career goals so I can guide you better?"
    ]),

    # Education and Major
    (r"senior|manager|junior", [
        "Why are you aimming for this level?",
    ]),

    (r"my major is (.*)", [
        "{0} is a great field! What kind of jobs are you considering with it?",
        "How do you plan to use your major in {0} to achieve your goals?"
    ]),

    # Skills
    (r"(skills|strengths|weaknesses)", [
        "What are your top strengths, and how do you think they will benefit your career?",
        "Identifying your skills is crucial. What do you consider your top strengths?"
    ]),
    (r"\b(python|java|sql|communication|leadership|marketing)\b", [
        "{0} is a valuable skill! How are you showcasing it in your career?",
        "{0} is in demand. Have you highlighted it in your resume or LinkedIn?"
    ]),

    # Interview Preparation
    (r"interview|prepare", [
        "Preparing for an interview is key. What role are you preparing for?",
        "Interviews are a great opportunity to shine! What do you need help with?"
    ]),
    (r"questions|ask", [
        "What questions do you have in mind for the interviewer?",
        "Asking insightful questions can leave a good impression. What’s on your list?"
    ]),

    # Career Growth
    (r"grow|promotion|advance", [
        "Career growth requires planning and skill development. What steps are you currently taking?",
        "Are you exploring new responsibilities or networking opportunities for growth?"
    ]),

    # Salary and Negotiation
    (r"salary|pay|money", [
        "What are your salary expectations for your next role?",
        "Knowing your worth is important. What salary range are you aiming for?"
    ]),
    (r"(\d{1,3}(?:,\d{3})+)", [
        "Why do you think you're worth {0}? What unique skills do you bring?",
        "That’s an ambitious goal of {0}. How did you arrive at that number?"
    ]),

    # Work-Life Balance
    (r"stress|overwhelmed|work-life balance", [
        "Balancing work and life can be challenging. How are you managing your time?",
        "Work-life balance is so important. What’s stressing you out right now?"
    ]),

    # Default Catch-all
    (r".*", [
        "I’m not sure I understand. Could you rephrase?",
        "That’s interesting. Can you clarify or provide more details?"
    ])
]