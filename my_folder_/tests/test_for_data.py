import logging
import pandas as pd
import os
import pytest

log_file = os.path.join("my_folder_", "tests", "data_test.log")

class TestDataExistence:
    def test_data_existence(self):
        logging.debug("Loading training data...")
        df_train = pd.read_csv(r'my_folder_\Data\preprocessed_data.csv')
        logging.debug("Training data loaded successfully.")
        
        logging.debug("Verifying training data existence...")
        assert not df_train.empty, "No training data"
        logging.debug("Training data exists.")

def test_main():
    logging.info("Starting the tests...")
    
    # Run the test cases
    logging.debug("Running the test cases...")
    pytest.main(['-s', '-v'])
    
    logging.info("Tests completed.")
