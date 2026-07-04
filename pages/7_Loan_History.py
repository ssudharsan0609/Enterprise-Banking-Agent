import streamlit as st
import sqlite3
import pandas as pd

st.title("Loan History")

conn = sqlite3.connect("database/banking.db")

df = pd.read_sql_query(
    "SELECT * FROM loan_applications",
    conn
)

conn.close()

st.dataframe(df)