import streamlit as st

def show_results_page():
    st.title("Analysis Results")
    if 'analysis_result' in st.session_state:
        result = st.session_state['analysis_result']
        st.write(result.text)
    else:
        st.warning("No results to display. Please analyze a resume first.")