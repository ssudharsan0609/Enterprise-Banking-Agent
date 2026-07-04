import json

def extract_json(response):

    response = response.replace("```json", "")
    response = response.replace("```", "")

    data = json.loads(response)

    return data