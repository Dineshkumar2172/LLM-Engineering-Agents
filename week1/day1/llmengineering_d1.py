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

# openai = OpenAI()
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
# print(ed.title)
# print(ed.text)

# Types of prompts
#       1. system prompt - that tells them what task they are performing and what tone they should use.
#       2. user prompt - the conversation startedr that they should reply to.
#
# For example:
#       System Prompt: “You are a helpful assistant knowledgeable in technology and programming. Respond in a friendly and informative manner.”
#       User Prompt: “Can you explain the difference between Python and JavaScript?”
#       In this example, the system prompt sets the AI’s role and tone, while the user prompt provides the specific question the AI needs to address.
#
# Define our system prompt
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring texts that might be navigation related.\
Respond in markdown."

# A function that writes a user prompt that asks for summaries of websites:
def user_prompt_for(website):
    user_prompt = f"you are looking at website titled {website.title}"
    user_prompt += "The contents of this website is as follows: \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize them too. \n\n"
    user_prompt += website.text
    return user_prompt

# Messages
# The API from OpenAI expects to receive messages in a particular structure. Many of the other APIs share this structure
#
#       [
#              {"role": "system", "content": "system message goes here"},
#              {"role": "user", "content": "user message goes here"}
#       ]
#
# below functions creates exactly the prompt above
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# # and now: call the OpenAI API.
# def summarize(url):
#     website = Website(url)
#     response = openai.chat.completions.create(
#         model = "gpt-40-mini",
#         messages = messages_for(website)
#     )
#     return response.choices[0].message.content

# summarize("https://edwarddonner.com")

# def display_summary(url):
#     summary = summarize(url)
#     display(Markdown(summary))

# display_summary("https://edwarddonner.com")

# tailoring it to support our sage API instead of OpenAI import - use to get response from our sage
def sage_ai(messages, model):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = { "messages": messages, "model": model }
    response = requests.post(os.getenv("SAGE_URL"), headers=headers, json=data)
    return response.json()

def summarize(url):
    website = Website(url)
    response = sage_ai( model = "gpt-4o-mini", messages = messages_for(website) )    
    return response["choices"][0]["message"]["content"]

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))

display_summary("https://edwarddonner.com")
