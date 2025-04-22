# 📡 Resume Radar

Resume Radar is a GenAI-powered resume analyzer and job matcher application built using **Google Gemini API** and **Streamlit**.  
It helps job seekers by extracting skills from uploaded resumes and comparing them to any job description, offering match percentages, missing skills, and improvement suggestions.

![Screenshot](./logo.png)

---

## 🚀 Features

- 🧾 Upload a PDF resume and extract technical + soft skills
- 📝 Paste any job description for comparison
- 📊 Get AI-generated match report with improvement tips
- ⚡ Powered by Gemini Pro (Google Generative AI API)
- 🖼️ Clean, user-friendly Streamlit interface
- ✅ 100% free to use with your own API key

---

## 🧠 Tech Stack

- 🧠 [Google Gemini API](https://makersuite.google.com/)
- 🐍 Python 3.10+
- 🧾 pdfplumber
- 🌐 Streamlit
- 📦 dotenv, requests

---

## 🛠️ Setup Instructions

1. **Clone the repo**
git clone https://github.com/Anurag-027/resume-radar.git
cd resume-radar

2. **Create a virtual environment**
python3 -m venv venv
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Add your .env file**
GEMINI_API_KEY=your_api_key_here

5. **Run the app**
streamlit run app.py

💡 How It Works
Step | Task
1️⃣ | Extract text from uploaded PDF resume
2️⃣ | Send a prompt to Gemini Pro to extract skills
3️⃣ | Use a second prompt to compare skills with a pasted job description
4️⃣ | Display structured output in a clean dashboard

🌍 Live Demo
📡 Deployed here: https://resume-radar.streamlit.app

🙌 Acknowledgements
Gemini API
Streamlit
pdfplumber

✨ Author
Made with 💙 by Anurag Varshney .

