import pandas as pd

def load_data():
    df = pd.read_csv("data/clustered_songs.csv")
    return df
