import streamlit as st
import sqlite3
import pandas as pd

st.title(" Banking Dashboard")

conn = sqlite3.connect("database/banking.db")

df = pd.read_sql_query(
    "SELECT * FROM loan_applications",
    conn
)

conn.close()

total = len(df)

approved = len(df[df["recommendation"] == "Approve"])

pending = len(df[df["recommendation"] == "Pending"])

rejected = len(df[df["recommendation"] == "Reject"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Applications", total)

col2.metric("Approved", approved)

col3.metric("Pending", pending)

col4.metric("Rejected", rejected)

st.divider()

st.subheader("Applications")

st.dataframe(df)