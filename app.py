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
# Step 2: Subject selection
if selected_class:
    st.write("Ab apna subject select karo:")
    selected_subject = st.selectbox(
        "Select your subject",
        ["Physics", "Chemistry", "Biology", "Mathematics"]
    )

    if selected_subject:
        st.success(f"✅ You selected {selected_subject}")

        # Step 3: Topic input
        topic_input = st.text_input(f"Type the topic/chapter for {selected_subject}:")
        if topic_input:
            st.info(f"🔹 You entered topic: {topic_input}")
            st.write("Ab aapka AI revision aur MCQ module yaha se connect hoga 🔜")
