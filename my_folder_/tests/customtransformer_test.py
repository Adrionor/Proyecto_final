import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

log_file = os.path.join("my_folder_", "tests", "custom_transformers.log")

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

class OutliersRemovalTransformer:
    def fit(self, X, y=None):
        # No fitting is required for this transformer
        return self
    
    def transform(self, X):
        logging.debug("Start transforming data by removing outliers...")
        
        # Perform outlier removal transformation here
        
        logging.debug("Outlier removal transformation completed.")
        return X

def main():
    logging.info("Starting the program...")

    # Rest of your code

if __name__ == "__main__":
    main()
