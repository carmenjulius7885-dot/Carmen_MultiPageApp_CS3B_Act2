import streamlit as st

st.set_page_config(page_title="Skills", page_icon="💡", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #8ABEB9, #B7E5CD);
    font-family: 'Segoe UI', sans-serif;
}

.header {
    background: linear-gradient(135deg, #456882, #234C6A);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.skill-label {
    font-weight: bold;
    margin-top: 10px;
}

.badge {
    display: inline-block;
    background: #e0f2fe;
    padding: 8px 12px;
    border-radius: 10px;
    margin: 5px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>💡 My Skills Dashboard</h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("💻 Programming")

    python = st.slider("Python", 0, 100, 80)
    st.progress(python)

    js = st.slider("JavaScript", 0, 100, 70)
    st.progress(js)

    php = st.slider("PHP", 0, 100, 75)
    st.progress(php)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("🎨 Design")

    design = st.slider("UI/UX Design", 0, 100, 85)
    st.progress(design)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🛠 Tools")
    st.markdown("""
    <div>
        <span class="badge">💻 GitHub</span>
        <span class="badge">🧑‍💻 VS Code</span>
        <span class="badge">⚡ Streamlit</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
