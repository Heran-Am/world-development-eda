import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Drop columns we don't need
    df = df.drop(columns=['year_code'])
    
    # 2. Convert year to integer
    df['year'] = df['year'].astype(int)
    
    # 3. Remove aggregates (World Bank includes regions, not just countries)
    aggregates = [
        'World', 'Africa Eastern and Southern', 'Africa Western and Central',
        'Arab World', 'Caribbean small states', 'Central Europe and the Baltics',
        'Early-demographic dividend', 'East Asia & Pacific',
        'East Asia & Pacific (excluding high income)',
        'East Asia & Pacific (IDA & IBRD countries)',
        'Euro area', 'Europe & Central Asia',
        'Europe & Central Asia (excluding high income)',
        'Europe & Central Asia (IDA & IBRD countries)',
        'European Union', 'Fragile and conflict affected situations',
        'Heavily indebted poor countries (HIPC)', 'High income',
        'IBRD only', 'IDA & IBRD total', 'IDA blend', 'IDA only',
        'IDA total', 'Late-demographic dividend',
        'Latin America & Caribbean',
        'Latin America & Caribbean (excluding high income)',
        'Latin America & the Caribbean (IDA & IBRD countries)',
        'Least developed countries: UN classification',
        'Low & middle income', 'Low income', 'Lower middle income',
        'Middle East & North Africa',
        'Middle East & North Africa (excluding high income)',
        'Middle East & North Africa (IDA & IBRD countries)',
        'Middle income', 'North America', 'Not classified',
        'OECD members', 'Other small states',
        'Pacific island small states', 'Pre-demographic dividend',
        'Small states', 'South Asia', 'South Asia (IDA & IBRD)',
        'Sub-Saharan Africa', 'Sub-Saharan Africa (excluding high income)',
        'Sub-Saharan Africa (IDA & IBRD countries)',
        'Upper middle income', 'Upper middle income'
    ]
    df = df[~df['country'].isin(aggregates)]
    
    # 4. Fill missing values with the country's own median across years
    numeric_cols = ['co2_per_capita', 'gdp_per_capita', 'life_expectancy',
                    'health_expenditure', 'electric_power',
                    'infant_mortality', 'population', 'school_enrollment']
    
    df[numeric_cols] = df.groupby('country')[numeric_cols].transform(
        lambda x: x.fillna(x.median())
    )
    
    # 5. Add a continent/region column for richer analysis
    region_map = {
        'AFG':'South Asia','BGD':'South Asia','BTN':'South Asia',
        'IND':'South Asia','LKA':'South Asia','MDV':'South Asia',
        'NPL':'South Asia','PAK':'South Asia',
        'BRA':'Latin America','ARG':'Latin America','COL':'Latin America',
        'CHL':'Latin America','MEX':'Latin America','PER':'Latin America',
        'VEN':'Latin America','ECU':'Latin America','BOL':'Latin America',
        'PRY':'Latin America','URY':'Latin America',
        'USA':'North America','CAN':'North America',
        'DEU':'Europe','FRA':'Europe','GBR':'Europe','ITA':'Europe',
        'ESP':'Europe','NLD':'Europe','SWE':'Europe','NOR':'Europe',
        'CHE':'Europe','POL':'Europe','BEL':'Europe','AUT':'Europe',
        'CHN':'East Asia','JPN':'East Asia','KOR':'East Asia',
        'TWN':'East Asia','HKG':'East Asia','MNG':'East Asia',
        'NGA':'Sub-Saharan Africa','ETH':'Sub-Saharan Africa',
        'KEN':'Sub-Saharan Africa','GHA':'Sub-Saharan Africa',
        'TZA':'Sub-Saharan Africa','ZAF':'Sub-Saharan Africa',
        'UGA':'Sub-Saharan Africa','MOZ':'Sub-Saharan Africa',
        'SAU':'Middle East & North Africa','EGY':'Middle East & North Africa',
        'IRN':'Middle East & North Africa','IRQ':'Middle East & North Africa',
        'MAR':'Middle East & North Africa','DZA':'Middle East & North Africa',
        'RUS':'Europe & Central Asia','KAZ':'Europe & Central Asia',
        'UZB':'Europe & Central Asia','TUR':'Europe & Central Asia',
    }
    df['region'] = df['country_code'].map(region_map).fillna('Other')
    
    print("✅ Cleaning done!")
    print("SHAPE after cleaning:", df.shape)
    print("\nMISSING VALUES after cleaning (%):")
    print((df.isnull().sum() / len(df) * 100).round(2))
    
    return df

if __name__ == "__main__":
    from load_data import load_data
    df = load_data("../data/wdi_raw.csv")
    df_clean = clean_data(df)
    print(df_clean.head())