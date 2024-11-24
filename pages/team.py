"""
Team Page:
Provide information about the team behind the project. This could include your name, role, 
and a brief description of the project.
"""
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Our Team", page_icon="👥", layout="wide")

# Title and Introduction
st.title("Meet Our Team 👥")
st.write("""
We are a team of passionate professionals committed to achieving excellence in every aspect of this project. 
Learn more about us below!
""")

# Add a divider for better separation
st.divider()

# Team Members Data
team_members = [
    {
        "name": "Adwa Alshehri",
        "image": "Images/u.png",
        "role": "Streamlit page designer",
        "bio": "Adwa handled the streamlit code in team page and main page."
    },
    {
         "name": "Shaykhah Aldawsari",
        "image": "Images/u.png",
        "role": "Developer",
        "bio": "Build the main logic and enhanced the accuracy of the system"
    },
    {
       "name": "Lamees Aloqlan",
        "image": "Images/u.png",
        "role": "Developer & Designer",
        "bio": "Lamees is responsible for designing chat UI and enhancing the main function & collect the pattern."
    },
    {
        "name": "Naif Abdullah Alsabhan",
        "image": "Images/u.png",
        "role": "object orianted design",
        "bio": "Naif handles backend development and ensures the application runs smoothly where he uses oop design."
    },
    {
        
         "name": "Mana Saleh",
        "image": "Images/u.png",
        "role": "Develper & Deployment",
        "bio": "Mana is in charge of developing and breaking down the code as will as deployment."
    }
]

# Display Team Members
cols = st.columns(5)  # Create 5 columns for equal spacing

for idx, member in enumerate(team_members):
    with cols[idx % 5]:  # Use each column for one member
        st.image(member["image"], width=120, use_column_width="always")  # Resize the image
        st.markdown(f"### {member['name']}")
        st.markdown(f"**{member['role']}**")
        st.caption(member["bio"])  # Display the bio as a smaller caption

# Add a footer
st.write("---")
st.write("💼 **Powered by Our Team** – Dedicated to innovation and excellence.")
