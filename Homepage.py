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
A Third years student of Information Technology at Metropolia University Of Applied Science.
"""
EMAIL = "tranviet.thienthanh@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "  ",
    "LinkedIn": "  ",
    "GitHub": "   ",
    "Twitter": "   ",
}
PROJECTS = {
    "🏆   ",
    "🏆   ",
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



st.sidebar.success("Select a demo above.")
