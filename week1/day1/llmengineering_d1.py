import json
import os
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key: raise ValueError("SAGE_TOKEN environment variable not set")

# headers = {
#     "Authorization": f"Bearer {os.getenv('SAGE_TOKEN')}",
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }

# data = {
#     "messages": [
#         {
#             "content": "What is the meaning of life?",
#             "role": "user"
#         }
#     ],
#     "model": "gpt-4o-mini"
# }

# response = requests.post(os.getenv("SAGE_URL"), headers=headers, json=data)
# print(json.dumps(response.json(), indent=2))

openai = OpenAI()

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
        
ed = Website("https://edwarddonner.com")
print(ed.title)
print(ed.text)

