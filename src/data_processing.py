import pandas as pd
from typing import List

from config import FEATURES_TO_REMOVE

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    print(f"Excel file loaded, format: {df.shape}")

    # use try e except File not found error

    print(f"Columns to be removed: {FEATURES_TO_REMOVE}")
    df = df.drop(columns=FEATURES_TO_REMOVE, errors='ignore')
    print(f"Columns removed, new format: {df.shape}")

    if "Data de cadastro" in df.columns:
        df['Data de cadastro'] = pd.to_datetime(df['Data de cadastro'], dayfirst=True)
        print(f"Existing 'Data de cadastro' converted to datetime.")
    
    print("End of Data Processing")
    return df

