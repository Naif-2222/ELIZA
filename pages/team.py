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
        "role": "Project Coordinator",
        "bio": "Adwa leads the coordination efforts, ensuring smooth collaboration across the team."
    },
    {
        "name": "Sheikha Aldossari",
        "image": "Images/u.png",
        "role": "Data Scientist",
        "bio": "Sheikha specializes in data analysis and modeling to extract valuable insights."
    },
    {
        "name": "Lamees",
        "image": "Images/u.png",
        "role": "Frontend Developer",
        "bio": "Lamees is responsible for designing and developing the user interface."
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
        "role": "Full Stack Developer",
        "bio": "Mana is in charge of integrating frontend and backend systems for seamless operation."
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
