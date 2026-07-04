import streamlit as st
import sqlite3
import pandas as pd

st.title(" Risk Assessment")

conn = sqlite3.connect("database/banking.db")

df = pd.read_sql_query(
    "SELECT * FROM loan_applications ORDER BY id DESC LIMIT 1",
    conn
)

conn.close()

if df.empty:
    st.warning("No loan applications found.")

else:

    risk_score = df.loc[0, "risk_score"]

    st.metric("Risk Score", risk_score)

    if risk_score >= 80:
        st.success(" Low Risk")

    elif risk_score >= 50:
        st.warning(" Medium Risk")

    else:
        st.error(" High Risk")

    st.subheader("AI Recommendation")

    if risk_score >= 80:
        st.write("✔ Customer is eligible for loan approval.")

    elif risk_score >= 50:
        st.write("✔ Manual review by Loan Officer is recommended.")

    else:
        st.write("✔ High risk. Loan should be rejected.")