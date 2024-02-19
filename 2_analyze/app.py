from process import DataProcessor

def main():
    processor1 = DataProcessor("../data/api_data_boamp.csv", sep=";", is_simap=False)
    processor1.load_and_process_data()
    processor1.save_data("../data/api_data_with_responses.csv")
    processor2 = DataProcessor("../data/api_data_simap.csv", is_simap=True)
    processor2.load_and_process_data()
    processor2.save_data("../data/api_data_with_responses_simap.csv")


if __name__ == "__main__":
    main()
