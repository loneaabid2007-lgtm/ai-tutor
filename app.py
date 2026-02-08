

# ---- Step 0: Page Config ----
st.set_page_config(page_title="AI Tutor", page_icon="📘")

# ---- Step 1: NEET Topics Template ----
neet_topics = {
    "Class 11": {
        "Physics": ["Mechanics", "Thermodynamics", "Electrostatics", "Optics", "Gravitation"],
        "Chemistry": ["Atomic Structure", "Chemical Bonding", "Thermodynamics", "Solutions", "Equilibrium"],
        "Biology": ["Cell Biology", "Genetics", "Human Physiology", "Plant Physiology", "Evolution"]
    },  # <-- Comma fixed here
    "Class 12": {
        "Physics": ["Electromagnetism", "Modern Physics", "Optics", "Current Electricity", "Semiconductors"],
        "Chemistry": ["Solid State", "Electrochemistry", "Organic Chemistry", "Coordination Compounds", "Biomolecules"],
        "Biology": ["Reproduction", "Genetics & Evolution", "Human Health", "Biotechnology", "Ecology"]
    }
}

# ---- Step 2: MCQ Template ----
mcq_bank = {
    "Mechanics": [
        {"question": "Newton's First Law is also called?",
         "options": ["Law of Inertia", "Law of Motion", "Law of Gravity", "Law of Work"],
         "answer": "Law of Inertia"},
        {"question": "Unit of Force?",
         "options": ["Newton", "Joule", "Pascal", "Watt"],
         "answer": "Newton"}
    ],
    "Cell Biology": [
        {"question": "The basic unit of life is?",
         "options": ["Cell", "Atom", "Molecule", "Organ"],
         "answer": "Cell"},
        {"question": "Site of energy production in cell?",
         "options": ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"],
         "answer": "Mitochondria"}
    ]
}

# ---- Step 3: Streamlit App ----
st.title("📘 AI Tutor")
st.subheader("NEET Smart Revision App")

st.write("Welcome 👋")
st.write("Pehle apni class select karo:")

# Class Selection
selected_class = st.selectbox(
    "Select your class",
    ["Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
)

if selected_class:
    st.success(f"✅ You selected {selected_class}")

    # Subject Selection
    st.write("Ab apna subject select karo:")
    if selected_class in ["Class 11", "Class 12"]:
        subjects = list(neet_topics[selected_class].keys())
    else:
        subjects = ["Science", "Math"]

    selected_subject = st.selectbox("Choose subject:", subjects)

    if selected_subject:
        st.success(f"✅ You selected {selected_subject}")

        # Topic Input
        topic_input = st.text_input(f"Type the topic/chapter for {selected_subject}:")

        if topic_input:
            st.info(f"🔹 You entered topic: {topic_input}")

            # MCQ Module
            st.subheader("🧪 Practice MCQs")
            mcqs = mcq_bank.get(topic_input, [
                {"question": f"What is {topic_input}?", 
                 "options": ["Option A", "Option B", "Option C", "Option D"], 
                 "answer": "Option A"}
            ])

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

            # AI Explanation + Language Toggle
            st.subheader("🌐 AI Explanation")
            language = st.radio("Choose Language:", ["Hindi", "English"], horizontal=True)

            if language == "Hindi":
                explanation = f"यहाँ **{topic_input}** का सरल हिंदी में विवरण दिखेगा।\n- Key points\n- Important formulas\n- Example questions"
            else:
                explanation = f"Here is a simple English explanation for **{topic_input}**:\n- Key points\n- Important formulas\n- Example questions"

            st.write(explanation)
