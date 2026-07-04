def calculate_risk(
    monthly_salary,
    loan_amount,
    documents_complete=True
):
    score = 0

    # Salary Check
    if monthly_salary >= 80000:
        score += 40

    elif monthly_salary >= 50000:
        score += 30

    elif monthly_salary >= 30000:
        score += 20

    else:
        score += 10

    # Loan Amount Check
    if loan_amount <= monthly_salary * 20:
        score += 30
    else:
        score += 10

    # Documents Check
    if documents_complete:
        score += 30

    return score