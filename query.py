import openai
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIQuery:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def query_gpt(self, row):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": query},
                    {"role": "user", "content": row},
                ],
            )
            return completion.choices[0].message["content"]
        except Exception as e:
            return f"Error: {e}"
