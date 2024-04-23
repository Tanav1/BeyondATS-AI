import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import os

secret_key = os.environ.get(NEW_API_KEY)


# Configure your model
def setup_model():
    genai.configure(api_key=secret_key)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    system_instruction = """
    Prompt: Given the job title, detailed job description, and a candidate's uploaded resume provided on the website, 
    perform a comprehensive analysis to assess the candidate's suitability for the role. The output should include a compatibility 
    score from 0 to 10, detailed explanations for the score, and additional metrics that provide deeper insights into various 
    aspects of the candidate’s profile. Ensure that each metric containing scores includes reasoning, and provide 2 to 3 examples 
    per section from the resume where applicable. The data will be fed like this [f"Role/Job Title: {job_title} Responsibilities:{job_description} Additional Notes:{additional_notes}", resume_text].
    Ensure that all of this data is taken into account in analysis. Also for clarification, Additional Notes contains additional information
    from the hiring manager that should be taken into account while running analysis. An example would be candidate must have a bachelors degree.
    Also, do not assume any pronouns from the resume. 

    ### Output Format:
    - Compatibility Score: Numeric score from 0-10 indicating overall suitability.
    - Basic Information: Extract candidate details such as name, contact info, LinkedIn, location, and email.
    - Education: Detail educational background including institutions, years attended, and GPA (if available).
    - Advanced Metrics for Holistic Assessment: Assess skill proficiency levels, cultural fit, innovation index, leadership potential, 
      adaptability score, technology adaptation rate, communication effectiveness, project impact score, client engagement score, 
      risk management index, learning agility index, and digital literacy score. These should have scores from 0-10 as well as justification.
    - Detailed Evaluation Report: Include sections on strengths, relevant experiences, quantifiable achievements, areas for improvement,
      feedback for candidate, questions for interview, red flag analysis, achievement impact, and an overall summary with hiring recommendation.

    Ensure all sections are clearly defined and consistently presented, allowing for straightforward parsing and display in the web interface,
    ensuring that hiring managers receive all necessary insights to make informed decisions.
    """

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  system_instruction=system_instruction,
                                  safety_settings=safety_settings)
    return model


model = setup_model()


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''  # Concatenate text from each page
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])

def show_resume_page():
    st.title("Resume Scanner")
    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    job_description = st.text_area("Roles/Responsibilities/Description", height=250)
    additional_notes = st.text_area("Any Additional Notes about role, company, or candidate")

    # User selects input method
    input_method = st.radio("Choose your input method:", ("Upload Candidate Resume", "Paste Candidate Resume"))
    resume_text = ""
    if input_method == "Upload Candidate Resume":
        resume = st.file_uploader("Upload Candidate Resume", type=['pdf', 'docx', 'txt'])
        if resume:
            file_type = resume.type
            try:
                if file_type == "application/pdf":
                    resume_text = extract_text_from_pdf(resume)
                    st.subheader("Extracted Text from PDF:")
                elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    resume_text = extract_text_from_docx(resume)
                    st.subheader("Extracted Text from DOCX:")
                elif file_type == "text/plain":
                    resume_text = str(resume.read(), "utf-8")  # Decode for txt file
                    st.subheader("Extracted Text from TXT:")
                else:
                    st.error("Unsupported file type.")
            except Exception as e:
                st.error(f"Failed to read the file: {str(e)}")
    else:
        resume_text = st.text_area("Paste candidate resume text here:")

    if st.button("Analyze Resume") and resume_text:
        with st.spinner('Analyzing resume... Please wait.'):
            st.write('Once finished analyzing, go to View Results on Navigation Bar')
            # Assume model.generate_content takes a string of resume text
            prompt_parts = f"Role/Job Title: {job_title} Responsibilities: {job_description} Company Name: {company_name} Additional Notes: {additional_notes} Resume Text: {resume_text}"
            response = model.generate_content(prompt_parts)

        if response:
            st.success('Analysis complete! You can now view the results.')
            st.session_state['analysis_result'] = response
            st.session_state['analysis_done'] = True  # Set this to control result page visibility
            st.session_state['page'] = 'View Results'  # Ensure this exactly matches the page name
            st.experimental_rerun()
        else:
            st.error('Failed to analyze the resume. Please try again.')


# response = model.generate_content(
#     model="gemini-pro-vision",
#     content=[prompt, cookie_picture]
# )
