import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

st.markdown("""
<style>
.home {
    background: linear-gradient(to right, #EAE6BC, #6FB1FC);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}

.image-card {
    text-align: center;
    padding: 15px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="home">
    <h1>🏠Home</h1>
    <h4>Explore my projects, skills, and journey</h4>
    <p>Get to know me better</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #F6F4E8, #E5EEE4);
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #4A90E2;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #555;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton > button {
    height: 140px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    white-space: pre-line;
}
div.stButton > button:hover {
    border: 2px solid #6FB1FC;
    transform: scale(1.02);
    transition: 0.2s;
}
</style>
""", unsafe_allow_html=True)

st.write("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("👤\nAbout Me\nLearn more about me", use_container_width=True):
        st.session_state.page = "about"

with col2:
    if st.button("💼\nProjects\nView my work", use_container_width=True):
        st.session_state.page = "projects"

with col3:
    if st.button("🛠️\nSkills\nWhat I know", use_container_width=True):
        st.session_state.page = "skills"

with col4:
    if st.button("📩\nContact\nGet in touch", use_container_width=True):
        st.session_state.page = "contact"
        
st.write("---")

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "about":
    st.title("👤 About Me")

elif st.session_state.page == "projects":
    st.title("💼 Projects")
    
elif st.session_state.page == "skills":
    st.title("🛠️ Skills")

elif st.session_state.page == "contact":
    st.title("📩 Contact")



