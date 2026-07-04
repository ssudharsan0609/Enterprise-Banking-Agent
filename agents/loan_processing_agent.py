import re

from utils.pdf_reader import extract_text_from_pdf

from agents.document_agent import analyze_document
from agents.extraction_agent import extract_json

from agents.risk_agent import calculate_risk
from agents.fraud_agent import detect_fraud
from agents.workflow_agent import determine_workflow


def process_loan_application(pdf_path, loan_amount):

    # Step 1 - Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Step 2 - AI Analysis
    ai_response = analyze_document(text)

    # Step 3 - Extract JSON
    data = extract_json(ai_response)

    # Step 4 - Extract Salary
    salary = data.get("monthly_salary", "0")

    salary = str(salary)

    # Remove INR, ₹, commas, spaces etc.
    salary = re.sub(r"[^0-9.]", "", salary)

    try:
        salary = float(salary)
    except:
        salary = 0

    print("Extracted Salary:", salary)

    # Step 5 - Calculate Risk
    risk_score = calculate_risk(
        monthly_salary=salary,
        loan_amount=loan_amount,
        documents_complete=True
    )

    # Step 6 - Fraud Detection
    fraud = detect_fraud(data)

    # Step 7 - Workflow Decision
    workflow = determine_workflow(
        risk_score,
        fraud["status"]
    )

    return {
        "document": data,
        "risk_score": risk_score,
        "fraud": fraud,
        "workflow": workflow
    }