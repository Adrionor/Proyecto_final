# main.py
import argparse
import pandas as pd
from predict import ModelPredictor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Predictor')
    parser.add_argument('model_path', type=str, help='Path to the trained model file')
    parser.add_argument('new_data', type=str, help='Path to the file containing new data for prediction')
    
    args = parser.parse_args()

    predictor = ModelPredictor(args.model_path)

    new_data = pd.read_csv(args.new_data)

    predictions = predictor.predict(new_data)
    print(predictions)