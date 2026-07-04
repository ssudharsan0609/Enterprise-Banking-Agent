def determine_workflow(risk_score, fraud_status):
    """
    Determines the workflow based on
    Risk Score and Fraud Status.
    """

    # High fraud always goes to investigation
    if fraud_status == "High Risk":
        return {
            "workflow_status": "Manual Investigation",
            "recommendation": "Reject",
            "next_step": "Fraud Investigation Team"
        }

    # Low Risk Applicant
    if risk_score >= 80:
        return {
            "workflow_status": "Approved",
            "recommendation": "Approve",

            "next_step": "Loan Disbursement"
        }

    # Medium Risk Applicant
    elif risk_score >= 50:
        return {
            "workflow_status": "Manual Review",
            "recommendation": "Review",
            "next_step": "Loan Officer Review"
        }

    # High Risk Applicant
    else:
        return {
            "workflow_status": "Rejected",
            "recommendation": "Reject",
            "next_step": "Notify Customer"
        }