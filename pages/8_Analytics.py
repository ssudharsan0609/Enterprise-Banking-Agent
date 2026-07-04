import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Banking Analytics")

conn = sqlite3.connect("database/banking.db")

df = pd.read_sql_query(
    "SELECT * FROM loan_applications",
    conn
)

conn.close()

if df.empty:
    st.warning("No applications available.")
    st.stop()

# Loan Type Distribution
st.subheader(" Loan Type Distribution")

fig1 = px.pie(
    df,
    names="loan_type",
    title="Loan Types"
)

st.plotly_chart(fig1, use_container_width=True)

# Recommendation Distribution
st.subheader(" Recommendation Distribution")

fig2 = px.bar(
    df,
    x="recommendation",
    title="Recommendations"
)

st.plotly_chart(fig2, use_container_width=True)

# Risk Score Distribution
st.subheader(" Risk Score")

fig3 = px.histogram(
    df,
    x="risk_score",
    nbins=10,
    title="Risk Score Distribution"
)

st.plotly_chart(fig3, use_container_width=True)