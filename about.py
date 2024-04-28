import streamlit as st


def show_about_page():

    st.markdown("""
                   <h1 style='text-align: center;'>About BeyondATS AI</h1>
                   <h3 style='text-align: center;'>What Does the Resume Scanner Do?</h3>
               """, unsafe_allow_html=True)


    st.write("""
    The Resume Scanner is an advanced tool designed to transform the recruitment process by offering a more nuanced analysis of candidate resumes compared to traditional approaches. Here’s how it stands out:

    - **Contextual Analysis:** Uses AI to understand the substance of a resume relative to the job description, focusing on relevance and context.
    - **Compatibility Scoring:** Calculates how well a candidate's experience and skills match the job requirements, providing a score from 0 to 10.
    - **Insightful Feedback:** Offers detailed explanations for each score, highlighting strengths and areas for improvement.
       """)

    with st.expander("Case Study: The Impact of Inaccurate Resumes on Hiring Processes", expanded=False):
        st.write("""
        ## Case Study: The Impact of Inaccurate Resumes on Hiring Processes

        As part of a social experiment, a social media influencer submitted a resume containing false information about their work experience. The resume listed positions at renowned companies such as Google, Instagram, and Amazon, alongside peculiar job responsibilities:

        - "Enhanced a 300% increase in average coffee break time of team, by nonstop crying in the main office room."
        - "Verified sending threats to 16 competitors, decreasing the competitive landscape by 18%."
        - "Helped utilize Google's computing resources to mine $15M of Ethereum before getting caught & returning it."

        These are only a few of the odd job responsibilities listed. Additionally, the candidate claimed to have worked on the non-existent "Amazon Dating" team. Despite the incredulous claims, the resume garnered interviews from reputable companies including Databricks, MongoDB, Reddit, Lucid, Cloudflare, and Robinhood.
        """)
        st.image("image/Interviews.png", caption="Companies that reached out with interview opportunities highlighted in green", use_column_width=True)
        st.write("""
        This incident underscores the challenges faced by companies in vetting candidates amidst the sheer volume of applications received. 

        Automated applicant tracking systems (ATS) and time-pressed hiring managers often overlook inconsistencies or inaccuracies in resumes, leading to the inadvertent consideration of unqualified candidates.

        To address this issue, companies are increasingly turning to AI-driven solutions to enhance their hiring processes. By utilizing machine learning algorithms, organizations can efficiently screen resumes for both qualifications and integrity, mitigating the risk of hiring based on false information.

        This case highlights the importance of thorough resume vetting and the potential for AI to streamline recruitment practices, ensuring that deserving candidates receive fair consideration while maintaining the integrity of the hiring process.

        More Information:

        [LinkedIn](https://www.linkedin.com/posts/jehakjerrylee_kismma-d-nhuhts-series-activity-7184308527132241921-76m5/)

        [Twitter](https://twitter.com/JerryJHLee/status/1778484920593055763)

        [Reddit](https://www.reddit.com/r/jobs/comments/1c1zw83/i_applied_to_100_jobs_using_a_resume_with_the/)
        """)

    with st.expander("How Does It Work?", expanded=False):
        st.markdown("""
        ## How Does It Work?
        Powered by the Google Gemini 1.5 Pro AI, the Resume Scanner leverages cutting-edge technology to provide a comprehensive evaluation of resumes. Here’s a detailed breakdown of its capabilities and the processes involved:

        - **Advanced AI Capabilities:**
            - **Next-Generation AI Technology:** Building on the successes of its predecessor, Gemini 1.5 Pro introduces new functionalities that expand its application across a broader range of tasks.
            - **Enhanced Efficiency with MoE Architecture:** Utilizes a Mixture-of-Experts architecture to improve training efficiency. This allows the model to dynamically allocate processing power where it's most needed, enhancing performance across varied tasks.
            - **Superior Performance:** Gemini 1.5 Pro significantly outperforms earlier models in understanding and generating text, images, and code, showcasing remarkable in-context learning capabilities.
            - **Safety and Ethics Commitment:** Rigorous testing ensures the model adheres to high standards of AI ethics, focusing on safety, fairness, and minimizing biases.
    
        - **Deep Content Analysis:**
            - **Beyond Keywords:** While traditional ATS systems rely heavily on keyword matching, our AI delves deeper by analyzing the context in which these keywords appear, the relevance of the described experiences to the job requirements, and the progression and consistency of the career path presented in the resume.
            - **Comprehensive Fit Assessment:** The AI examines both the resume and the job description to assess a candidate's fit. It considers multiple factors such as the relevance of professional experiences, alignment of educational background with job requirements, and suitability of demonstrated skills for the role. This comprehensive approach ensures a nuanced evaluation, identifying candidates who are truly a good match for the position.

        - **Interactive Feedback System:**
            - **Real-Time Adjustments:** The Resume Scanner also offers an interactive feedback system where recruiters can adjust the importance of certain skills or experiences on the fly. This real-time adjustment allows for even more tailored analysis that aligns with dynamic business needs or specific project requirements.
            - **Actionable Insights:** By providing detailed insights into the strengths and potential gaps in a candidate's resume, the tool empowers recruiters to make informed decisions quickly and effectively.

        These advanced features ensure that the Resume Scanner is not just a tool for filtering candidates but a comprehensive system for understanding their potential and aligning them with the right opportunities based on an in-depth analysis of their professional profiles.
        """, unsafe_allow_html=True)

    with st.expander("Our Solution", expanded=False):
        st.markdown("""
        ### Our Solution
        The Resume Scanner tackles critical recruitment challenges by integrating several innovative features that collectively enhance both the efficiency and fairness of the hiring process:

        - **Flexible Input Options:**
            - **Custom Job Descriptions:** Allows recruiters to input a specific job description that reflects the unique requirements and priorities of the role, ensuring that the analysis is tailored and relevant.
            - **Pre-Curated Templates:** Offers a selection of pre-curated job descriptions for common roles, which can be customized or used as is, providing a quick start option that saves time and effort.
            - **Resume Flexibility:** Users can upload resumes in various formats (e.g., PDF, DOCX), making the tool accessible and convenient for all users, regardless of how their professional information is formatted.

        - **Contextual Understanding:**
            - **Advanced Semantic Analysis:** Uses cutting-edge AI to perform deep semantic analysis, ensuring that the understanding of the resume content goes beyond keywords to grasp the nuances of candidate experiences.
            - **Role-Specific Insights:** Tailors its analysis to the specifics of the job role, considering industry-specific competencies and skills that are crucial for accurate candidate assessment.
            - **Cultural Fit Evaluation:** Additionally analyzes soft skills and personal attributes to assess potential cultural fit, which is as important as professional qualifications in many organizational contexts.

        - **Enhanced Evaluation Metrics:**
            - **Compatibility Scoring:** Each candidate is scored on a scale from 0 to 10 based on their resume's alignment with the job description, where higher scores reflect a more suitable candidate.
            - **Detailed Feedback:** Provides detailed explanations for the compatibility score, offering insights into strengths and areas for improvement that help recruiters make more informed decisions.
            - **Dynamic Scoring System:** The scoring system adapts based on feedback from recruiters, learning from each interaction to improve its accuracy over time.

        ### Impact of Our Solution
        By adopting this AI-driven approach, companies can ensure a more equitable and effective recruitment process. This technology:

        - **Reduces Biases:** Minimizes unconscious biases by focusing on factual content and context rather than subjective interpretations of resume data.
        - **Aligns Candidates with Opportunities:** Helps align the right candidates with the right opportunities based on genuine qualifications and potential, rather than merely who best formatted their resume for keyword searches.
        - **Streamlines Hiring:** Significantly cuts down the time spent screening resumes manually, allowing recruiters to focus on engaging with potential hires and enriching the candidate experience.

        These features collectively make the Resume Scanner a transformative tool in the recruitment landscape, setting new standards for how companies discover and evaluate talent.
        """, unsafe_allow_html=True)

    with st.expander("What does the Resume Scanner look for?", expanded=False):
        st.markdown("""
        ### Detailed Analysis Criteria
        When analyzing a resume in comparison to a job description, the Resume Scanner uses the following criteria to assess a candidate's suitability for the role:

        - **Contextual Relevance**: The tool scrutinizes specific skills and experiences mentioned in the resume, assessing how these align with the needs described in the job description. It focuses on genuine expertise and relevance, going beyond mere keyword matching.

        - **Quantifiable Achievements**: It highlights significant achievements that can be quantified, evaluating how these accomplishments have prepared the candidate for the responsibilities of the role.

        - **Career Progression and Relevance**: The analysis considers the candidate’s career trajectory to determine their growth and suitability for the advertised position.

        - **Handling of Ambiguities or Unclear Information**: Any ambiguous or insufficiently detailed information in the resume is cautiously interpreted or flagged for manual review.

        - **Feedback for Improvement**: The tool provides constructive feedback, suggesting how candidates might improve their presentation or acquire additional skills to better align with the job requirements.

        The final output includes a compatibility score from 0 to 10, where 0 indicates minimal qualification and 10 indicates a perfect match, complete with detailed reasoning for the score.
        """)



if __name__ == "__main__":
    show_about_page()
