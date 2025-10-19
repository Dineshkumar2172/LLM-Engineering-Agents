# Three topics to be covered on this day
#
#       1. Models - open source, closed source, multi-modal architecture and which one to choose
#       2. Tools - HuggingFace, Langchain, Gradio, Weights & Biases, Modal
#       3. Techniques - APIs, Multi-shot prompting, RAG, Fine-tuning, Agenization

# Closed-Source Frontier Models (Or paid models)
#
#     GPT from OpenAI
#     Claude from Anthropic
#     Gemini from Google DeepMind
#     Perplexity 
#
# Open-Source Frontier Models
#
#     LLaMA from Meta
#     Mixtral from Mistral
#     Qwen from Alibaba Cloud
#     Gemma from Google
#     Phi from Microsoft
#
#33 Three ways to use models
#
#     1. Chat interfaces like ChatGPT, Claude, Bard
#     2. Cloud APIs - LLM API (accessing through code instead of chat interface - per API request cost)
#        Frameworks like Langchain - provides unified interface to access multiple models
#        Managed AI Cloud services - Amazon bedrock, Google Vertex, Azure ML
#     3. Direct inference - downloading model weights and running inference on local machine or cloud VM
#        With the HuggingFace transformers library, you can run inference on many open-source models
#        With Ollama to run locally

# benefits of using local models
#       1. no API charges - open source
#       2. data doesn't leave our box
#
# only disadvantage would be it's significantly less powerful than frontier model.

import requests
from bs4 import BeautifulSoup

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False
}

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])


# using ollama directly instead
import ollama

response = ollama.chat(model=MODEL, messages=messages)
print(response.json()['message']['content'])

