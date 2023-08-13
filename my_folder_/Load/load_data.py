import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

# Load bankruptcy data
loader = DataLoader("my_folder_/Data/data.csv")
data = loader.load_data()