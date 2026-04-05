from src.load_data import load_data, explore

if __name__ == "__main__":
    df = load_data("data/wdi_raw.csv")
    explore(df)