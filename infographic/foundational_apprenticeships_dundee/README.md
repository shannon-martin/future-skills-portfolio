<table>
  <tr>
    <td style="vertical-align: top; padding-right: 20px; min-width: 320px;">
      <h1>Foundational Apprenticeships in Dundee: Enrolment Comparison and Framework Gender Distribution Analysis</h1>
      <br></br>
      <strong>The Foundational Apprenticeship (FA) data was selected to explore statistics relating to enrolments for each Scottish local authority in comparison with Dundee enrolments, and trends relating to the gender distribution of each provided framework. This data is available in XLSX format as supplementary report tables and can be found on the Skills Development Scotland site published as ’FA Supplementary Tables 2023’ which accompany the ‘Foundation Apprenticeship Report 2023’. The data used for analysis is from sheets 1.1 ‘FA enrolments by framework and gender’ and 1.7 ‘FA enrolments by local authority’.</strong>
      <br/><br/>
      For this analysis, the questions explored were:
      <br/><br/>
      <ol>
        <li> How do Dundee’s FA enrolments compare to the average FA enrolments across Scotland?</li>
        <li> Has there been any notable change in the gender distribution of frameworks over the years?</li>
        <br/><br/>
      </ol>
    </td>
    <td style="vertical-align: top; text-align: right; width: 560px;">
      <img alt="Foundational Apprenticeships in Dundee Enrolment Comparison and Framework Gender Distribution" src="https://github.com/user-attachments/assets/84dd2e0c-14a2-4de6-891a-39e5b7ce01f1" />
           Foundational Apprenticeships in Dundee Infographic
    </td>
  </tr>
</table>


# Local Authority Enrolments Analysis
To explore question 1, central tendency, variability, and dispersion statistics were calculated using the built-in Excel functions AVERAGE(), MEDIAN(), MODE.SNGL(), STDEV.P(), QUARTILE.INC(), MIN(), and MAX(). The Range was calculated using Range=Max-Min, and the Interquartile Range (IQR) was calculated using IQR=Q3-Q1.


| Descriptive Statistic | Cohort 1 L6 | Cohort 2 L6 | Cohort 3 L6 2018 | Cohort 4 L6 2019 | L4/5 Pilot 2019 | Cohort 5 L6 2020 | L4/5 Pilot 2020 | Cohort 6 L6 2021 | L4/5 Pilot 2021 | Cohort 7 L6 2022 | L4/5 Pilot 2022 |
|-----------------------|-------------|--------------|-------------------|-------------------|------------------|-------------------|------------------|-------------------|-------------------|-------------------|------------------|
| Mean                  | 18          | 43           | 53                | 108               | 36               | 93                | 74               | 78                | 88                | 77                | 68               |
| Median                | 15          | 25           | 32                | 68                | 18               | 64                | 62               | 49                | 57                | 53                | 40               |
| Mode                  | 15          | 7            | 37                | 65                | 8                | 26                | 29               | 41                | 31                | 15                | 0                |
| SD                    | 9.78        | 53.54        | 49.93             | 98.27             | 51.48            | 78.12             | 64.09            | 80.86             | 72.81             | 87.61             | 84.94            |
| Min                   | 6           | 7            | 6                 | 6                 | 6                | 12                | 5                | 5                 | 18                | 5                 | 0                |
| Max                   | 47          | 239          | 216               | 458               | 198              | 361               | 231              | 420               | 257               | 480               | 350              |
| Range                 | 41          | 232          | 210               | 452               | 192              | 349               | 226              | 415               | 239               | 475               | 350              |
| Q1                    | 10.25       | 12           | 21                | 52.25             | 8                | 39.5              | 22               | 31.25             | 32.5              | 25                | 0                |
| Q3                    | 22.25       | 45           | 67                | 123.5             | 31.5             | 116.25            | 103              | 97                | 121.75            | 95                | 97.5             |
| IQR                   | 12          | 33           | 46                | 71.25             | 23.5             | 76.75             | 81               | 65.75             | 89.25             | 70                | 97.5             |


How do Dundee’s FA enrolments compare to the average for all local authorities?


| Local Authority | Cohort 1 L6 | Cohort 2 L6 | Cohort 3 L6 2018 | Cohort 4 L6 2019 | L4/5 Pilot 2019 | Cohort 5 L6 2020 | L4/5 Pilot 2020 | Cohort 6 L6 2021 | L4/5 Pilot 2021 | Cohort 7 L6 2022 | L4/5 Pilot 2022 |
|----------------|-------------|--------------|-------------------|-------------------|------------------|-------------------|------------------|-------------------|-------------------|-------------------|------------------|
| Dundee City    | N/A         | 9            | 21                | 89                | 7                | 123               | 14               | 97                | 37                | 95                | 90               |


