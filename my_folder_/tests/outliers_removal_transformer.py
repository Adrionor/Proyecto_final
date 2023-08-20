import logging
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

import os

log_file = os.path.join("my_folder_", "Preprocess", "preprocess.log")


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])
class OutliersRemovalTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        dataset = X.copy()
        for col in dataset.columns:
            logging.debug(f"Processing outliers removal for column {col}...")
            dataset = self.outliers_removal(dataset[col], str(col), dataset)
            logging.debug(f"Outliers removal completed for column {col}.")
        return dataset
    
    def outliers_removal(self, feature, feature_name, dataset):
        logging.debug(f"Calculating percentiles and IQR for feature {feature_name}...")
        q25, q75 = np.percentile(feature, 25), np.percentile(feature, 75)
        feat_iqr = q75 - q25
        logging.debug(f"Calculated IQR: {feat_iqr}")

        feat_cut_off = feat_iqr * 1.5
        feat_lower, feat_upper = q25 - feat_cut_off, q75 + feat_cut_off
        
        logging.debug("Identify outliers...")
        outliers = [x for x in feature if x < feat_lower or x > feat_upper]

        logging.debug(f"Removing outliers for feature {feature_name} from the dataset...")
        dataset = dataset.drop(dataset[(dataset[feature_name] > feat_upper) | (dataset[feature_name] < feat_lower)].index)
        logging.debug(f"Outliers removal completed for feature {feature_name}.")
        
        return dataset

def main():
    logging.info("Starting the program...")
    
    # Create an instance of the OutliersRemovalTransformer class
    logging.debug("Creating an instance of the OutliersRemovalTransformer class...")
    transformer = OutliersRemovalTransformer()
    logging.debug("Instance of the OutliersRemovalTransformer class has been created successfully.")
    
    # Perform the transformation
    logging.debug("Performing transformation...")
    transformed_dataset = transformer.transform(X)
    logging.debug("Transformation completed.")
    
    logging.info("Program execution completed.")

if __name__ == "__main__":
    main()
