import pandas as pd
import re

from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


# CONSTANTS
# cols to be processed with cleaning/filtering functions
CAP_COLS = ['site_address', 'owner_developer']
DATE_COLS = ['year_site_added', 'last_planning_approval_date', 'date_completed_expired']
YEAR_COLS = ['year_24_25', 'year_25_26', 'year_26_27', 'year_27_28']
NUMERIC_COLS = ['site_capacity', 'bw_plots_written_off', 'no_of_houses', 'no_of_flats','plots_completed_in_survey_year', 'total_completions', 
                'units_to_build','year_24_25', 'year_25_26', 'year_26_27', 'year_27_28','year_28_29', 'year_29_30', 'year_30_31', 'year_31_32',
                'year_32_33', 'year_33_34', 'later_years', 'total_programmed','site_area_ha', 'easting', 'northing', 'shape_area', 'shape_length']
INFO_COLS = ['site_address', 'owner_developer', 'tenure_type', 'site_capacity', 'site_status']

# output filename
OUTPUT_FILE = 'cleanedHousingSites.csv'

# regex to help clean the mixed date formats (UK/US)
AMPMTIME_REGEX = re.compile(r"\s+\d{1,2}:\d{2}(:\d{2})?\s*(?:AM|PM)?$", re.IGNORECASE)
AMPM_REGEX = r"\b(?:AM|PM)\b"

# VARIABLES
# get root dir containing script
root = Path(__file__).parent.resolve()

# get the data folder relative to the root directory
data_dir = root / 'data'

csv_file = data_dir / 'housingSites.csv'

# newline
nl = "\n"


# HELPER FUNCTIONS
def strip_time(s: pd.Series) -> pd.Series:
    """strip the time from US dates"""
    return s.str.replace(AMPMTIME_REGEX, "", regex=True)

def clean_text(text: str) -> str:
    """Remove extra spaces and apply capitalisation."""
    if isinstance(text, str):
        return text.strip().title()
    return text

def fix_mixed_dates(col):
    """Converts mixed UK/US date formats by checking if 'AM/PM' is present,
        is so attemts US parsing, else UK parsing."""
    s = col.astype(str).str.strip()

    # mask - rows that contain AM or PM
    ampm = s.str.contains(AMPM_REGEX, case=False, regex=True)

    # remove trailing time so formats work
    s_clean = strip_time(s)

    # for AM/PM rows, use US (month-first)
    us = pd.to_datetime(s_clean.where(ampm), dayfirst=False, format='%m/%d/%Y', errors="coerce")

    # for all other rows, use UK (day-first)
    uk = pd.to_datetime(s_clean.where(~ampm), dayfirst=True, format='%d/%m/%Y', errors="coerce")

    # combine the two results
    return us.fillna(uk)

# CLEANING FUNCTIONS
def standardise_columns(df):
    """Normalises column names by:
    - converting to lowercase
    - stripping leading/trailing spaces
    - replacing spaces and punctuation with underscores
    - collapsing multiple underscores
    - normalising slashes like 'Year 24/25' to 'year_24_25'
    - removing double underscores like Shape__Area to shape_area"""

    def clean(col):
        col = col.strip().lower()

        # Replace slashes with underscore (Year 24/25)
        col = col.replace("/", "_")

        # Replace any non-alphanumeric with underscore
        col = re.sub(r"[^a-z0-9]+", "_", col)

        # Collapse multiple underscores
        col = re.sub(r"_+", "_", col)

        # Remove leading/trailing underscores
        col = col.strip("_")

        return col

    df = df.copy()
    df.columns = [clean(c) for c in df.columns]
    logging.info(f"Standardised column names.")
    return df

def load_data(input_path: str) -> pd.DataFrame:
    """Loads the imput file into a DataFrame."""
    logging.info(f"Loading data from: {input_path}")
    if not Path.exists(input_path):
        logging.error(f"Input file not found: {input_path}")
        
    df = pd.read_csv(input_path)
    logging.info(f"{input_path} succesfully loaded.")
    
    # log missing values, only log columns where missing values are present
    logging.info(f"Missing values are present in columns:{nl}{df.isna().sum()[df.isna().sum() > 0]}")
    return df

def clean_data(df: pd.DataFrame, cols_to_standardise: list, numeric_cols: list, date_cols: list) -> pd.DataFrame:
    """Sandardise capitalisation, convert numeric columns, and fix date formats."""
    df = df.copy()
    # standardise capitalisation
    for col in cols_to_standardise:
        df[col] = df[col].apply(clean_text)
    logging.info(f"Standardised capitalisation and stripped whitespace from {cols_to_standardise} columns.")
    
    # convert numeric columns
    col_types_bef = df.dtypes.copy()
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    # for col in df.columns:
    #     df[col] = pd.to_numeric(df[col], errors='coerce')
    col_types_aft = df.dtypes 
    numeric_converted = col_types_bef.index[col_types_bef.ne(col_types_aft)].tolist()
    if numeric_converted:
        logging.info(f"Converted {numeric_converted} to numeric.")

    # fix date formats
    for col in date_cols:
        if col in df.columns:
            df[col] = fix_mixed_dates(df[col])
        else:
            logging.warning(f"Missing date column, skipping: {col}")

    logging.info(f"Converted {date_cols} columns into datetime format.")
        
    return df

