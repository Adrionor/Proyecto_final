import argparse
import joblib
import pandas as pd
from imblearn.pipeline import make_pipeline as imbalanced_make_pipeline
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

class ModelPredictor:
    
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, new_data):
        # Applying StandardScaler
        SC = StandardScaler()
        new_data = pd.DataFrame(SC.fit_transform(new_data.values), 
                                index=new_data.index, columns=new_data.columns)
        return self.model.predict(new_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Predictor')
    parser.add_argument('model_path', type=str, help='Path to the trained model file')
    parser.add_argument('new_data', type=str, help='Path to the file containing new data for prediction')
    
    args = parser.parse_args()

    predictor = ModelPredictor(args.model_path)

    new_data = pd.read_csv(args.new_data)

    predictions = predictor.predict(new_data)
    print(predictions)
