import streamlit as st

def show_home_page():
    st.markdown("""
           <h1 style='text-align: center;'>Welcome to BeyondATS AI</h1>
           <h3 style='text-align: center;'>Streamline your hiring process with AI-driven insights</h3>
       """, unsafe_allow_html=True)
    st.image("image/logo.jpeg", caption="Image by Freepik", use_column_width=True)
    st.markdown("""
            Traditional Applicant Tracking Systems (ATS) have revolutionized the recruitment process by automating the initial screening of resumes. However, these systems are not without flaws, which can lead to significant challenges in talent acquisition:

            - **Overreliance on Keywords:** Conventional ATS software relies heavily on keyword matching to filter candidates. This approach can favor candidates who tailor their resumes with specific keywords over those with genuine qualifications. As a result, some candidates who may not be as qualified but know how to "game" the system can pass through the ATS filters, while more capable candidates with resumes that do not adhere to specific keyword criteria might be overlooked.

            - **Missing Out on True Talent:** Many highly qualified candidates are often disregarded by traditional screening processes because their resumes are not optimized for ATS algorithms. This misalignment can cause a loss of potential talent simply because their document formatting or diction does not match the expected patterns.

            ### Our Solution
            The Resume Scanner is designed to mitigate these issues by focusing on the content's context and depth rather than just the presence of certain words:

            - **Beyond Keywords:** Our tool significantly reduces reliance on keyword matching, employing advanced algorithms to analyze the context in which terms are used, the relevance of skills to the job description, and the overall narrative of career progression. This method ensures that the evaluation of candidates is based on their true capabilities and experiences rather than on their ability to optimize a resume for keyword searches.

            - **Highlighting True Competence:** By evaluating actual competencies and achievements, our software recognizes the inherent value and potential of candidates. It assesses how their experiences and skills align with the job requirements, ensuring that each candidate's true talent is considered in the decision-making process.

            - **Fair and Inclusive Screening:** By prioritizing substantive evaluation over keyword frequency, the Resume Scanner promotes a more equitable hiring process. It levels the playing field for all candidates, providing an opportunity for truly talented individuals to shine, regardless of their familiarity with ATS optimization techniques.

            This comprehensive approach not only improves the quality of candidate selection but also supports a more diverse and inclusive workforce by ensuring that all applicants are fairly considered based on their actual qualifications and suitability for the role.
            """, unsafe_allow_html=True)
