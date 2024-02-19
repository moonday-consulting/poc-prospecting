import openai
from dotenv import load_dotenv
import os
import traceback

load_dotenv("../.env")

def query_gpt_with_url():
    url = input("Veuillez entrer une URL : ")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=[
                {"role": "system", "content": "Tu dois donner l'identite de ce site avec un texte recapitulant son secteur, et ses services :"},
                {"role": "user", "content": url}
            ]
        )
        result = response.choices[0].message["content"]
        print("Résultat de la requête GPT :", result)
        with open("../data/query.txt", "w", encoding="utf-8") as file:
            file.write(result)
    except Exception as e:
        print(f"Une erreur s'est produite lors de la requête à l'API OpenAI : {e}")
        traceback.print_exc()
