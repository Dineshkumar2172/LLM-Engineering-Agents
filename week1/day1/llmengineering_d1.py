import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('SAGE_TOKEN')}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

data = {
    "messages": [
        {
            "content": "What is the meaning of life?",
            "role": "user"
        }
    ],
    "model": "gpt-4o-mini"
}

response = requests.post(os.getenv("SAGE_URL"), headers=headers, json=data)
print(json.dumps(response.json(), indent=2))
