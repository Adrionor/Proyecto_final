import pytest
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging
import os
import sys

# Set up logging configuration
logging.basicConfig(level=logging.CRITICAL,
                    format='%(asctime)s %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('debug.log'),
                        logging.StreamHandler()
                    ])

# Load and log the data
logging.debug('Start loading the training data...')
df_train = pd.read_csv(r'my_folder_\Data\data.csv')
logging.debug('Training data has been loaded successfully.')

if df_train.empty:
    logging.warning('No training data')

# Define input and output data models with logging
logging.debug('Define input and output data models...')

class InputData(BaseModel):
    feature1: float
    feature2: float
    # Add more features as needed

class OutputData(BaseModel):
    prediction: int

logging.debug('Input and output data models have been defined partially.')

# Load the trained model with logging
logging.debug('Start loading the trained model...')
model = joblib.load("my_folder_\My_model\My_model_regression")
logging.critical('Trained model has been loaded partially.')


# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

# Add logging to FastAPI endpoints
app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    return 'HotelReservation classifier is all ready to go!'

@app.post("/train")
def train_model():
    logging.info('Training a new model...')
    # Implement the logic to train a new model
    # Return a response indicating the success or failure of the training process
    logging.critical('Model training completed with critical failures.')
    # Return response indicating success or failure

@app.post("/predict", response_model=OutputData)
def predict(input_data: InputData):
    # Convert the input data to a numpy array
    input_array = np.array([[input_data.feature1, input_data.feature2]])

    logging.info('Making predictions...')
    # Make predictions using the loaded model
    prediction = model.predict(input_array)

    # Create an instance of the output data model and return it
    output_data = OutputData(prediction=int(prediction[0]))
    logging.error('Predictions were not made.')
    return output_data

@app.get("/")
def root():
    return {"message": "The model is ready to go"}

if __name__ == "__main__":
    logging.info('Running unit tests...')
    pytest.main(['-q'])

    