import streamlit as st
import pandas as pd
from db import engine

def render_dashboard():

    if st.button("🏠 Home"):
        st.session_state.page = "home"
        st.rerun()

    st.title("QA Dashboard")
    df = pd.read_sql("SELECT * FROM responses", con=engine)

    if df.empty:
        st.info("No responses yet.")
    else:
        st.dataframe(df)

    # --- Filters ---
    with st.expander("🔍 Filter Responses", expanded=True):
        departments = df["department"].dropna().unique().tolist()
        qa_types = df["qa_type"].dropna().unique().tolist()
        meetings = df["meeting"].dropna().unique().tolist()

        selected_dept = st.selectbox("Department", ["All"] + sorted(departments))
        selected_qa = st.selectbox("QA Type", ["All"] + sorted(qa_types))
        selected_meeting = st.selectbox("Meeting", ["All"] + sorted(meetings))

        if selected_dept != "All":
            df = df[df["department"] == selected_dept]
        if selected_qa != "All":
            df = df[df["qa_type"] == selected_qa]
        if selected_meeting != "All":
            df = df[df["meeting"] == selected_meeting]

    # --- Metrics ---
    st.subheader("📈 Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Responses", len(df))
    col2.metric("Departments", df["department"].nunique())
    col3.metric("Meetings", df["meeting"].nunique())

    # --- Display data ---
    st.subheader("📄 Responses")
    st.dataframe(df)

    # Optional: show top priorities mentioned
    st.subheader("🗂 Common Priorities (by text frequency)")
    priority_responses = df[df["question"] == "What is your first priority?"]["response"].dropna()
    top_words = (
        priority_responses.str.lower()
        .str.split()
        .explode()
        .value_counts()
        .head(10)
    )
    st.bar_chart(top_words)