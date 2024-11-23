"""
Team Page:
Provide information about the team behind the project. This could include your name, role, 
and a brief description of the project.
"""
import streamlit as st

# Team Page

st.title("Our Team 👥")
    
st.write("") 

# Create 5 columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
 st.image("/workspaces/ELIZA/Images/u.png")
 st.write("Adwa Alshehri") 
 st.write("A brief bio about Adwa.")
 st.write("")  

with col2:
 st.image("/workspaces/ELIZA/Images/u.png")
 st.write("Sheikha Aldossari")
 st.write("A brief bio about Sheikha.")
 st.write("")  
    
with col3:
 st.image("/workspaces/ELIZA/Images/u.png")
 st.write("Lamees")
 st.write("A brief bio about Lamees.")
    
with col4:
 st.image("/workspaces/ELIZA/Images/u.png")
 st.write("Naif") 
 st.write("A brief bio about Naif.")

with col5:
 st.image("/workspaces/ELIZA/Images/u.png")
 st.write("Manaa")
 st.write("A brief bio about Manaa.")

