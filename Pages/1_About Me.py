import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #8ABEB9, #B7E5CD);
    font-family: 'Segoe UI', sans-serif;
}

.hero {
    background: linear-gradient(135deg, #456882, #234C6A);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.glass {
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.profile {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.section-title {
    color: #333;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>👤 About Me</h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="glass">

    <h3 class="section-title">👋 Hello!</h3>
    <p>
    I'm <b>Julius P. Carmen</b>, an aspiring web developer and Computer Science student.
    I enjoy building interactive applications and exploring modern technologies.
    </p>

    <h3 class="section-title">🎯 Goals</h3>
    <ul>
        <li>🚀 Improve programming skills</li>
        <li>🧩 Build real-world applications</li>
        <li>💼 Become a professional developer</li>
    </ul>

    <h3 class="section-title">💡 Interests</h3>
    <ul>
        <li>🌐 Web Development</li>
        <li>🎨 UI/UX Design</li>
        <li>📊 Data Visualization</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.image("Pages/9a982bd3-dbba-4e0a-a286-7f74848efd01.jpg", width=400)

    st.markdown("""
    <div style="text-align: center; margin-left: 15px;">
    <h3>Julius P. Carmen</h3>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <h4>⚡ Quick Info</h4>
        <p><b>Focus:</b> Web Applications</p>
        <p><b>Tech Stack:</b> Python, Streamlit</p>
    </div>
    """, unsafe_allow_html=True)


st.write("---")

