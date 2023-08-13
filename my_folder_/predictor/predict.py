# predictor.py
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

class ModelPredictor:
    
    def __init__(self, model_path):
        self.model = joblib.load(r'my_folder_\My_model\My_model_regression')

    def predict(self, new_data):
        # Applying StandardScaler
        SC = StandardScaler()
        new_data = pd.DataFrame(SC.fit_transform(new_data.values), 
                                index=new_data.index, columns=new_data.columns)
        return self.model.predict(new_data)


def main():
    # Load new data for prediction
    new_data = pd.read_csv(r"my_folder_\Data\preprocessed_data.csv")
        
    # Create an instance of the ModelPredictor class
    predictor = ModelPredictor(r"my_folder_\My_model\My_model_regression")

    # Perform prediction on the new data
    predictions = predictor.predict(new_data)
    
    print("Predictions:", predictions)

if __name__ == "__main__":
    main()