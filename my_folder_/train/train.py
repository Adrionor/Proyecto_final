import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data: pd.DataFrame, preprocessed_data_file: str) -> pd.DataFrame:
        preprocessed_data = self.scaler.fit_transform(data)
        preprocessed_df = pd.DataFrame(preprocessed_data, columns=data.columns)
        preprocessed_df.to_csv(preprocessed_data_file, index=False)
        return preprocessed_df

def train_model(data: pd.DataFrame, preprocessed_data_file: str):
    # Split features and labels
    X = data.drop("Bankrupt?", axis=1)
    y = data["Bankrupt?"]

    # Preprocess the data
    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess(X, preprocessed_data_file)

    # Split preprocessed data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(preprocessed_data, y, test_size=0.2, random_state=42)

    # Train and evaluate bankruptcy classifier
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    accuracy = classifier.score(X_test, y_test)
    print("Accuracy:", accuracy)

def main():
    # Load bankruptcy data
    data = pd.read_csv(r"my_folder_\Data\data.csv")

    # Specify the file path for the preprocessed data file
    preprocessed_data_file = r"my_folder_\Data\preprocessed_data.csv"
    
    # Train the model and save the preprocessed data to a file
    train_model(data, preprocessed_data_file)

if __name__ == "__main__":
    main()
