import pandas as pd
from query import OpenAIQuery

class DataProcessor:
    def __init__(self, filename, sep=',', is_simap=False):
        self.filename = filename
        self.sep = sep
        self.is_simap = is_simap
        self.df = None
        self.openai_query = OpenAIQuery()

    def load_and_process_data(self):
        self.df = pd.read_csv(self.filename, sep=self.sep)
        unique_field = "description" if self.is_simap else "objet"
        self.df = self.df.drop_duplicates(subset=[unique_field])
        self.df["gpt_response"] = self.df[unique_field].apply(self.openai_query.query_gpt)

    def save_data(self, output_filename):
        if self.df is not None:
            self.df.to_csv(output_filename, index=False, sep=self.sep)
