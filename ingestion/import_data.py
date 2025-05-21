import pandas as pd
import requests

def load_csv(path="ingestion/example_sales.csv"):
    """Load sales data from local CSV file."""
    return pd.read_csv(path)

def fetch_api_data(url="https://jsonplaceholder.typicode.com/posts"):
    """Fetch dummy API data as placeholder (e.g. blog posts)."""
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())

if __name__ == "__main__":
    df_csv = load_csv()
    print("✅ Loaded CSV:")
    print(df_csv.head())

    df_api = fetch_api_data()
    print("\n✅ Fetched API Data:")
    print(df_api.head())
