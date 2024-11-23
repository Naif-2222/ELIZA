import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="ELIZA Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page title and introduction
st.title("🤖 **ELIZA Chatbot**")
st.subheader("Your Career Guidance Companion")

st.write("""
Welcome to **ELIZA**, your go-to chatbot for career advice, job searching, and skill development. 
Designed with advanced **natural language processing**, ELIZA provides personalized insights to 
help you achieve your career goals.
""")

# # Add a hero image (optional)
# image = Image.open("Images/chatbot_cover.png")  # Replace with your image
# st.image(image, caption="Your Career Journey Starts Here", use_column_width="always")

# Features section
st.write("---")
st.markdown("### 🌟 **Key Features**")
features = [
    "💼 **Career Guidance**: Tailored advice to help you navigate your career.",
    "🔍 **Job Searching**: Get tips and resources for finding the perfect role.",
    "📈 **Skill Development**: Learn what skills are in demand and how to acquire them.",
    "🧠 **AI-Powered Insights**: Advanced NLP ensures meaningful conversations."
]

for feature in features:
    st.markdown(feature)

# Add an interactive call-to-action section
st.write("---")
st.markdown("### 🚀 **Start Your Career Journey Now**")
st.markdown("""
Click the button app on right to chat with ELIZA and unlock your career potential.
""")


# Footer
st.write("---")
st.markdown(
    """
    <div style="text-align: center;">
        Powered by <b>ELIZA Chatbot</b> – Your Career Assistant. <br>
        © 2024 All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
