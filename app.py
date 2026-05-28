import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_docx
from ai_analyzer import analyze_resume

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3a8a;
    }
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1e40af;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("📄 AI-Powered Resume Analyzer")
st.markdown("Upload your resume and the job description to see how well you match the role!")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Job Description")
    job_description = st.text_area("Paste the Job Description here:", height=300, placeholder="e.g. We are looking for a Software Engineer with Python and React experience...")

with col2:
    st.subheader("2. Upload Resume")
    uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
    
    resume_text = ""
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        if file_extension == 'pdf':
            resume_text = extract_text_from_pdf(uploaded_file)
        elif file_extension == 'docx':
            resume_text = extract_text_from_docx(uploaded_file)
        
        if resume_text:
            st.success("Resume uploaded and text extracted successfully!")
        else:
            st.error("Failed to extract text from the file.")

# Analysis Button
st.markdown("---")
col_button, col_empty = st.columns([1, 4])
with col_button:
    analyze_button = st.button("🚀 Analyze Resume")

# Results Section
if analyze_button:
    if not job_description.strip():
        st.warning("Please paste a job description.")
    elif not uploaded_file:
        st.warning("Please upload a resume.")
    elif not resume_text:
        st.error("Could not read the resume. Please try another file.")
    else:
        with st.spinner("AI is analyzing your resume... Please wait."):
            analysis_result = analyze_resume(resume_text, job_description)
            
            st.subheader("📊 Analysis Results")
            st.markdown(analysis_result)
