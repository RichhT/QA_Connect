import streamlit as st
from qa_form import render_qa_form
from dashboard import render_dashboard

# Initialize the page selection state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Routing logic
if st.session_state.page == "home":
    st.title("Welcome to the QA Platform")

    st.write("Choose where you’d like to go:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 Fill Out QA Form"):
            st.session_state.page = "form"
            st.rerun()
    with col2:
        if st.button("📊 View Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

elif st.session_state.page == "form":
    render_qa_form()

elif st.session_state.page == "dashboard":
    render_dashboard()
