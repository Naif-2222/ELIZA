"""
The Chat Page:
Here, users will be able to interact with ELIZA. The page should simulate a conversation using pattern matching and substitutions.
"""

import streamlit as st

# Setting the title and description
st.title("Joe Girard - Your Personal Car Salesman")
st.write("Welcome to Joe's corner! Ask me anything about cars, deals, and the best options for your budget. Joe Girard is here to help you drive away with the perfect car!")

# Chat interface
st.header("Chat with Joe")
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []  # Initialize chat history

# User input box
user_input = st.text_input("You:", placeholder="Type your question here...")

# Predefined responses to common keywords:
respons = [{'buy':["What do you look for the most when you decide to buy a new car?","What are your top priorities when you`re looking to buy a new car?"]},
            {'feature':['What kind of features do you have in your main?',"Is there a specific feature would you like to have?"]},
            {'yes':['Why do you think so?','can you elaborate?']},
            {'no':['Why do you think so?','can you elaborate?']},
            {'accessibility' : ["Are you looking for a car with specific accessibility features, such as wheelchair access or adaptive controls?"]},
            {'reliability':['Are you specifically looking for a car with high reliability and low maintenance?']},
            {'maintenance':["Are you interested in cars with technology that helps track maintenance needs?","Are you looking for a car that`s easy to maintain"]}
            ]

def user_input_analysis():
    '''this function suppoes to prepare the input for the generation of eliza response'''
    pass

def response_generation():
    '''
    this function will use the response list and the user analyized input
    return eliza response
    '''

# Process input and generate a response
if user_input:
    # Mock response for now; replace this with your chatbot logic
    response = f"Joe: That's a great question! Let me tell you about our latest deals."
    
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