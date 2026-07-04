import sqlite3

def save_application(
    customer_name,
    loan_amount,
    loan_type,
    data,
    risk_score=0,
    fraud_status="Pending",
    workflow_status="Pending",
    recommendation="Pending"
):

    conn = sqlite3.connect("database/banking.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO loan_applications(
        customer_name,
        loan_amount,
        loan_type,
        document_type,
        company_name,
        monthly_salary,
        pan_number,
        aadhaar_number,
        bank_name,
        account_number,
        summary,
        risk_score,
        fraud_status,
        workflow_status,
        recommendation
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        customer_name,
        loan_amount,
        loan_type,
        data.get("document_type"),
        data.get("company_name"),
        data.get("monthly_salary"),
        data.get("pan_number"),
        data.get("aadhaar_number"),
        data.get("bank_name"),
        data.get("account_number"),
        data.get("summary"),
        risk_score,
        fraud_status,
        workflow_status,
        recommendation
    ))

    conn.commit()
    conn.close()