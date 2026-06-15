import streamlit as st
from modules.pdf_loader import extract_text
from modules.quiz_generator import generate_quiz

st.set_page_config(
    page_title="QuizoraAI",
    page_icon="📚",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align:center;
    color:#4CAF50;
}

div.stButton > button {
    width:100%;
    border-radius:15px;
    height:3em;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("📚 QuizoraAI")

# ---------- SIDEBAR ----------
with st.sidebar:

    st.header("⚙️ Quiz Settings")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    num_questions = st.slider(
        "Number of Questions",
        5,
        20,
        10
    )

    generate = st.button("🚀 Generate Quiz")

# ---------- GENERATE QUIZ ----------
if generate:

    if uploaded_file is None:
        st.error("Please upload a PDF.")
    else:

        progress_bar = st.progress(0)
        status = st.empty()

        status.text("📄 Reading PDF...")
        progress_bar.progress(20)

        text = extract_text(uploaded_file)

        status.text("🧠 AI is analyzing content...")
        progress_bar.progress(50)

        questions = generate_quiz(
            text,
            difficulty,
            num_questions
        )

        status.text("✍️ Creating questions...")
        progress_bar.progress(80)

        st.session_state["questions"] = questions

        status.text("🎉 Quiz Ready!")
        progress_bar.progress(100)

# ---------- QUIZ ----------
if "questions" in st.session_state:

    questions = st.session_state["questions"]

    st.header("📝 Quiz")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Questions",
            len(questions)
        )

    with col2:
        st.metric(
            "Difficulty",
            difficulty
        )

    answers = []

    for i, q in enumerate(questions):

        with st.container(border=True):

            st.subheader(f"Q{i+1}")

            st.write(q["question"])

            choice = st.radio(
                "Choose an option",
                list(q["options"].keys()),
                format_func=lambda x:
                f"{x}. {q['options'][x]}",
                key=i
            )

            answers.append(choice)

    submit = st.button("✅ Submit Quiz")

    if submit:

        score = 0

        st.header("📊 Results")

        for i, (user_ans, q) in enumerate(
                zip(answers, questions)):

            if user_ans == q["answer"]:

                score += 1

                st.success(
                    f"Q{i+1}: Correct ✅"
                )

            else:

                st.error(
                    f"Q{i+1}: Incorrect ❌"
                )

            st.write(
                f"Correct Answer: {q['answer']}. "
                f"{q['options'][q['answer']]}"
            )

            st.info(
                f"Explanation: {q['explanation']}"
            )

        st.header(
            f"🎯 Final Score: {score}/{len(questions)}"
        )

        percentage = score * 100 / len(questions)

        st.progress(int(percentage))

        st.metric(
            "Accuracy",
            f"{percentage:.1f}%"
        )