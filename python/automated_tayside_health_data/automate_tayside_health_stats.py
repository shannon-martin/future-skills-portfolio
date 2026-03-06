import pandas as pd
from scipy import stats

from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


## CONSTANTS
# get root dir containing script
ROOT = Path(__file__).parent.resolve()
# get the data folder relative to the root directory
DATA_DIR = ROOT / 'data'

# data file
CSV_FILE = DATA_DIR / 'taysideHealthData.csv'
OUTPUT_FILE = DATA_DIR / 'cleanedTaysideHealthData.csv'

# newline
NL = '\n'

NUMERIC_COLS = ['Age', 'BMI', 'SystolicBP', 'DiastolicBP', 'Cholesterol', 'PhysicalActivityHours', 'DiabetesRiskScore']
HEALTH_INDICATOR_COLS = ['BMI', 'SystolicBP', 'DiastolicBP', 'Cholesterol', 'PhysicalActivityHours', 'DiabetesRiskScore']
HIGH_RISK_INDICATORS = {'Obese':            {'BMI': 30},
                        'Hypertensive':     {'SystolicBP': 140},
                        'HighDiabetesRisk': {'DiabetesRiskScore': 8},
                        }
BMI_TTEST_CITIES = ['Perth', 'Dundee']
GENDER_COMPARISON_INDICATOR = 'SystolicBP'
CHI_SQUARE_VALUES = ['SmokingStatus', 'DiabetesRiskScore']

## FORMATTING
# formats to %
def fmt_pct(x):
    return f"{x:.2f}%"

# formats to 2 d.p.
def fmt_2dp(x):
    return f"{x:.2f}"


## IMPORT
def load_data(input_path) -> pd.DataFrame:
    logging.info(f"Loading data from: {input_path}")
    if not Path.exists(input_path):
        logging.error(f"Input file not found: {input_path.name}")
    df = pd.read_csv(input_path)
    logging.info(f"{input_path.name} has been loaded successfully.")
    return df

## CLEAN
def clean_data(df: pd.DataFrame, numeric_cols: list) -> pd.DataFrame:
    logging.info("Cleaning data...")
    df[numeric_cols].apply(pd.to_numeric)
    logging.info(f"Columns: {numeric_cols} have been successfully converted to numeric type.")
    return df

## SAVE
# SAVE CLEANED DATA
def save_data(df: pd.DataFrame, output_file: Path):
    """Save cleaned dataset."""
    if Path(output_file).exists():
       logging.error(f"Output filename '{output_file}' already exists.")
    
    df.to_csv(output_file, index=False)
    logging.info(f"Cleaned and transformed file saved as {output_file}.")

## DESCRIPTIVE STATS
# Overall Descriptive Statistics
def overall_stats(df: pd.DataFrame):
    logging.info("Generating overall descriptive statistics...")
    return df.describe()

# Compare Indicators by City
def city_comparison(df: pd.DataFrame, health_indicator_cols: list) -> pd.DataFrame:
    logging.info("Generating city comparisons...")
    comparison = df.groupby('City')[health_indicator_cols].mean()
    return comparison.map(fmt_2dp)

# Smoking Prevelence
def smoking_analysis(df: pd.DataFrame):
    logging.info("Generating smoking analysis...")
    overall = df['SmokingStatus'].value_counts(normalize=True) * 100
    by_city = pd.crosstab(df['City'], df['SmokingStatus'], normalize='index') * 100
    return overall.map(fmt_pct), by_city.map(fmt_pct)

# Identify High-Risk Clusters
def high_risk(df: pd.DataFrame, risk_indicators: dict):
    logging.info("Identifying high-risk clusters...")
    df = df.copy()
    
    for risk, indicator in risk_indicators.items():
        col, value = next(iter(indicator.items()))
        df[risk] = df[col] >= value
        
    risk_summary = df.groupby('City')[list(risk_indicators.keys())].sum()
    return risk_summary

