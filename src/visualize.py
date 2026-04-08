import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Make outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def plot_gdp_vs_life_expectancy(df):
    """Scatter plot: GDP per capita vs Life Expectancy"""
    fig, ax = plt.subplots()
    
    # Use 2019 data (last year before COVID)
    df_2019 = df[df['year'] == 2019].dropna(subset=['gdp_per_capita', 'life_expectancy'])
    
    scatter = ax.scatter(
        df_2019['gdp_per_capita'],
        df_2019['life_expectancy'],
        c=df_2019['gdp_per_capita'],
        cmap='viridis',
        alpha=0.7,
        s=60
    )
    
    ax.set_xscale('log')
    ax.set_xlabel('GDP per Capita (USD, log scale)', fontsize=12)
    ax.set_ylabel('Life Expectancy (years)', fontsize=12)
    ax.set_title('GDP per Capita vs Life Expectancy (2019)', fontsize=14)
    plt.colorbar(scatter, label='GDP per Capita')
    plt.tight_layout()
    plt.savefig('outputs/gdp_vs_life_expectancy.png', dpi=150)
    plt.close()
    print("✅ Saved: gdp_vs_life_expectancy.png")


def plot_life_expectancy_trend(df):
    """Line chart: Global average life expectancy over time"""
    fig, ax = plt.subplots()
    
    trend = df.groupby('year')['life_expectancy'].mean().reset_index()
    
    ax.plot(trend['year'], trend['life_expectancy'],
            color='steelblue', linewidth=2.5, marker='o', markersize=4)
    
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Average Life Expectancy (years)', fontsize=12)
    ax.set_title('Global Average Life Expectancy Over Time (2000–2022)', fontsize=14)
    plt.tight_layout()
    plt.savefig('outputs/life_expectancy_trend.png', dpi=150)
    plt.close()
    print("✅ Saved: life_expectancy_trend.png")


def plot_co2_top_countries(df):
    """Bar chart: Top 15 countries by average CO2 per capita"""
    fig, ax = plt.subplots()
    
    top_co2 = (df.groupby('country')['co2_per_capita']
               .mean()
               .sort_values(ascending=False)
               .head(15)
               .reset_index())
    
    sns.barplot(data=top_co2, x='co2_per_capita', y='country',
            hue='country', palette='Reds_r', legend=False, ax=ax)
    
    ax.set_xlabel('Average CO2 per Capita (t CO2e)', fontsize=12)
    ax.set_ylabel('')
    ax.set_title('Top 15 Countries by CO2 Emissions per Capita (2000–2022)', fontsize=14)
    plt.tight_layout()
    plt.savefig('outputs/co2_top_countries.png', dpi=150)
    plt.close()
    print("✅ Saved: co2_top_countries.png")


def plot_infant_mortality_vs_health(df):
    """Scatter: Health expenditure vs Infant Mortality"""
    fig, ax = plt.subplots()
    
    df_2019 = df[df['year'] == 2019].dropna(
        subset=['health_expenditure', 'infant_mortality'])
    
    ax.scatter(
        df_2019['health_expenditure'],
        df_2019['infant_mortality'],
        alpha=0.6, color='tomato', s=60
    )
    
    ax.set_xscale('log')
    ax.set_xlabel('Health Expenditure per Capita (USD, log scale)', fontsize=12)
    ax.set_ylabel('Infant Mortality Rate (per 1,000 births)', fontsize=12)
    ax.set_title('Health Spending vs Infant Mortality (2019)', fontsize=14)
    plt.tight_layout()
    plt.savefig('outputs/infant_mortality_vs_health.png', dpi=150)
    plt.close()
    print("✅ Saved: infant_mortality_vs_health.png")


def plot_correlation_heatmap(df):
    """Heatmap of correlations between all indicators"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    cols = ['gdp_per_capita', 'life_expectancy', 'co2_per_capita',
            'health_expenditure', 'electric_power',
            'infant_mortality', 'school_enrollment']
    
    corr = df[cols].corr()
    
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, ax=ax, square=True)
    
    ax.set_title('Correlation Between Development Indicators', fontsize=14)
    plt.tight_layout()
    plt.savefig('outputs/correlation_heatmap.png', dpi=150)
    plt.close()
    print("✅ Saved: correlation_heatmap.png")


if __name__ == "__main__":
    df = pd.read_csv("data/wdi_clean.csv")
    plot_gdp_vs_life_expectancy(df)
    plot_life_expectancy_trend(df)
    plot_co2_top_countries(df)
    plot_infant_mortality_vs_health(df)
    plot_correlation_heatmap(df)
    print("\n🎉 All charts saved to outputs/")