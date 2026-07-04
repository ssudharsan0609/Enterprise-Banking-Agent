import streamlit as st
import os

from agents.loan_processing_agent import process_loan_application
from database.database_manager import save_application

st.title(" Loan Application")

customer_name = st.text_input("Customer Name")

loan_amount = st.number_input(
    "Loan Amount",
    min_value=1000
)

loan_type = st.selectbox(
    "Loan Type",
    [
        "Home Loan",
        "Personal Loan",
        "Vehicle Loan",
        "Education Loan",
        "Business Loan"
    ]
)

uploaded_file = st.file_uploader(
    "Upload Loan Document",
    type=["pdf"]
)

if st.button("Submit Application"):

    if uploaded_file is None:
        st.error("Please upload a document.")

    else:

        os.makedirs("uploads", exist_ok=True)

        filepath = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())

       
        result = process_loan_application(
            filepath,
            loan_amount
        )

        # Extract document data
        data = result["document"]

        # Save to database
        save_application(
            customer_name,
            loan_amount,
            loan_type,
            data,
            result["risk_score"],
            result["fraud"]["status"],
            result["workflow"]["workflow_status"],
            result["workflow"]["recommendation"]
        )

        # Display results
        st.success("Application Saved Successfully!")

        st.subheader(" AI Extracted Information")
        st.json(data)

        st.subheader(" Risk Score")
        st.metric("Risk Score", result["risk_score"])

        st.subheader(" Fraud Detection")
        st.write(result["fraud"]["status"])
        st.write(result["fraud"]["reasons"])

        st.subheader(" Workflow")
        st.write(result["workflow"]["workflow_status"])
        st.write(result["workflow"]["recommendation"])
        st.write(result["workflow"]["next_step"])