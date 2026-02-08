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
# Step 4: MCQ & AI Explanation Skeleton
if topic_input:

    st.write("📌 AI Revision & MCQs Module")

    # Example: MCQs list
    mcqs = [
        {
            "question": f"What is the main concept of {topic_input}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        },
        {
            "question": f"Important formula in {topic_input}?",
            "options": ["Formula X", "Formula Y", "Formula Z", "Formula W"],
            "answer": "Formula Y"
        }
    ]

    st.subheader("🧪 Practice MCQs")
    score = 0
    for i, mcq in enumerate(mcqs):
        st.write(f"Q{i+1}: {mcq['question']}")
        user_answer = st.radio("Select answer:", mcq["options"], key=f"mcq{i}")
        if user_answer:
            if user_answer == mcq["answer"]:
                st.success("✅ Correct")
                score += 1
            else:
                st.error(f"❌ Wrong. Correct answer: {mcq['answer']}")

    st.info(f"Your Score: {score}/{len(mcqs)}")

    # Placeholder for AI Explanation
    st.subheader("🤖 AI Explanation")
    st.write(f"AI explanation for **{topic_input}** will appear here in future updates.")
# Step 5: AI Explanation + Language Toggle
if topic_input:

    st.subheader("🌐 Language Selection for Explanation")
    language = st.radio("Choose Language:", ["Hindi", "English"], horizontal=True)

    st.subheader("🤖 AI Explanation")
    
    if language == "Hindi":
        explanation = f"यहाँ **{topic_input}** का सरल हिंदी में विवरण दिखेगा।\n- Key points\n- Important formulas\n- Example questions"
    else:
        explanation = f"Here is a simple English explanation for **{topic_input}**:\n- Key points\n- Important formulas\n- Example questions"

    st.write(explanation)
