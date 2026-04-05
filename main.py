from src.load_data import load_data, explore
from src.clean_data import clean_data

if __name__ == "__main__":
    df = load_data("data/wdi_raw.csv")
    explore(df)
    df_clean = clean_data(df)
    
    # Save cleaned data
    df_clean.to_csv("data/wdi_clean.csv", index=False)
    print("\n✅ Cleaned data saved to data/wdi_clean.csv")