Power Query was then used to clean the local authority enrolment descriptive analysis tables. This process involved unpivoting the columns to convert the data from wide form into long form to enable visualisations of Dundee’s statistics against the calculated descriptive statistics for all local authorities. This was done in preparation before being imported into Power BI for clearer and interactive visualisations of the comparisons.

## Average Scottish Foundational Enrolments Comparison
This comparison shows that Dundee’s FA enrolments prior to 2020 were less than the average for most Scottish local authorities. However, Dundee’s FA enrolments appear to have increased over time and surpassed the mean from 2020 to 2022. 

<img width="1228" height="613" alt="image" src="https://github.com/user-attachments/assets/2c4c9363-d0d0-4300-97e2-5c8352027775" />
Figure 1: Line chart showing Dundee's FA enrolments at level 6 compared to the overall Scottish mean.


## Average Scottish Foundational Pilot Enrolments Comparison
This comparison also suggests that Dundee’s FA pilot enrolments have been significantly lower than the Scottish average from 2019 to 2021 but were above the average in 2022. Though it is important to note that many local authorities do not have data available for FA pilots, either due to the data not being available, the local authorities not offering FA pilots, or due to disclosure control being applied to supress the data which may affect this interpretation.

<img width="1108" height="567" alt="image" src="https://github.com/user-attachments/assets/b638343e-883f-44e7-b9e3-a6eed40d7228" />
Figure 2: Line chart showing Dundee's FA enrolments at levels 4 and 5 compared to the overall Scottish mean.


# Gender Distribution
To explore question 2 and prior to analysis, Power Query was used to clean the data tables in sheet 1.2. This process involved replacing missing or supressed values, removing unneeded rows/columns, renaming column headers, unpivoting the columns to convert the data from wide form into long form, and splitting the columns on delimiter to create separate columns for ‘Gender’ and ‘Cohort’. Power BI was then used to visualise the gender distribution of each framework for each cohort. 

Total female and male enrolments for level 6 FAs were an equal 50/50 split for the first cohort in 2016/17. However, female enrolments have increased over the years, surpassing male enrolments and **increasing the enrolment gender gap by 26%** for the most recent cohort in 2022/23. Further research is needed before assumptions can be made as to the reasons for this widening gap.

<img width="1219" height="501" alt="image" src="https://github.com/user-attachments/assets/ef7f9ce2-0f25-4921-bc08-65a2c3f5afac" />
Figure 3: Line chart showing the increasing gender enrolment gap for level 6 FAs over the years.


Conversely, female enrolments for FAs at levels 4 and 5 have been consistently low at 11% female and 89% male in 2019/20, then 17% female and 83% male in 2022/23. This shows a small increase in female enrolments over the years, although **level 4 and 5 FA enrolments remain heavily male dominated**. This indicates that far more encouragement for female pupils to enrol is needed to remedy the gender inequality for FAs at these levels.

<img width="1574" height="679" alt="image" src="https://github.com/user-attachments/assets/38eea25e-e2a1-4506-abfd-6c6716160f3f" />
Figure 4: Side-by-side donut charts showing the gender distribution comparison between level 4 and 5 enrolments for 2019/20 and 2022/23.

## SCQF Level 6
The results of the visualisations show that female enrolments have a notable downward trend over the years in the Business Skills and Financial Services frameworks, and a slight downward trend in the Scientific Technologies framework for FAs at SCQF Level 6. The gender distribution of the Business Skills and Scientific Technologies frameworks were almost balanced in 2022/23, though the gender enrolment gap of the Financial Services framework has notably widened over the years. 

### Gender Distribution for Business Skills, Financial Services, and Scientific Technologies Frameworks
<img width="1133" height="680" alt="image" src="https://github.com/user-attachments/assets/40bb5d52-d07a-46a1-ad52-4fd1dbf4d2dc" />
Figure 5: 100% stacked bar charts showing the gender distribution of the Business Skills, Financial Services, and Scientific Technologies frameworks showing a downward trend of female enrolments from 2016/17 to 2022/23.

Multiple frameworks were selected in Power BI for a combined gender enrolment comparison analysis which shows that females consistently made up 13% and under of combined enrolments in Civil Engineering, Engineering, IT: Hardware/System Support, and IT: Software Development frameworks over the years.

### Combined Gender Distribution for Engineering and IT Frameworks
<img width="1129" height="659" alt="image" src="https://github.com/user-attachments/assets/6225396e-e83e-403b-a90d-39b24f4dc379" />
Figure 6: 100% stacked bar chart showing the combined gender distribution of the Civil Engineering, Engineering, IT: Hardware/System Support, and IT: Software Development frameworks.


Whereas males consistently made up 8% and under of combined enrolments in the Social Services and Healthcare, and Social Services Children and Young People frameworks over the years. 
### Combined Gender Distribution for Social Services and Healthcare Frameworks
<img width="1131" height="657" alt="image" src="https://github.com/user-attachments/assets/f4b5eea4-5594-47ff-a57c-babc17eae37a" />
Figure 7: 100% stacked bar chart showing the combined gender distribution of the Social Services and Healthcare, and Social Services Children and Young People frameworks.


