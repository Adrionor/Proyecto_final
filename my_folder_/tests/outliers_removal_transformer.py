from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class OutliersRemovalTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        dataset = X.copy()
        for col in dataset.columns:
            dataset = self.outliers_removal(dataset[col], str(col), dataset)
        return dataset
    
    def outliers_removal(self, feature, feature_name, dataset):
        q25, q75 = np.percentile(feature, 25), np.percentile(feature, 75)
        feat_iqr = q75 - q25
        feat_cut_off = feat_iqr * 1.5
        feat_lower, feat_upper = q25 - feat_cut_off, q75 + feat_cut_off
        outliers = [x for x in feature if x < feat_lower or x > feat_upper]
        dataset = dataset.drop(dataset[(dataset[feature_name] > feat_upper) | (dataset[feature_name] < feat_lower)].index)
        return dataset