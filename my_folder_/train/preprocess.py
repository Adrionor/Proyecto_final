import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data: pd.DataFrame, preprocessed_data_file: str) -> pd.DataFrame:
        preprocessed_data = self.scaler.fit_transform(data)
        preprocessed_df = pd.DataFrame(preprocessed_data, columns=data.columns)
        preprocessed_df.to_csv(preprocessed_data_file, index=False)
        return preprocessed_df

def preprocess_data(data: pd.DataFrame, preprocessed_data_file: str):
    # Preprocess the data
    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess(data, preprocessed_data_file)
    
    return preprocessed_data

def main():
    # Load bankruptcy data
    data = pd.read_csv(r"my_folder_\Data\data.csv")

    # Specify the file path for the preprocessed data file
    preprocessed_data_file = r"my_folder_\Data\preprocessed_data.csv"
    
    # Preprocess the data
    preprocessed_data = preprocess_data(data, preprocessed_data_file)
    
    print("Preprocessed data:\n", preprocessed_data)

if __name__ == "__main__":
    main()