# FILTER/METRICS FUNCTIONS
def filter_sites(
    df: pd.DataFrame,
    status: str | None = None,
    greenfield_brownfield: str | None = None,
    min_capacity: float | None = None,
    min_size: float | None = None,
    tenure: str | None = None,
    owner_contains: str | None = None,
    address_contains: str | None = None) -> pd.DataFrame:
    """Return a subset of sites matching chosen criteria.
    All parameters are optional; only those provided are applied."""
    df = df.copy()

    if status and 'site_status' in df.columns: 
        df["site_status"] = df["site_status"].astype("string").str.strip()
        df = df[df["site_status"].str.casefold() == status.strip().casefold()]
        logging.info(f"Fltered by 'Site status' == {status}.")

 
    if greenfield_brownfield and 'greenfield_brownfield' in df.columns:
        df['greenfield_brownfield'] = df['greenfield_brownfield'].astype('string').str.strip()
        df = df[df['greenfield_brownfield'].str.casefold() == greenfield_brownfield.strip().casefold()]
        logging.info(f"Filtered by 'Greenfield/Brownfield' == {greenfield_brownfield}.")


    if min_capacity is not None and 'site_capacity' in df.columns:
        df = df[df['site_capacity'] >= float(min_capacity)]
        logging.info(f"Fltered by 'Site capacity' >= {min_capacity}.")
        
    if min_size is not None and 'site_area_ha' in df.columns:
        df = df[df['site_area_ha'] >= float(min_size)]
        logging.info(f"Fltered by 'Site area (ha)' >= {min_size}.")
        

    if tenure and 'tenure_type' in df.columns:
        df['tenure_type'] = df['tenure_type'].astype('string').str.strip()
        df = df[df['tenure_type'].str.casefold() == tenure.strip().casefold()]
        logging.info(f"Filtered by 'Tenure type' == {tenure}.")

        
    if owner_contains and 'owner_developer' in df.columns:
        df = df[df['owner_developer'].str.contains(owner_contains, case=False, na=False)]
        logging.info(f"Fltered by 'Owner/Developer' containing '{owner_contains}'.")
        
    if address_contains and 'site_address' in df.columns:
        df = df[df['site_address'].str.contains(address_contains, case=False, na=False)]
        logging.info(f"Fltered by 'Site address' == '{address_contains}'.")
        
    return df

def top_sites_by_capacity(df: pd.DataFrame,  info_cols, n: int = 10) -> pd.DataFrame:
    """Return top n sites by capacity, (default: 10)"""
    cols = [c for c in info_cols if c in df.columns]
    out = df.copy()
    out = out.sort_values(by='site_capacity', ascending=False, na_position='last')
    return out[cols].head(n)


def calculate_metrics(df: pd.DataFrame, year_cols: list) -> pd.DataFrame:
    # total site capacity
    logging.info(f"Calculating site capacity...")
    total_capacity = df['site_capacity'].sum()
    print(f"Total site capacity is {total_capacity}.{nl}")

    # projected builds for 2024-2027
    logging.info(f"Calculating projected builds for year(s): {year_cols}.")
    total_units = 0
    for col in year_cols:
        total_units += df[col].sum()
    print(f"The total projected units for 2024-2027 is: {total_units}.{nl}")

    # cumulative capacity per tenure type
    logging.info(f"Calculating cumulative capacity per tenure type...")
    tenure_capacity = df.groupby('tenure_type')['site_capacity'].sum().to_dict()
    print(f"The cumulative capacity per tenure type is: {tenure_capacity}. {nl}")

    large_sites = filter_sites(df, min_size=5)
    print(f"The top 5 largest sites are: {nl}")
    print(f"{top_sites_by_capacity(large_sites, INFO_COLS, 5)}{nl}")

    # under construction
    df_uc = filter_sites(df, status='Under Construction')
    print(f"There are {len(df_uc)} sites currently under construction totalling {df_uc['site_capacity'].sum()} units. {nl}")

    # greenfield vs brownfield
    gb = []
    for n in ['Greenfield', 'Brownfield']:
        sub = filter_sites(df, greenfield_brownfield=n)
        gb.append({'type': n, 'sites': len(sub), 'capacity': sub['site_capacity'].sum()})
    print(f"Capacity of Geenfield vs Brownfield sites:{nl}{gb}{nl}")

# SAVE CLEANED DATA
def save_data(df: pd.DataFrame, output_filename: str):
    """Save cleaned dataset."""
    if Path(output_filename).exists():
       logging.error(f"Output filename '{output_filename}' already exists.")
    
    df.to_csv(output_filename, index=False)
    logging.info(f"Cleaned and transformed file saved as {output_filename}.")


def main():
    df = load_data(csv_file)
    df = standardise_columns(df)
    df_clean = clean_data(df, CAP_COLS, NUMERIC_COLS, DATE_COLS)
    calculate_metrics(df_clean, YEAR_COLS)
    save_data(df_clean, OUTPUT_FILE)

if __name__ == "__main__":
    main()