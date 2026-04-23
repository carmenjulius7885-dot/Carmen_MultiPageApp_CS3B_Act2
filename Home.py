import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #f0fdf4);
    font-family: 'Segoe UI', sans-serif;
}

/* Force sidebar visible */
section[data-testid="stSidebar"] {
    display: block !important;
}

/* Header */
.header {
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

/* Glass cards */
.glass {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: 0.3s;
}

.glass:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.2);
}

/* Buttons */
div.stButton > button {
    height: 130px;
    font-size: 17px;
    font-weight: bold;
    border-radius: 15px;
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(5px);
    border: none;
}

div.stButton > button:hover {
    background: #4facfe;
    color: white;
    transform: scale(1.05);
    transition: 0.2s;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>🏠 Home</h1>
    <p>✨ Discover my journey, skills, and creative work</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🚀 Explore")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("👤\nAbout Me", use_container_width=True):
        st.switch_page("pages/About.py")

with col2:
    if st.button("💼\nProjects", use_container_width=True):
        st.switch_page("pages/Projects.py")

with col3:
    if st.button("🛠️\nSkills", use_container_width=True):
        st.switch_page("pages/Skills.py")

with col4:
    if st.button("📩\nContact", use_container_width=True):
        st.switch_page("pages/Contact.py")

st.write("---")