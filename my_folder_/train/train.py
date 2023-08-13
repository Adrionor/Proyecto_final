import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = r"my_folder_\Data\data.csv"

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

def train_model(data: pd.DataFrame):
    # Split features and labels
    X = data.drop("Bankrupt?", axis=1)
    y = data["Bankrupt?"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # Evaluate the model
    accuracy = classifier.score(X_test, y_test)
    print("Accuracy:", accuracy)

def main():
    # Load bankruptcy data
    loader = DataLoader("bankruptcy_data.csv")
    data = loader.load_data()

    # Train the model
    train_model(data)

if __name__ == "__main__":
    main()
