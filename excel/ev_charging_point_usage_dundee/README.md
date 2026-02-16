# Exploring and Analysing Community Data
## Public EV Charge Point Usage Dundee City Council (Jan 2025 to Aug 2025)

The dataset used was obtained in CSV format from the Dundee Open Data portal found at: https://data.dundeecity.gov.uk/datasets/e185a3a1cfc948a69ada76e950b9d447/about

The dataset contains recorded charging usage instances of Electric Vehicles (EVs) from January 2025 to August 2025. This data includes information for each charging instance including SRD ID – which is the unique ID of the charging instance, charging point ID (CP ID) – which is a unique identifier for each charger located within a site, location information such as the site name and postcode. The data also includes connector type, energy consumed in kWh, duration, and the start/end date and time of each charging instance.

**Note:** I removed 9 rows before my analysis which contained negative values in the Duration column. They appear to have been incorrectly recorded as they also have incorrect End Dates in the year of 1990.

## Which Charging Hub has the highest average energy consumption?
The Greenmarket 150kWh Bus Charger hub, or site, has the highest average energy consumption of 164.02kWh. 

<img width="1401" height="704" alt="image" src="https://github.com/user-attachments/assets/37b13250-fc68-40d7-b4f4-51c494bfdaa2" />


## Most rapid charging sessions last between how many minutes?
Most rapid charging sessions last between 21-50 minutes.

<img width="949" height="564" alt="image" src="https://github.com/user-attachments/assets/ab15e4c0-2f02-437d-ae65-2def0bf271bb" />


## Which hub is busiest on weekend evenings?
Princes Street Charging Hub is the busiest hub on weekend evenings (between 5pm to 9pm), followed by Clepington Road – 4th Hub, and Lochee Charging Hub. With 949, 935, and 704 recorded charging instances respectively.

<img width="1248" height="750" alt="image" src="https://github.com/user-attachments/assets/aebf0245-5e9b-4672-85a1-f38b9c447b93" />


## The total energy consumption (kWh) per site
Clepington Road – 4th Hub has the highest total consumption out of all the sites at 350,983.07kWh. Which is almost 100,000kWh more consumption than the next highest site Princes Street Charging Hub, which sits at 251669.47 kWh.

<img width="1632" height="614" alt="image" src="https://github.com/user-attachments/assets/54223eb0-efec-456c-af6d-50d417400c94" />


## Average session duration over time
Average charging duration was lowest in February 2025, then started to steadily rise onwards and peaked in August 2025. 

<img width="1044" height="570" alt="image" src="https://github.com/user-attachments/assets/8b3df054-1a20-4379-8092-4cfc1db6db4d" />

