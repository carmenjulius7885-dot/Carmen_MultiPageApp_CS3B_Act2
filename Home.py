import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Home App",
    page_icon="🏠",
    layout="wide"
)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About","Project","Skills", "Contact"])

if page == "Home":
    st.title("🏠 Welcome to My Streamlit App")
    st.subheader("Your simple homepage layout")

    st.write("""
    This is your home page. You can customize this with:
    - Charts 📊
    - Data tables 📋
    - Images 🖼️
    - Interactive widgets 🎛️
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("📌 Feature 1")

    with col2:
        st.success("🚀 Feature 2")

    with col3:
        st.warning("⚡ Feature 3")

    with col4:
        st.warning("⚡ Feature 4")
        
elif page == "About Me":
    st.title("ℹ️ About Me")
    st.write("This app is built using Streamlit.")

elif page == "Project":
    st.title("ℹ️ Project")
    st.write("This app is built using Streamlit.")

elif page == "Skills":
    st.title("ℹ️ Skills")
    st.write("This app is built using Streamlit.")

elif page == "Contact":
    st.title("📞 Contact")
    st.write("Email: your@email.com")
