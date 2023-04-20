import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

#------HEADER SECTION-------
st.subheader("Hi, I am Thanh Tran :wave:")
st.title("A Third years student of Information Technology at Metropolia University Of Applied Science")
st.write(" ")


#-----WHAT I DO ------
with st.container()
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
          
