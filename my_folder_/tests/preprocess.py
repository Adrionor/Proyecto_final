import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging
import os

log_file = os.path.join("my_folder_", "tests", "preprocess.log")

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data: pd.DataFrame, preprocessed_data_file: str) -> pd.DataFrame:
        logging.debug("Start data preprocessing...")
        
        preprocessed_data = self.scaler.fit_transform(data)
        preprocessed_df = pd.DataFrame(preprocessed_data, columns=data.columns)
        preprocessed_df.to_csv(preprocessed_data_file, index=False)
        
        logging.debug("Data preprocessing completed.")
        
        return preprocessed_df

def preprocess_data(data: pd.DataFrame, preprocessed_data_file: str):
    # Preprocess the data
    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess(data, preprocessed_data_file)
    
    return preprocessed_data

def main():
    logging.info("Starting the program...")

    # Load bankruptcy data
    data = pd.read_csv(r"my_folder_\Data\data.csv")

    # Specify the file path for the preprocessed data file
    preprocessed_data_file = r"my_folder_\Data\preprocessed_data.csv"
    
    # Preprocess the data
    logging.info("Preprocessing the data...")
    preprocessed_data = preprocess_data(data, preprocessed_data_file)
    
    logging.info("Preprocessed data:\n%s", preprocessed_data)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR,
                        format="%(asctime)s %(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler("debug.log"),
                            logging.StreamHandler()
                        ])
    main()
