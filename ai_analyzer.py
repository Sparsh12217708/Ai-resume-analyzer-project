import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def analyze_resume(resume_text, job_description):
    """
    Sends the resume and job description to the Gemini API and gets the analysis.
    """
    if not api_key or api_key == "your_api_key_here":
        return "Error: Please set your Google Gemini API key in the .env file."

    prompt = f"""
    Act as a skilled and highly experienced ATS (Applicant Tracking System) with a deep understanding of tech roles, software engineering, data science, and general corporate hiring.
    
    Your task is to evaluate the following resume against the provided job description.
    
    Job Description:
    {job_description}
    
    Resume:
    {resume_text}
    
    Please provide a detailed evaluation structured exactly as follows:
    
    ### Match Percentage
    [Provide a percentage indicating how well the resume matches the job description, e.g., 85%]
    
    ### Profile Summary
    [Provide a brief 2-3 sentence summary of the candidate's profile in relation to the job]
    
    ### Missing Keywords
    [List the crucial keywords, skills, or experiences from the job description that are missing from the resume. Bullet points.]
    
    ### Recommendations
    [Provide 3-5 specific, actionable recommendations on how the candidate can improve their resume to better match this job description. Bullet points.]
    """

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"An error occurred while communicating with the AI API: {str(e)}"
