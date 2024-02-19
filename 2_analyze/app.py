from process import DataProcessor
from query_id import query_gpt_with_url

def main():
    choice = input("Voulez-vous (1) entrer une URL pour une requête GPT ou (2) procéder directement à l'analyse des données ? Entrez 1 ou 2 : ")
    if choice == '1':
        #not working because gpt 3 cannot "see" url
        query_gpt_with_url()
    elif choice == '2':
        processor1 = DataProcessor("../data/api_data_boamp.csv", sep=";", is_simap=False)
        processor1.load_and_process_data()
        processor1.save_data("../data/api_data_with_responses.csv")
        processor2 = DataProcessor("../data/api_data_simap.csv", is_simap=True)
        processor2.load_and_process_data()
        processor2.save_data("../data/api_data_with_responses_simap.csv")
    else:
        print("Choix non valide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()
