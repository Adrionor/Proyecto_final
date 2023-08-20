import logging
import unittest
import pandas as pd
import os

log_file = os.path.join("my_folder_", "tests", "data_test.log")

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])
class TestDataExistence(unittest.TestCase):
    def test_data_existence(self):
        logging.debug("Loading training data...")
        df_train = pd.read_csv(r'my_folder_\Data\preprocessed_data.csv')
        logging.debug("Training data loaded successfully.")
        
        logging.debug("Verifying training data existence...")
        self.assertFalse(df_train.empty, "No training data")
        logging.debug("Training data exists.")

def main():
    logging.info("Starting the tests...")
    
    # Run the test cases
    logging.debug("Running the test cases...")
    unittest.main()
    
    logging.info("Tests completed.")

if __name__ == '__main__':
    main()
