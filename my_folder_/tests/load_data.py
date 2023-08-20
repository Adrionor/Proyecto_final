import logging
import os
import pandas as pd
log_file = os.path.join("my_folder_", "tests", "load.log")
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        logging.debug("Start loading data from CSV...")
        data = pd.read_csv(self.file_path)
        logging.debug("Data has been loaded successfully.")
        return data

def main():
    logging.info("Starting the program...")

    # Create an instance of the DataLoader class
    loader = DataLoader("my_folder_/Data/data.csv")

    logging.debug("Start loading data...")
    data = loader.load_data()
    logging.debug("Data has been loaded.")

    logging.info("Data loaded successfully.")

    logging.info("Program execution completed.")

if __name__ == "__main__":
    main()
