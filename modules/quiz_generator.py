import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


def generate_quiz(text, topic, difficulty, num_questions):

    if topic.strip() != "":

        prompt = f"""
Generate {num_questions} {difficulty} multiple-choice questions ONLY from the topic "{topic}".

For each question provide:
- question
- four options A, B, C, D
- correct answer
- explanation

Return ONLY a JSON array.

Format:

[
{{
"question":"...",
"options": {{
"A":"...",
"B":"...",
"C":"...",
"D":"..."
}},
"answer":"A",
"explanation":"..."
}}
]

Content:
{text[:5000]}
"""

    else:

        prompt = f"""
Generate {num_questions} {difficulty} multiple-choice questions from the content below.

For each question provide:
- question
- four options A, B, C, D
- correct answer
- explanation

Return ONLY a JSON array.

Format:

[
{{
"question":"...",
"options": {{
"A":"...",
"B":"...",
"C":"...",
"D":"..."
}},
"answer":"A",
"explanation":"..."
}}
]

Content:
{text[:5000]}
"""

    try:

        response = llm.invoke(prompt)

        response_text = response.content.strip()

        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

        questions = json.loads(response_text)

        return questions

    except Exception as e:

        print("ERROR:", e)

        return []