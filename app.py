import streamlit as st

st.set_page_config(page_title="AI Tutor", page_icon="📘")

st.title("📘 AI Tutor")
st.subheader("NEET Smart Revision App")

st.write("Welcome 👋")
st.write("Pehle apni class select karo:")

# Class selection
selected_class = st.selectbox(
    "Select your class",
    ["Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
)

if selected_class:
    st.success(f"✅ You selected {selected_class}")

st.info("Next step: Subject & MCQs add karenge 🚀")
