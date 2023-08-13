import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        preprocessed_data = self.scaler.fit_transform(data)
        return pd.DataFrame(preprocessed_data, columns=data.columns)

# Load bankruptcy data
data = pd.read_csv("my_folder_\Data\data.csv")

# Split features and labels
X = data.drop("Bankrupt?", axis=1)
y = data["Bankrupt?"]

# Preprocess the data
preprocessor = DataPreprocessor()
X_preprocessed = preprocessor.preprocess(X)

# Split preprocessed data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

# Train and evaluate bankruptcy classifier
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
accuracy = classifier.score(X_test, y_test)
print("Accuracy:", accuracy)