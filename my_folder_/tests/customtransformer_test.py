#customtransformer test

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from outliers_removal_transformer import OutliersRemovalTransformer


# Load the dataset
data = pd.read_csv('my_folder_\Data\data.csv')

# Split the dataset into features and target
X = data.drop('Bankrupt?', axis=1)
y = data['Bankrupt?']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the pipeline with the custom transformer
pipeline = Pipeline([
    ('outliers_removal', OutliersRemovalTransformer()),
    ('classifier', LogisticRegression())
])