"""
The Chat Page:
Here, users will be able to interact with ELIZA. The page should simulate a conversation using pattern matching and substitutions.
"""

import streamlit as st
import re, random


# Patterns and responses for the ELIZA-like chatbot
# The patterns are regular expressions that match specific user intents or phrases
# Responses are predefined with some dynamic parts to make it feel more interactive
patterns = [
    # Greetings - Matches common ways to say hello
    (r"hi|hello|hey", [
        "Hi there! How can I assist you today?", 
        "Hello! Welcome to Toyota Sales. What can I help you with?"
    ]),
    
    # How are you - ELIZA shows empathy and acknowledges the user
    (r"how are you", [
        "I'm just a bot, but I'm here to help you find your perfect Toyota! How are you?"
    ]),
    
    # User looking for a specific type of car or model
    (r"i'm looking for (.*)", [
        "Great! Are you considering a sedan like the Corolla or an SUV like the RAV4?",
        "Looking for {0}? We have several options. What features are most important to you?"
    ]),
    
    # Specific model mentioned (e.g., RAV4)
    (r"rav4", [
        "The RAV4 is an excellent choice! Are you looking for hybrid options or all-wheel drive?",
        "The RAV4 is perfect for families and adventurers alike. Do you have a color preference?"
    ]),
    
    # Another specific model (e.g., Corolla)
    (r"corolla", [
        "The Corolla is a top pick for reliability and fuel efficiency. What’s your budget for it?",
        "The Corolla is an excellent daily driver. Would you like to explore trims or colors?"
    ]),
    
    # User mentions a color
    # It either confirms or apologizes based on whether the color is available
    (r"(red|blue|black|silver|white|gray)", [
        "That's a great color choice! The RAV4 looks amazing in {0}. Let’s move forward.",
        "Unfortunately, {0} isn't available for this model. Would you like to choose another color?"
    ]),
    
    # User says yes or agrees
    (r"yes|sure|okay", [
        "Perfect! Let me tell you more about it.",
        "Great! Let’s talk about the features and options available."
    ]),
    
    # User says no or declines
    (r"no|not really", [
        "No problem! Let me know what else you’re interested in.",
        "That’s okay! Would you like to explore other models or features?"
    ]),
    
    # User mentions price or budget
    (r"(.*)price(.*)", [
        "Toyota offers models across various price ranges. What’s your budget?",
        "Are you looking for something affordable or more on the luxury side?"
    ]),
    
    # User mentions features
    (r"(.*)features(.*)", [
        "Are you looking for safety features, entertainment systems, or something else?",
        "Toyota models come with advanced features like lane assist and adaptive cruise control. What’s a must-have for you?"
    ]),
    
    # User wants to quit or exit
    (r"quit|exit", [
        "Thanks for visiting Toyota Sales! Have a great day!",
        "Goodbye! Hope to see you again soon."
    ]),
    
    # Fallback - Catches anything that doesn't match a specific pattern
    (r"(.*)", [
        "Can you tell me more about that?",
        "I’m here to help! What are you looking for in your Toyota?",
        "Interesting! Could you elaborate a bit more?"
    ])
]


# Setting the title and description
st.title("Joe Girard - Your Personal Car Salesman")
st.write("Welcome to Joe's corner! Ask me anything about cars, deals, and the best options for your budget. Joe Girard is here to help you drive away with the perfect car!")

# Chat interface
st.header("Chat with Joe")
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []  # Initialize chat history

# User input box
user_input = st.text_input("You:", placeholder="Type your question here...")




# Function to match user input with patterns and generate a response
# Uses regex to identify the intent and dynamically adapts the response
def response_generation(user_input):
    '''
    this function will use the response list and the user analyized input
    return eliza response
    '''
    for pattern, responses in patterns:
        # Check if user input matches the current pattern
        match = re.match(pattern, user_input.lower())
        if match:
            # Pick a random response and dynamically insert user input if needed
            response = random.choice(responses)
            if "{0}" in response and match.groups():
                return response.format(*match.groups())  # Substitute group captures into the response
            return response  # Return the response if no substitution is needed
    return "Can you tell me more about that?"  # Fallback in case no pattern matches

# Process input and generate a response
if user_input:
   # Generate a response using the chatbot logic
    response = response_generation(user_input)
    
    # Append to chat history
    st.session_state["chat_history"].append((user_input, response))

# Display the chat history
st.write("### Chat History")
for user_msg, joe_response in st.session_state["chat_history"]:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**{joe_response}**")

# Reset chat history button
if st.button("Reset Chat"):
    st.session_state["chat_history"] = []
    st.success("Chat history cleared!")