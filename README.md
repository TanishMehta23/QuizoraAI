# 📚 QuizoraAI

> Transform PDFs into Interactive Learning with AI

QuizoraAI is an AI-powered learning platform that converts PDF documents into interactive quizzes using **Google Gemini AI**, **Python**, and **Streamlit**. Upload your notes, select difficulty, and instantly generate MCQs with explanations.

---

## 📷 Screenshots

### 🏠 Home Page

![Home](assets/home.png)

---

## 🚀 Features

* 📄 Upload PDF documents
* 🧠 AI-powered quiz generation
* 🎯 Difficulty levels (Easy, Medium, Hard)
* 🔢 Custom number of questions
* 📝 Interactive quiz interface
* ✅ Instant score calculation
* 📖 Detailed explanations for answers
* 📊 Accuracy metrics and progress bar
* 🎨 Modern Streamlit UI
* ⚡ Powered by Google Gemini AI

---

## 📷 Preview

### Home Page

* Upload PDF
* Choose difficulty
* Select number of questions
* Generate quiz

### Quiz Interface

* Multiple-choice questions
* Interactive options
* Submit answers

### Results

* Final score
* Accuracy percentage
* Correct answers
* Explanations

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini

### Libraries

* streamlit
* langchain-google-genai
* pypdf
* python-dotenv

---

## 📂 Project Structure

```text
QuizoraAI/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── modules/
│   ├── pdf_loader.py
│   └── quiz_generator.py
│
└── assets/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/QuizoraAI.git
cd QuizoraAI
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---


## 💡 Example Workflow

```text
PDF
 ↓
Text Extraction
 ↓
Gemini AI
 ↓
MCQ Generation
 ↓
Interactive Quiz
 ↓
Score & Explanations
```

---

## 📌 Tech Used

* Python
* Streamlit
* Google Gemini AI
* PyPDF
* LangChain

---


## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# QuizoraAI

### Transform PDFs into Interactive Learning 🚀