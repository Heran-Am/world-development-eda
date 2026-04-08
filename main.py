from src.load_data import load_data, explore
from src.clean_data import clean_data
from src.visualize import (
    plot_gdp_vs_life_expectancy,
    plot_life_expectancy_trend,
    plot_co2_top_countries,
    plot_infant_mortality_vs_health,
    plot_correlation_heatmap
)
import pandas as pd

if __name__ == "__main__":
    # Step 1: Load
    df = load_data("data/wdi_raw.csv")

    # Step 2: Clean
    df_clean = clean_data(df)
    df_clean.to_csv("data/wdi_clean.csv", index=False)

    # Step 3: Visualize
    df_viz = pd.read_csv("data/wdi_clean.csv")
    plot_gdp_vs_life_expectancy(df_viz)
    plot_life_expectancy_trend(df_viz)
    plot_co2_top_countries(df_viz)
    plot_infant_mortality_vs_health(df_viz)
    plot_correlation_heatmap(df_viz)

    print("\n🎉 All done! Check the outputs/ folder for your charts.")