def detect_fraud(data):

    fraud_score = 0
    reasons = []

    # PAN Missing
    if not data.get("pan_number"):
        fraud_score += 20
        reasons.append("PAN Number Missing")

    # Aadhaar Missing
    if not data.get("aadhaar_number"):
        fraud_score += 20
        reasons.append("Aadhaar Number Missing")

    # Salary Missing
    if not data.get("monthly_salary"):
        fraud_score += 20
        reasons.append("Salary Information Missing")

    if fraud_score >= 40:
        status = "High Risk"

    elif fraud_score >= 20:
        status = "Medium Risk"

    else:
        status = "Low Risk"

    return {
        "fraud_score": fraud_score,
        "status": status,
        "reasons": reasons
    }