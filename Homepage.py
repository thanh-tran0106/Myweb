from pathlib import Path


import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "images" / "Thanh_CV_2023_Jan.pdf"
profile_pic = current_dir / "images" / "profile-pic-2.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Thanh Tran"
PAGE_ICON = ":wave:"
NAME = "Thanh Tran"
DESCRIPTION = """
A Third years student of Information Technology at Metropolia University Of Applied Science.
"""
EMAIL = "tranviet.thienthanh@gmail.com"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
