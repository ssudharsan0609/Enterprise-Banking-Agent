import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_document(text):

    prompt = f"""
You are an AI Loan Processing Agent.

Analyze the following banking document.

Return ONLY valid JSON.

Schema:

{{
"document_type":"",
"customer_name":"",
"company_name":"",
"monthly_salary":"",
"pan_number":"",
"aadhaar_number":"",
"bank_name":"",
"account_number":"",
"summary":""
}}

Document:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text