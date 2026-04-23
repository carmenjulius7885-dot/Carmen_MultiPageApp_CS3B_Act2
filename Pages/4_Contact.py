import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📞", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #8ABEB9, #B7E5CD);
    font-family: 'Segoe UI', sans-serif;
}

.card {
    background: #456882;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

div.stButton > button {
    background: #4CAF50;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: #388E3C;
    transform: scale(1.05);
    transition: 0.2s;
}

.social {
    background: rgba(255,255,255,0.7);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>📞 Contact Me</h1>", unsafe_allow_html=True)

st.write("---")

if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "message" not in st.session_state:
    st.session_state.message = ""

col1, col2 = st.columns([2, 1])

with col1:

    st.subheader("📩 Send a Message")

    st.session_state.name = st.text_input("👤 Name", value=st.session_state.name)
    st.session_state.email = st.text_input("📧 Email", value=st.session_state.email)
    st.session_state.message = st.text_area("💬 Message", value=st.session_state.message)

    colA, colB = st.columns(2)

    with colA:
        if st.button("Send Message"):
            if st.session_state.name and st.session_state.email and st.session_state.message:
                st.success(f"Thanks {st.session_state.name}! Your message has been sent ✅")
            else:
                st.error("Please complete all fields.")

    with colB:
        if st.button("🧹 Clear Form"):
            st.session_state.name = ""
            st.session_state.email = ""
            st.session_state.message = ""
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="social">
        <h3>🌐 Connect With Me</h3>
        <p>💻 GitHub</p>
        <p>📘 Facebook</p>
        <p>📧 Email</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")