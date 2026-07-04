import streamlit as st
import sqlite3
import pandas as pd

st.title(" Loan Workflow")

conn = sqlite3.connect("database/banking.db")

df = pd.read_sql_query(
    "SELECT * FROM loan_applications ORDER BY id DESC LIMIT 1",
    conn
)

conn.close()

if df.empty:
    st.warning("No loan applications found.")

else:

    st.metric(
        "Workflow Status",
        df.loc[0, "workflow_status"]
    )

    st.subheader("Recommendation")

    st.success(df.loc[0, "recommendation"])

    st.subheader("Current Stage")

    stages = [
        " Upload Documents",
        " AI Analysis",
        " Risk Assessment",
        " Fraud Detection",
        " Loan Officer Review",
        " Final Decision"
    ]

    for stage in stages:
        st.write(stage)