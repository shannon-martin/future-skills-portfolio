# Testing in Python: Tay Cities Pollution Data Analysis
My 'tayPollutionAnalysis.pynb' notebook analyses the Tay Cities Sewage dataset, which records pollution levels across cities and rivers in the Tay region of Scotland between 2010 and 2020.

The aim was to build a reliable, testable data pipeline that moves from raw data through to cleaned outputs, recursive analysis, mathematical prediction, and visualisation. Testing has been included to confirm each function works correctly.


## Visualisations
3 charts are generated to display different aspects of the dataset. The bar chart shows average pollution per river, sorted highest to lowest with colour intensity reflecting the value. The line graph overlays historical pollution levels with Fibonacci-based predictions, with a vertical line marking where recorded data ends and projections begin. The histogram shows the overall distribution of pollution values across the dataset, with overlayed mean and median for visual clarity.

### Average Sewage Levels per River
A bar chart visualising the average sewage levels per river, revealing that the Elricht has the highest average sewage levels at 36.8, and Leven has the lowest at 34.4.


### Predicted Contamination Trends per City
Line chart showing the historical and predicted pollution levels using Fibonacci trend modelling.

### Distribution of Pollution Levels
Histogram showing the distribution of pollution values accross the data.


## Functions
load_data()  
Reads the CSV file into a DataFrame and validates its structure before any processing begins. The function checks that the file exists and that all required columns are present, raising an error immediately if either check fails. This prevents corrupted or incomplete data from causing issues later in the pipeline.

clean_data()  
Standardises the dataset to ensure consistency before analysis. River names are converted to lowercase with whitespace removed so that the same river is not treated as multiple different entries. Pollution levels and measurement years are converted to the correct numeric types, and any rows with missing or duplicate values are removed.

recursive_average()  
Calculates the average pollution level for each river using a recursive function rather than a built-in method. The function moves through the records one at a time, adding the total and count for a given river, then divides at the end to produce the average.

fibonacci_pred()  
Uses a recursive Fibonacci function to predict future Contaminant_Index values. The Contaminant_Index column in the dataset already follows a Fibonacci sequence, so the function extends the existing pattern forward 5 years.

save_data()  
Saves the cleaned DataFrame to a CSV file. Warns if the file already exists and will be overwritten.


## Tests
Each function has its own test: load, clean, recursive average, Fibonacci, and visualisations are all verified against known inputs with expected outputs. I used assert statements and logging throughout, although I have been learning how to use the pytest framework also.

TEST 1: Load Data  
TEST 2: Clean Data  
TEST 3: Recursion  
TEST 4: Fibonacci  
TEST 5: Visualisations  
TEST 6: Saving  

Output showing all tests passed:  

<img width="961" height="162" alt="image" src="https://github.com/user-attachments/assets/e7108114-c860-49b5-892f-d2d456c75d64" />

