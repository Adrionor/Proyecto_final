import logging
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import os

log_file = os.path.join("my_folder_", "train", "train.log")

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

def train_model(data: pd.DataFrame, preprocessed_data_file: str):
    logging.debug("Start model training...")

    # Split features and labels
    X = data.drop("Bankrupt?", axis=1)
    y = data["Bankrupt?"]

    # Preprocess the data
    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess(X, preprocessed_data_file)

    # Split preprocessed data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(preprocessed_data, y, test_size=0.2, random_state=42)

    # Train and evaluate the bankruptcy classifier
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    accuracy = classifier.score(X_test, y_test)

    logging.error("Accuracy: %s", accuracy)

def main():
    logging.info("Starting the main function...")

    # Load bankruptcy data
    data = pd.read_csv(r"my_folder_\Data\data.csv")

    # Specify the file path for the preprocessed data file
    preprocessed_data_file = r"my_folder_\Data\preprocessed_data.csv"

    # Train the model and save the preprocessed data to a file
    train_model(data, preprocessed_data_file)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR,
                        format="%(asctime)s %(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])
    logging.info("Application starting...")
    main()
    logging.info("Application execution completed.")
