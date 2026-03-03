# Automated Housing Data Analysis
The goal was to build a repeatable, automated pipeline that imports a raw housing sites CSV, standardises and cleans it, calculates a few useful metrics, and then saves a cleaned output ready for analysis. To make that reliable, I organised the logic into small, testable functions, wrapped execution under a main() function, and added logging to make each step observable when it runs unattended. Data was obtained from [Dundee Open Data Portal](https://data.dundeecity.gov.uk/search?tags=housing%2520sites).

The script flows in a clear, linear sequence:
1. **Loads input** by reading 'housingSites.csv' from the known 'data/' directory.  
2. **Standardises column names** by lowercasing, replacing spaces with underscores, and removing punctuation to ensure consistent formatting for later steps.  
3. **Cleans values** by:  
   - normalising capitalisation and trimming whitespace for key identifier fields,  
   - safely converting numeric values using 'errors=coerce',  
   - resolving mixed UK/US date formats, including rows containing AM/PM timestamps.  
4. **Filters and calculates metrics** using utility functions that generate capacity totals, projections, tenure breakdowns, largest sites, and other summary summaries.  
5. **Saves output** to a single file: 'cleanedHousingSites.csv'.  
6. **Automates execution** through a 'main()' function guarded by 'if __name__ == "__main__":', enabling scheduled runs or simple one‑liner execution.


## Logging

I configured logging and used logging.info(), logging.warning(), and logging.error() messages to narrate each stage: loading, standardising columns, type conversions, date fixes, filters, and saving. In an automated context, these log lines make it possible to diagnose failures (missing files, unexpected changes) or confirm that each step completed. Compared to print statements, logs can later be routed to files or monitoring tools without changing code flow.


## Functions used

### Single purpose helpers
clean_text() trims and applies title casing. 
strip_time() removes trailing time components before parsing US dates. 
fix_mixed_dates()  detects AM/PM and applies US month first parsing for those cases, with UK day first parsing otherwise, then merges the results.

### Core cleaning
standardise_columns() converts all column names into a standard format.
clean_data() wraps capitalisation, numeric coercion, and date parsing into a single step. 

### Analysis
filter_sites() lets me slice by status, greenfield/brownfield, minimum capacity/size, tenure, or string contains. These filters enable focused checks without rewriting. 
top_sites_by_capacity() is a simple helper to return top sites by their capacity.
calculate_metrics()prints quick metrics such as total capacity, short term projections, tenure capacity, largest sites, and counts under construction. 

### IO
load_data() read file and initial diagnostics (like reporting missing values).
save_data() writes the cleaned data to CSV.

## Example output
<img width="1308" height="740" alt="image" src="https://github.com/user-attachments/assets/cb18600c-2590-40d2-a760-556db1703369" />

