import streamlit as st
import pdfplumber
import docx2txt
import os
import tempfile

def extract_text(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file.name.endswith('.docx'):
        temp_file_path = os.path.join(tempfile.gettempdir(), file.name)
        with open(temp_file_path, "wb") as f:
            f.write(file.read())
        return docx2txt.process(temp_file_path)
    elif file.name.endswith('.txt'):
        return file.read().decode("utf-8")
    else:
        return "Unsupported file format."

st.set_page_config(page_title="Resume & Job Description Comparison Tool", layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("Resume & JD Comparison Tool")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.subheader("Upload Resume")
    resume_file = st.file_uploader("Upload your resume (.pdf, .docx, .txt)", type=['pdf', 'docx', 'txt'], key="resume")


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.subheader("Upload Job Description")
    jd_file = st.file_uploader("Upload job description (.pdf, .docx, .txt)", type=['pdf', 'docx', 'txt'], key="jd")


if resume_file and jd_file:
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)


    st.subheader("Parsed Content")
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Resume Text", resume_text, height=400)
    with col2:
        st.text_area("Job Description Text", jd_text, height=400)


    st.subheader("Matching Keywords")
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    common_words = resume_words.intersection(jd_words)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"**Common Keywords Found:** {len(common_words)}")
        st.write(", ".join(sorted(list(common_words))[:50]))  # top 50
