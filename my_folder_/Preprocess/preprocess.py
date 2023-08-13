import pandas as pd
from sklearn.linear_model import LogisticRegression

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

def train_model(X: pd.DataFrame):
    # Train the model
    classifier = LogisticRegression()
    classifier.fit(X, X)

    # Print the coefficients
    print("Coefficients:", classifier.coef_)

def main():
    # Load preprocessed data
    file_path = r"my_folder_\Data\preprocessed_data.csv"
    loader = DataLoader(file_path)
    data = loader.load_data()

    # Exclude the target variable
    X = data

    # Train the model
    train_model(X)

if __name__ == "__main__":
    main()
