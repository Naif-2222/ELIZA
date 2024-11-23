"""
The Chat Page:
Here, users will be able to interact with ELIZA. The page should simulate a conversation using pattern matching and substitutions.
"""

import streamlit as st
import re

patterns = [
    # Greetings
    (r"hi|hello|hey", "Hello! How can I assist you with your career today?"),

    (r"find|search|looking for", "Job searching can be challenging. What type of role are you looking for?"),
    
    (r"change|switch|new career", "Why do you want to?"),

    (r"job|work", "What specific career-related questions do you have?"),
    
    (r"skills|strengths", "Identifying your strengths is crucial. What do you consider your top skills?"),

    (r"\b(?:python|java|javascript|sql|excel|communication|leadership|project management|teamwork|negotiation|design|marketing|analytical|management)\b", "How much do you think you will be paid for this skill?"),

    (r"interview|prepare", "Preparing for an interview is key. What position are you interviewing for?"),

    (r"senior|manager|junior", "Why are you aimming for this level?"),

    (r"salary|money", "What are your expectations?"),

    (r"(\d{1,3}(?:,\d{3})*)(.*)", "Why do you think you deserve this amount?"),
        
    (r"work-life balance|stress|overwhelmed", "Balancing work and personal life can be tough. How are you managing your time currently?"),
    
    (r"(no growth|no promotion|stagnation|lack of opportunity)", "What steps do you think you could take to overcome this?"),

    (r"advance|promotion|grow in my career", "Career growth requires strategy and skill development. What steps are you taking to advance?"),
        
    (r"unhappy|dissatisfied|not fulfilled", "Job satisfaction is important for long-term happiness. What aspects of your job are making you feel that way?"),
    
    (r"boss|coworker|conflict|workplace", "Dealing with difficult colleagues or managers can be tough. Have you considered discussing your concerns with them?"),
         
    (r"courses|certifications|learning", "Continuous learning can open up new opportunities. Have you considered taking any courses or certifications to further your career?"),
    
    (r"yes", 'can you tell me more?'),

    (r"no", 'why not?'),

    # End of Conversation
    (r"(quit|exit|bye)", "Goodbye! Best of luck with your career. Feel free to reach out anytime."),
    
    # Default catch-all
    (r".*", "I'm not sure I understand. Can you tell me more about what you're looking for?")
]


def response_generation(user_input):
    '''
    This function matches the user input with the patterns and generates an appropriate response.
    '''
    for pattern, response in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response  
    
    return "Can you tell me more?"


def run_chatbot():
    st.title("Career Coach")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []  

    user_input = st.chat_input(placeholder="Type your question here...")

    if user_input:
        response = response_generation(user_input)
        
        st.session_state["chat_history"].append((user_input, response))

    for user_msg, joe_response in st.session_state["chat_history"]:
            with st.chat_message("user"):
                st.markdown(user_msg)
            with st.chat_message("assistant"):
                st.markdown(joe_response)

run_chatbot()
