import streamlit as st
import sqlite3
import pandas as pd
from database.db import create_database

create_database()

st.set_page_config(
    page_title="Enterprise Banking Loan Agent",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Enterprise Banking Loan Processing & Fraud Intelligence Agent")

st.markdown("""
### AI-powered Banking Workflow Automation System

This application automates the complete loan approval process using **Google Gemini AI**, including:

-  Document Analysis
-  Risk Assessment
-  Fraud Detection
-  Workflow Automation
-  Banking Analytics
""")

st.divider()

# ------------------------------
# Dashboard Metrics
# ------------------------------

conn = sqlite3.connect("database/banking.db")
df = pd.read_sql_query("SELECT * FROM loan_applications", conn)
conn.close()

total = len(df)

approved = 0
review = 0
rejected = 0

if not df.empty:
    approved = len(df[df["workflow_status"] == "Approved"])
    review = len(df[df["workflow_status"] == "Manual Review"])
    rejected = len(df[df["workflow_status"] == "Rejected"])

col1, col2, col3, col4 = st.columns(4)

col1.metric(" Applications", total)
col2.metric(" Approved", approved)
col3.metric(" Manual Review", review)
col4.metric(" Rejected", rejected)

st.divider()

# ------------------------------
# Features
# ------------------------------

st.subheader(" Key Features")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info("\n\nAI Document Analysis")

with c2:
    st.info("\n\nRisk Assessment")

with c3:
    st.info("\n\nFraud Detection")

with c4:
    st.info("\n\nWorkflow Automation")

st.divider()

# ------------------------------
# Loan Workflow
# ------------------------------

st.subheader(" Loan Processing Workflow")

st.markdown("""
1.  Upload Loan Documents

2.  AI Document Analysis

3.  Risk Assessment

4.  Fraud Detection

5.  Loan Officer Review

6.  Final Decision
""")

st.divider()

# ------------------------------
# Technologies
# ------------------------------

st.subheader(" Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.success("""
 Python

 Streamlit

 SQLite
""")

with tech2:
    st.success("""
 Google Gemini AI

 PyMuPDF

 Pandas
""")

with tech3:
    st.success("""
 AI Agents

 Analytics

Automation
""")

st.divider()

st.caption(
    "Enterprise Banking Loan Processing & Fraud Intelligence Agent | Developed using Python, Streamlit & Google Gemini AI"
)