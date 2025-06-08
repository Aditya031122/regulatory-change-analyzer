import requests
import json


def analyze_with_llm(change_text):
    prompt = f"""
You are an expert in regulatory compliance.

Analyze the following regulatory text change and return a JSON with:
1. change_summary: A brief one-line summary of the change.
2. change_type: One of ["New Requirement", "Clarification of Existing Requirement", "Deletion of Requirement", "Minor Edit"]

Text:
\"\"\"{change_text}\"\"\"
Only return the JSON object.
"""

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False  
        })

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "").strip()
        else:
            return json.dumps({
                "error": f"Request failed with status {response.status_code}",
                "details": response.text
            })

    except Exception as e:
        return json.dumps({
            "error": "Failed to get a valid response from Gemma 2B",
            "details": str(e)
        })
