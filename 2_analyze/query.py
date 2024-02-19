import openai
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIQuery:
    def __init__(self, query_file='../data/query.txt'):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.query = self.load_query_from_file(query_file)

    def load_query_from_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except Exception as e:
            return f"Error loading query from {filepath}: {e}"

    def query_gpt(self, row):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": self.query},
                    {"role": "user", "content": row},
                ],
            )
            return completion.choices[0].message["content"]
        except Exception as e:
            return f"Error: {e}"