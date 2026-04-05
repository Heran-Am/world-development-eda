import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    # Read the CSV
    df = pd.read_csv(path, header=0)
    
    # Drop the last 3 rows (metadata footer)
    df = df[:-3]
    
    # Rename columns to short clean names
    df.columns = [
        'year', 'year_code', 'country', 'country_code',
        'co2_per_capita', 'gdp_per_capita', 'life_expectancy',
        'health_expenditure', 'electric_power', 'infant_mortality',
        'population', 'school_enrollment'
    ]
    
    # Convert year and numeric columns to proper types
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    numeric_cols = ['co2_per_capita', 'gdp_per_capita', 'life_expectancy',
                    'health_expenditure', 'electric_power', 'infant_mortality',
                    'population', 'school_enrollment']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    # Drop rows where both country and year are missing
    df = df.dropna(subset=['country', 'year'])
    
    return df

def explore(df: pd.DataFrame) -> None:
    print("=" * 50)
    print("SHAPE:", df.shape)
    print("\nCOLUMNS:", df.columns.tolist())
    print("\nFIRST 5 ROWS:")
    print(df.head())
    print("\nDATA TYPES:")
    print(df.dtypes)
    print("\nMISSING VALUES (%):")
    missing = (df.isnull().sum() / len(df) * 100).round(2)
    print(missing)
    print("\nBASIC STATS:")
    print(df.describe())

if __name__ == "__main__":
    df = load_data("data/wdi_raw.csv")
    explore(df)