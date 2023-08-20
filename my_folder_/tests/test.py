import logging
import unittest
import pandas as pd
from load_data import DataLoader
from preprocess import DataPreprocessor
from predict import ModelPredictor
import os

log_file = os.path.join("my_folder_", "tests", "test.log")

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

class ModelTester(unittest.TestCase):
    def test_predictions(self):
        logging.debug("Loading test data...")
        data_loader = DataLoader('test_data.csv')
        test_data = data_loader.load_data()
        logging.debug("Test data loaded successfully.")

        logging.debug("Preprocessing test data...")
        preprocessor = DataPreprocessor()
        preprocessed_data = preprocessor.preprocess(test_data)
        logging.debug("Test data preprocessed successfully.")

        logging.debug("Loading model...")
        predictor = ModelPredictor('model.pkl')
        logging.debug("Model loaded successfully.")

        logging.debug("Making predictions...")
        predictions = predictor.predict(preprocessed_data)
        logging.debug("Predictions made successfully.")

        logging.debug("Performing assertions...")
        self.assertEqual(len(predictions), len(test_data))
        # Add more assertions as needed
        logging.debug("Assertions passed.")

        logging.debug("Test completed.")

if __name__ == '__main__':
    logging.info("Starting the tests...")
    
    # Run the test cases
    logging.debug("Running the test cases...")
    unittest.main()
    
    logging.info("Tests completed.")
