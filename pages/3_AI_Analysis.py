import streamlit as st
import sqlite3
import pandas as pd

st.title(" AI Document Analysis")

conn = sqlite3.connect("database/banking.db")

query = """
SELECT *
FROM loan_applications
ORDER BY id DESC
LIMIT 1
"""

df = pd.read_sql_query(query, conn)

conn.close()

if df.empty:
    st.warning("No loan applications found.")

else:

    st.success("Latest AI Analysis")

    st.write("###  Customer Name")
    st.write(df.loc[0, "customer_name"])

    st.write("###  Document Type")
    st.write(df.loc[0, "document_type"])

    st.write("###  Company Name")
    st.write(df.loc[0, "company_name"])

    st.write("###  Monthly Salary")
    st.write(df.loc[0, "monthly_salary"])

    st.write("###  AI Summary")
    st.write(df.loc[0, "summary"])