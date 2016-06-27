import pandas as pd

def read_MetroOut():
    df = pd.read_csv("./data_sets/mrtOut.csv")
    return df