import streamlit as st
import pandas as pd
from db import engine
from form_questions import form_questions

def render_qa_form():

    if st.button("🏠 Home"):
        st.session_state.page = "home"
        st.rerun()
    st.title("QA Form")

    qa_type = st.sidebar.selectbox("Select Category", ["Line Management", "QA", "Department Meetings"])

    timeline_options = {
        "Line Management": ["Literacy Review", "High Participation Focus", "Coaching Session"],
        "QA": ["Middle Attainer Learning Walk", "Work Scrutiny", "Student Panel"],
        "Department Meetings": ["Developing Departments", "Department Meeting"]
    }

    meeting = st.sidebar.selectbox("Select Meeting", timeline_options[qa_type])

    questions = form_questions.get((qa_type, meeting), ["No questions defined for this form."])

    with st.form(key="qa_form"):
        responses = [st.text_area(q) for q in questions]
        department = st.text_input("Department Name")
        submit = st.form_submit_button("Submit")

        if submit:
            for i, q in enumerate(questions):
                row = {
                    "qa_type": qa_type,
                    "meeting": meeting,
                    "department": department,
                    "question": q,
                    "response": responses[i]
                }
                df = pd.DataFrame([row])
                df.to_sql("responses", engine, if_exists="append", index=False)

            st.success("Your response has been recorded in the database.")
