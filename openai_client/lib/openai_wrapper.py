import os
import openai
from dotenv import load_dotenv

class OpenAiWrapper:
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def __init__(self, model:str = "gpt-3.5-turbo"):
        self.model = model

    def complete_chat(self, prompt: str):
        return openai.ChatCompletion.create(model = self.model, messages = prompt)
