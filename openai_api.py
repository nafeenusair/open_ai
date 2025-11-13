import os
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIAPI:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        
        print("OpenAI API client initialized.")