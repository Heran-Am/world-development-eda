import pandas as pd 
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, skiprows=4)
    return df

def explore(df: pd.DataFrame) -> None:
    print("=" * 50)
    print("SHAPE:", df.shape)
    print("\nCOLUMNS:")
    print(df.columns.tolist())
    print("\nFIRST 5 ROWS:")
    print(df.head())
    print("\nMISSING VALUES (top 10):")
    print(df.isnull().sum().sort_values(ascending=False).head(10))
    
if __name__ == "__main__":
    df = load_data("data/wdi_raw.csv")
    explore(df)