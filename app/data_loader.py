import pandas as pd
import os

def load_imdb_dataset():
    dataset_path = os.path.join(os.path.dirname(__file__), "..", "IMDB_Dataset", "IMDB Dataset.csv")
    df = pd.read_csv(dataset_path)
    return df

