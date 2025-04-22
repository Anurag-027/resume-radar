import streamlit as st
from helper import extract_text_from_pdf, call_gemini, generate_resume_skills_prompt, generate_match_prompt

# 💼 Application Branding
st.set_page_config(page_title="Resume Radar", page_icon="logo.png")

# st.image("logo.png", width=120)  # Make sure logo.png is in the same folder
st.title("📄 Resume Radar")
st.caption("Your smart resume-to-job matching assistant — powered by GenAI ✨")

# 📤 Upload & Input
resume_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])
job_desc = st.text_area("📝 Paste the Job Description")

# 🧠 Analyze Button
if st.button("🔍 Analyze"):
    if resume_file and job_desc:
        with st.spinner("📃 Extracting resume..."):
            resume_text = extract_text_from_pdf(resume_file)

        with st.spinner("🛠 Extracting skills from resume..."):
            skills_prompt = generate_resume_skills_prompt(resume_text)
            resume_skills = call_gemini(skills_prompt)

        st.subheader("🔧 Extracted Skills")
        st.text(resume_skills)

        with st.spinner("📊 Matching with Job Description..."):
            match_prompt = generate_match_prompt(resume_skills, job_desc)
            match_output = call_gemini(match_prompt)

        st.subheader("📈 Match Report")
        st.markdown(match_output)
    else:
        st.warning("⚠️ Please upload both your resume and the job description.")
