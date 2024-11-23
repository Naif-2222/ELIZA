import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Mirai's Career Consulting",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Page Title
st.title("🚗💨 Welcome to **Mirai's Career Consulting**")

# Hero Image
image = Image.open("Images/Image 1.jpeg")  # Ensure the image file path is correct
st.image(image, caption="Empowering Your Career Journey", use_column_width="always")

# Introduction Section
st.write("---")
st.markdown("""
### 🌟 **Your Career Goals, Our Mission**
Welcome to **Mirai's Career Consulting**! We're committed to helping you achieve your career aspirations. 
Whether you're looking to:
- 🚀 Land your dream job,
- 📈 Advance your career, or
- 🌍 Explore new opportunities,

we provide personalized strategies and top-notch guidance to help you reach your full potential.
""")

st.write("---")

# Vision and Mission Section
st.markdown("""
### 🌟 **Why Choose Us?**
At **Mirai's Career Consulting**, we believe career development should be:
- **Personalized**: Your journey is unique, and so are our strategies.
- **Empowering**: Gain confidence in your career decisions.
- **Supportive**: We’re here to guide you every step of the way.

Our mission is to make your career journey **seamless**, **fulfilling**, and **rewarding** by connecting you with **professional specialists** who provide tailored advice.
""")

st.write("---")

# Sections of the Project
st.markdown("""
### 🔍 **Explore Our Features**
Here’s how our platform helps you:
1. **💬 Chat Page**: Chat with professional specialists to get tailored career advice.
2. **👥 Team Page**: Learn about the dedicated team behind Mirai's Career Consulting.
""")


# Footer
st.write("---")
st.markdown(
    """
    <div style="text-align: center;">
        <b>Mirai's Career Consulting</b> – Empowering Your Future. <br>
        © 2024 All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
