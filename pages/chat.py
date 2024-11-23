import streamlit as st
from eliza import response_generation

def run_chatbot():
    st.title("Career Coach - ELIZA")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    user_input = st.chat_input(placeholder="Type your question here...")

    if user_input:
        # Generate response
        response = response_generation(user_input)

        # Save chat history
        st.session_state["chat_history"].append((user_input, response))

    # Display chat history
    for user_msg, bot_response in st.session_state["chat_history"]:
        with st.chat_message("user"):
            st.markdown(user_msg)
        with st.chat_message("assistant"):
            st.markdown(bot_response)

run_chatbot()
