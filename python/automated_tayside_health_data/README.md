# Automated Tayside Health Analysis

I structured my analysis as a repeatable workflow: load_data() imports the CSV, clean_data() coerces numeric fields, and the pipeline ends with descriptive_analysis() and inferential_analysis() for end‑to‑end output. Modular functions (e.g. overall_stats(), city_comparison(), smoking_analysis(), high_risk(), bmi_ttest(), diabetes_ttest(), gender_ttest(), chi_squared()) isolate tasks, making the code easier to test, maintain, and extend. A main() execution supports reproducibility by defining constants in one place and running the same sequence consistently. The script automatically generates descriptive statistics (summary measures, city BMI comparisons, smoking prevalence, risk clustering) and inferential statistics (t‑tests for BMI, diabetes risk, and blood pressure; chi‑square for associations), ensuring both exploratory and confirmatory insights are produced in a single run. Logging was also used throughout.

## Findings
**BMI Comparison**: A t-stat value < 0 indicates that Perth has a slightly lower average BMI compared to Dundee on average. However, the p value of 0.263(3d.p.) indicates that this difference is not statistically significant, so the BMI scores between the cities are likely similar.  
**Smokers vs Non-Smokers**: A very large t-stat value of 24.124(3d.p.) implies a substantial difference between snokers and non-smokers. This strongly suggests that smoking is linked to much higher diabetes risk scores compared to not smoking.  
**Gender and Systolic Blood Pressure**: A negative t-stat value of -15.476(3d.p.) suggests that females on average have lower systolic blood pressure than males. A very small p value confirms that this is a signifcant difference.  
**Smoking Status and Diabetes Risk**: The chi-square result suggests there is a significant relationship between smoking status and diabetes risk.  

## Summary Descriptive Statistics Output
<img width="1222" height="861" alt="image" src="https://github.com/user-attachments/assets/ce1f48aa-9870-4ced-abce-9b75898b6138" />


## Summary Inferential Statistics Output
<img width="679" height="365" alt="image" src="https://github.com/user-attachments/assets/10157fde-41c9-4f12-ac72-bcf0a7c3d7d0" />
