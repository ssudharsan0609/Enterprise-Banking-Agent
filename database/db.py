import sqlite3

def create_database():

    conn = sqlite3.connect("database/banking.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_applications(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_name TEXT,

        loan_amount REAL,

        loan_type TEXT,

        document_type TEXT,

        company_name TEXT,

        monthly_salary REAL,

        pan_number TEXT,

        aadhaar_number TEXT,

        bank_name TEXT,

        account_number TEXT,

        summary TEXT,

        risk_score INTEGER,

        fraud_status TEXT,

        workflow_status TEXT,

        recommendation TEXT

    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database Created Successfully!")