import pandas as pd

def validate_csv(file_path):
    df = pd.read_csv(file_path)

    print("Row count:", len(df))

    if df.isnull().sum().sum() > 0:
        print("Warning: Null values detected")

    duplicates = df[df.duplicated()]
    if len(duplicates) > 0:
        print("Duplicate records detected")

    return df