# Summary Descriptive Analysis
def descriptive_analysis(df: pd.DataFrame):
    logging.info("Conducting descriptive analysis...")
    print(f"OVERALL STATISTICS{NL}{overall_stats(df)}{NL}")
    print(f"CITY COMPARISON{NL}{city_comparison(df, HEALTH_INDICATOR_COLS)}{NL}")
    overall, by_city = smoking_analysis(df)
    print(f"SMOKING ANALYSIS")
    print(f"Overall Smoking %: {NL}{overall.to_string()}{NL}% by City: {NL}{by_city.to_string()}{NL}")
    print(f"HIGH RISK CLUSTERS{NL}{high_risk(df, HIGH_RISK_INDICATORS)}{NL}")


## INFERENTIAL STATS
# BMI Comparison
def bmi_ttest(df: pd.DataFrame, bmi_ttest_cities: list):
    logging.info(f"Determining diference between {bmi_ttest_cities[0]} and {bmi_ttest_cities[1]}...")
    h0 = df[df['City'] == bmi_ttest_cities[0]]['BMI']
    h1 = df[df['City'] == bmi_ttest_cities[1]]['BMI']

    t_stat, p_value = stats.ttest_ind(h0, h1)
    return t_stat, p_value

# Diabetes Risk: Smokers vs Non-Smokers
def diabetes_ttest(df: pd.DataFrame):
    logging.info("Determining diabetes risk between smokers and non-smokers using t test...")
    smokers = df[df['SmokingStatus'] == 'Yes']['DiabetesRiskScore']
    non_smokers = df[df['SmokingStatus'] == 'No']['DiabetesRiskScore']

    t_stat, p_value = stats.ttest_ind(smokers, non_smokers)
    return t_stat, p_value

# Comparison Between Gender
def gender_ttest(df: pd.DataFrame, indicator='SystolicBP'):
    logging.info(f"Comparing {indicator} between genders using t test... ")
    female = df[df['Gender'] == 'Female'][indicator]
    male = df[df['Gender'] == 'Male'][indicator]

    t_stat, p_value = stats.ttest_ind(female, male)
    return t_stat, p_value

# Chi-Square
def chi_squared(df: pd.DataFrame, variables: list):
    logging.info(f"Accessing association between {variables[0]} and {variables[1]} using chi-square...")
    contingency = pd.crosstab(df[variables[0]], df[variables[1]])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    return chi2, p

# Summary Inferential Analysis
def inferential_analysis(df: pd.DataFrame):
    logging.info(f"Conducting inferential analysis...{NL}")

    bmi_t_stat, bmi_p_value = bmi_ttest(df, BMI_TTEST_CITIES)
    print(f"{NL}Comparison to determine the diference in BMI between {BMI_TTEST_CITIES[0]} - {BMI_TTEST_CITIES[1]} shows:{NL}t_stat= {bmi_t_stat} and p= {bmi_p_value}{NL}") 

    diabetes_t_stat, diabetes_p_value = diabetes_ttest(df)
    print(f"{NL}The diabetes risk between smokers and non-smokers: {NL}t_stat= {diabetes_t_stat}, p= {diabetes_p_value}{NL}")

    gender_t_stat, gender_p_value = gender_ttest(df, GENDER_COMPARISON_INDICATOR)
    print(f"{NL}The gender comparison for {GENDER_COMPARISON_INDICATOR} shows:{NL}t_stat= {gender_t_stat} and p= {gender_p_value}{NL}")
    
    chi2, p = chi_squared(df, CHI_SQUARE_VALUES)
    print(f"{NL}Accessing the association between {CHI_SQUARE_VALUES[0]} and {CHI_SQUARE_VALUES[1]} shows:{NL}chi2= {chi2} and p= {p}")


def main():
    df = load_data(CSV_FILE)
    clean_data(df, NUMERIC_COLS)
    #save_data(df, OUTPUT_FILE)
    descriptive_analysis(df)
    inferential_analysis(df)

if __name__ == "__main__":
    main()