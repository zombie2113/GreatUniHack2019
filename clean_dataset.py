import pandas as pd

def clean_data():
    data = pd.read_csv('export_simple.csv')
    data[data['url'].str.contains("imgur")]

    print("Now data has got -> " + data.shape)