import streamlit as st
from home import show_home_page
from resume import show_resume_page
from about import show_about_page
from results import show_results_page

def main():
    st.sidebar.title("Navigation")
    # Initialize session state for analysis completion if it doesn't already exist
    if 'analysis_done' not in st.session_state:
        st.session_state['analysis_done'] = False

    # Define the pages that are always available
    pages = ["Home", "About", "Resume Scanner"]

    # Only add "View Results" to the navigation if the analysis has been done
    if st.session_state['analysis_done']:
        pages.append("View Results")

    # Radio button for page navigation
    choice = st.sidebar.radio("Go to", pages)

    # Navigation logic
    if choice == "Home":
        show_home_page()
    elif choice == "About":
        show_about_page()
    elif choice == "Resume Scanner":
        show_resume_page()
    elif choice == "View Results":  
        show_results_page()

if __name__ == "__main__":
    main()
