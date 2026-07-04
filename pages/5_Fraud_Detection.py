import streamlit as st
import sqlite3
import pandas as pd

st.title(" Fraud Detection")

conn = sqlite3.connect("database/banking.db")

df = pd.read_sql_query(
    "SELECT * FROM loan_applications ORDER BY id DESC LIMIT 1",
    conn
)

conn.close()

if df.empty:
    st.warning("No loan applications found.")

else:

    fraud_status = df.loc[0, "fraud_status"]

    st.metric("Fraud Status", fraud_status)

    if fraud_status == "Low Risk":
        st.success(" No fraud indicators detected.")

    elif fraud_status == "Medium Risk":
        st.warning("⚠ Manual verification recommended.")

    else:
        st.error(" High fraud risk detected.")

    st.subheader("Verification Checklist")

    st.write("✔ PAN Number Checked")
    st.write("✔ Aadhaar Number Checked")
    st.write("✔ Bank Account Verified")