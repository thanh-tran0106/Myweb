from pathlib import Path


import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "images" / "CV.pdf"
profile_pic = current_dir / "images" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Thanh Tran"
PAGE_ICON = ":wave:"
NAME = "Thanh Tran"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "tranviet.thienthanh@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)





st.sidebar.success("Select a demo above.")


#------HEADER SECTION-------
st.subheader("Hi, I am Thanh Tran :wave:")
st.title("A Third years student of Information Technology at Metropolia University Of Applied Science")
st.write(" ")


#-----WHAT I DO ------
with st.container():
    st.write("--- ")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
                """
                 With broad experiences in Infrastructure, ranging from networking, DevOps and cloud solutions 
                 I have been working and hands on with multiple school projects such as creating an automated 
                 pipeline that provisions services to Docker Swarm/Kubernetes using orchestration tools Jenkins
                 and Github Action.I am familiar with containerization (Docker), orchestration (Ansible, Jenkins)
                 and cloud solutions (Docker Swarm, Kubernetes)
                 
                 """)
