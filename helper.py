import os
import requests
from dotenv import load_dotenv
import pdfplumber

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}" 


def call_gemini(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    


def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    
def generate_resume_skills_prompt(resume_text):
    return f"""
Extract the technical and soft skills from this resume:

{resume_text}

Return only a clean list in bullet points.
"""

def generate_match_prompt(resume_skills, job_desc):
    return f"""
Given these resume skills:

{resume_skills}

And this job description:

{job_desc}

Give:
1. Skill match percentage
2. Missing skills
3. Suggestions for improvement

Output must be clear and structured.
"""
    