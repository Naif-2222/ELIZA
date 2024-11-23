"""
Team Page:
Provide information about the team behind the project. This could include your name, role, 
and a brief description of the project.
"""
import streamlit as st

# Page title
st.title("Meet the Team")

# Brief description of the project
st.header("About the Project")
st.write("""
This project is designed to [briefly describe your project here]. 
It was developed by a talented and dedicated team committed to achieving excellence.
""")

# Team Members
st.header("Our Team")
team_members = [
    {"name": "Member 1", "role": "Project Manager", "description": "Responsible for overseeing the project and ensuring timely delivery."},
    {"name": "Member 2", "role": "Lead Developer", "description": "Focused on core development and technical architecture."},
    {"name": "Mana Saleh", 
     "role": "Developer & Git Specialis",
     "description": """Responsible for scripting, updating the project code, and managing the GitHub repository.
        Plays a key role in ensuring smooth collaboration and version control across the team.
        """},
    {"name": "Member 4", "role": "UI/UX Designer", "description": "Designed an intuitive and user-friendly interface."},
    {"name": "Member 5", "role": "QA Engineer", "description": "Ensures the quality and reliability of the project."},
]

# Display each team member
for member in team_members:
    st.subheader(member["name"])
    st.write(f"**Role:** {member['role']}")
    st.write(f"**About:** {member['description']}")
    st.write("---")
