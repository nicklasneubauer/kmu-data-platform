import pandas as pd

def clean_sales_data(df):
    df = df.dropna()
    df['amount'] = df['amount'].astype(float)
    return df
