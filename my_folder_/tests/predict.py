# predictor.py
import logging
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

log_file = os.path.join("my_folder_", "tests", "predict.log")


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler()
                    ])

logging.debug("Start loading the trained model...")
model = joblib.load(r"my_folder_\My_model\My_model_regression")
logging.debug("Trained model has been loaded successfully.")

class ModelPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, new_data):
        logging.debug("Start applying StandardScaler...")
        SC = StandardScaler()
        new_data = pd.DataFrame(SC.fit_transform(new_data.values),
                                index=new_data.index, columns=new_data.columns)
        logging.debug("StandardScaler has been applied successfully.")
        
        logging.debug("Start making predictions...")
        predictions = self.model.predict(new_data)
        logging.debug("Predictions have been made.")
        
        return predictions

def main():
    logging.info("Starting the main function...")
    
    # Load new data for prediction
    new_data = pd.read_csv(r"my_folder_\Data\data.csv")
    
    # Create an instance of the ModelPredictor class
    predictor = ModelPredictor(r"my_folder_\My_model\My_model_regression")
    
    # Perform prediction on the new data
    predictions = predictor.predict(new_data)
    
    logging.info("Predictions: %s", predictions)
    
    logging.info("Main function execution completed.")

if __name__ == "__main__":
    logging.info("Application starting...")
    main()
    logging.info("Application execution completed.")