The Accountancy and Creative and Digital Media frameworks have had the most equal gender distribution over the years, though Accountancy shows an increase in male enrolments, while the Creative and Digital Media framework shows an increase of female enrolments.

### Gender Distribution for Accountancy and Creative and Digital Media Frameworks
<img width="1237" height="742" alt="image" src="https://github.com/user-attachments/assets/a84994f0-85e6-4bda-9d93-da1e609a35d2" />
Figure 8: 100% stacked bar charts showing the gender distribution of the Accountancy and Creative and Digital Media frameworks.

## SCQF Level 4/5
Visualising the gender distribution of FA enrolments at levels 4 and 5 shows that the Automotive Skills and Construction Crafts frameworks remain heavily dominated by male pupils, whereas the Hospitality framework appears to have had a more balanced gender distribution.

### Gender Distribution of the Automative Skills, Construction Crafts, and Hospitality Frameworks
<img width="1174" height="696" alt="image" src="https://github.com/user-attachments/assets/2ff0b7a5-0a3a-4028-9174-8d2cee5714ac" />
Figure 9: 100% stacked bar charts showing the gender distribution of the Automative Skills, Construction Crafts, and Hospitality frameworks at levels 4 and 5.


## Conclusion
Analysis into the gender distribution of enrolments for each framework revealed that the engineering and IT level 6 frameworks and automotive and construction level 4/5 frameworks have consistently low female enrolments, while social service and healthcare level 6 frameworks have consistently low male enrolment. This may suggest that support for these specific frameworks should be more focused to tackle the gender imbalance, along with efforts to make these apprenticeships a more attractive choice for their respective underrepresented gender may have a stronger impact on closing the gender enrolment gaps. Encouraging more female pupils to pursue engineering, IT, construction, and automotive apprenticeships, whereas encouraging more male pupils to pursue social services and healthcare apprenticeships may have a better overall outcome in equalising the gender enrolment imbalance in these frameworks compared to simply focusing on FA enrolments overall.

## Data Quality
A note was included in the original data stating that disclosure control has been applied to values less than five (marked with an asterisk *) or where such numbers can be identified by differencing, and that some percentages may not sum to 100% due to rounding.

Many local authorities have some missing enrolment data; this missing data is more common for the SCQF levels 4/5 pilots. According to Skills Development Scotland, these pilots are work-based learning opportunities offered to pupils in S3 up to S6 via school-based projects. These pilots mainly focus on automotive, hospitality, and construction frameworks and were introduced in 2019. Compared to level 6 FAs which are offered to S5 and S6 pupils and introduced much earlier in 2016, they also offer more selection in frameworks. Being a newer process and more pupils naturally opting to enrol in a SCQF level 6 apprenticeship due to wider choice and availability are likely the main reasons for lack of enrolments. This may affect interpretation of Dundee’s enrolment comparison. 

Some local authorities in the SCQF L4/5 Pilot 2022 column in sheet 1.7 have enrolment values of ‘0’. It is not clear whether these values should have instead been recorded as an unknown value as no other columns have ‘0’ recorded enrolments. 
There was an unknown row in the 1.7 table which was removed before analysis due to having only 25 unknown enrolments associated with it.

## Bias and Limitations
The data in sheet 1.7 used for the enrolments by local authority analysis has both missing and anonymised data. Missing data was indicated by a dash ‘-‘ symbol, and anonymised data that was less than 5 was supressed with an asterisk ‘*’ symbol in the data tables. For visualisations in Power BI, both missing and anonymised cells were first converted into blank cells using Power Query. This removed the ability to distinguish between missing and supressed data in visualisations as Power BI excludes them in visuals by default.

There is an existing selection bias for frameworks by gender that has been observed in various academic areas. Female and male pupils may face societal, family, cultural, and peer pressure to pursue apprenticeship opportunities that align with gender stereotypes. This bias is important to keep in mind when considering possible solutions to increase the enrolment imbalance of certain frameworks.

It was not possible to explore gender distribution for frameworks by each local authority as the data did not include a breakdown of gender for each local authority’s enrolment counts. 
The accuracy of the data is both reliant on apprentices accurately self-reporting characteristics and is reliant on learning providers supplying data promptly and accurately. Many learning providers may have different frameworks to record information, which may lead to standardising issues when collecting the data.


## References
Skills Development Scotland (2025) FA Supplementary Tables 2023. Available at: https://www.skillsdevelopmentscotland.co.uk/publications-statistics/statistics/foundation-apprenticeships<br>
Skills Development Scotland (n.d.) Foundation Apprenticeships at SCQF Levels 4 and 5. Available at: https://www.apprenticeships.scot/for-employers/foundation-apprenticeships/scqf-levels-4-and-5/
