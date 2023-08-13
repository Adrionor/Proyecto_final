# preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    """
    A class used to preprocess data.

    ...

    Attributes
    ----------
    scaler : sklearn StandardScaler
        A scaler object used for data normalization.

    Methods
    -------
    preprocess(data: pd.DataFrame) -> pd.DataFrame
        Preprocesses the input data.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the DataPreprocessor object.
        """
        self.scaler = StandardScaler()

    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocesses the input data.

        Parameters
        ----------
            data : pd.DataFrame
                Input data to be preprocessed.

        Returns
        -------
            pd.DataFrame
                Preprocessed data.
        """
        # Apply data preprocessing steps here
        preprocessed_data = self.scaler.fit_transform(data)

        return pd.DataFrame(preprocessed_data, columns=data.columns)
