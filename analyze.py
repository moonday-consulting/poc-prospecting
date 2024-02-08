import os
import pandas as pd
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def query_gpt(row):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": """
                 Tu es employe chez Mooday Consulting. Cette entreprise est Moonday est un cabinet de conseil en stratégie et organisation spécialisé dans la modélisation et l’analyse de données.

Créé en 2016, le cabinet a été fondé sur le principe que la Data et sa richesse ne sont pas toujours efficacement exploitées par les entreprises.

Moonday est le premier cabinet de conseil alliant le consulting traditionnel en stratégie-organisation et la Data, actif qui, bien exploité, vous aide à prendre des décisions pour optimiser vos performances.
                 Je vais te donner une description d'appel d'offre et tu dois me dire si cela correspond a notre offre. Tu ne dois repondre que TRUE ou FALSE rien de plus"""},
                {"role": "user", "content": row}
            ]
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"

df = pd.read_csv("api_data.csv", sep=';')
df["gpt_response"] = df["objet"].apply(query_gpt)
df.to_csv("api_data_with_responses.csv", index=False, sep=';')
