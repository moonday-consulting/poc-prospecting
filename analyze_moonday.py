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
                {
                    "role": "system",
                    "content": """



                 Tu es employe chez Mooday Consulting. Cette entreprise est Moonday est un cabinet de conseil en stratégie et organisation spécialisé dans la modélisation et l’analyse de données.

                 Créé en 2016, le cabinet a été fondé sur le principe que la Data et sa richesse ne sont pas toujours efficacement exploitées
                 par les entreprises.
                 Moonday est le premier cabinet de conseil alliant le consulting traditionnel en stratégie-organisation 
                 et la Data, actif qui, bien exploité, vous aide à prendre des décisions pour optimiser vos performances.

                 Je vais te donner une description d'appel d'offre et tu dois me dire si cela correspond a notre offre. 
                 Tu ne dois repondre que TRUE ou FALSE rien de plus""",
                },
                {"role": "user", "content": row},
            ],
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"


df = pd.read_csv("api_data.csv", sep=";")
df_unique = df.drop_duplicates(subset=["objet"])
df_unique["gpt_response"] = df_unique["objet"].apply(query_gpt)
df_unique.to_csv("api_data_with_responses.csv", index=False, sep=";")

df = pd.read_csv("api_data_simap.csv")
df_unique = df.drop_duplicates(subset=["description"])
df_unique["gpt_response"] = df_unique["description"].apply(query_gpt)
df_unique.to_csv("api_data_with_responses_simap.csv", index=False)

df1 = pd.read_csv("api_data_with_responses.csv", sep=";")
df2 = pd.read_csv("api_data_with_responses_simap.csv", sep=",")
df1_transformed = df1[["idweb", "objet", "gpt_response", "url_pdf"]].copy()
df1_transformed.columns = ["id", "desc", "gpt_responses", "url_pdf"]
df1_transformed["country"] = "FRANCE"
df2_transformed = df2[["id", "description", "gpt_response"]].copy()
df2_transformed.columns = ["id", "desc", "gpt_responses"]
df2_transformed["url_pdf"] = ""
df2_transformed["country"] = "SUISSE"
df_fusion = pd.concat([df1_transformed, df2_transformed], ignore_index=True)
df_fusion.to_csv("api_data_fusion_moonday.csv", index=False)
