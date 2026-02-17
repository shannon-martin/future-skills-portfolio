# Exploring and Analysing Community Data
## Public EV Charge Point Usage Dundee City Council (Jan 2025 to Aug 2025)

The dataset used was obtained in CSV format from the Dundee Open Data portal found at: https://data.dundeecity.gov.uk/datasets/e185a3a1cfc948a69ada76e950b9d447/about

The dataset contains recorded charging usage instances of Electric Vehicles (EVs) from January 2025 to August 2025. This data includes information for each charging instance including SRD ID – which is the unique ID of the charging instance, charging point ID (CP ID) – which is a unique identifier for each charger located within a site, location information such as the site name and postcode. The data also includes connector type, energy consumed in kWh, duration, and the start/end date and time of each charging instance.

**Note:** I removed 9 rows before my analysis which contained negative values in the Duration column. They appear to have been incorrectly recorded as they also have incorrect End Dates in the year of 1990.

## Which Charging Hub has the highest average energy consumption?
The Greenmarket 150kWh Bus Charger hub, or site, has the highest average energy consumption of 164.02kWh. 

<img width="1401" height="704" alt="image" src="https://github.com/user-attachments/assets/37b13250-fc68-40d7-b4f4-51c494bfdaa2" />

Looking closer at the individual charging points, the points with CP ID’s 62124 and 62125, which are located at the Greenmarket 150kWh Bus Charger site, have the highest average energy consumption at 166.12kWh and 162.05kWh respectively.
The Greenmarket bus charging hub uses an ultra-rapid charger which can output DC≥150kWh, compared to other charging sites which primarily use rapid and AC connecters, which have lower output. This charging point is likely designed to charge larger electric vehicles like busses, so this is not a surprising finding considering that electric busses also have a significantly larger battery capacity than electric cars. 
Looking at the individual charging points, no other charging points exceed an average of 40kWh, and looking at the sites, most appear to fall between an average of 10 – 30 kWh. So, Greenmarket 150kWh Bus Charger site significantly skews the overall average.


## Most rapid charging sessions last between how many minutes?
Most rapid charging sessions last between 21-50 minutes.

<img width="949" height="564" alt="image" src="https://github.com/user-attachments/assets/ab15e4c0-2f02-437d-ae65-2def0bf271bb" />

After creating some bin ranges of 10 minutes, including an underflow of less than 1 minute and an overflow of more than 120 minutes (2 hours). I then created a visualisation of the counts of each charging instance which fall into these defined ranges. The visualisation showed most charging durations fell between 21-50 minutes.
To get a more precise understanding of the most common durations for charging sessions, I may want to create smaller bin ranges (i.e. 5 minutes instead of 10 minutes).


## Which hub is busiest on weekend evenings?
Princes Street Charging Hub is the busiest hub on weekend evenings (between 5pm to 9pm), followed by Clepington Road – 4th Hub, and Lochee Charging Hub. With 949, 935, and 704 recorded charging instances respectively.

<img width="1248" height="750" alt="image" src="https://github.com/user-attachments/assets/aebf0245-5e9b-4672-85a1-f38b9c447b93" />

To visualise this, I created a PivotChart using the Site as the Axis and the count of the individual charging instances (SRD ID) as Values, then filtered by day of the week (Saturdays and Sundays), and starting hours between 5pm to 9pm. Due to the exact definition of ‘weekend evenings’ varying, I also changed the filters to show 6pm to 10pm, which showed the same three sites as busiest.

Looking closer at the individual the charging points located at each site shows points with CP ID’s 61615 and 61616 to be the busiest, which both correspond to the Clepington Road – 4th Hub site, with 263 and 185 separate charging instances recorded for each point respectively.

Looking at this data made me consider that it could be important to note the amount of charging points per site. Many of the busiest sites are the sites with a higher number of charging points – meaning they can accommodate more EVs compared to sites which have fewer charging points. For reference, out of the 32 sites, 25 have 1-2 charging points. Princes Street Charging Hub has 9 charging points, Clepington Road – 4th Hub has 6 charging points, and Lochee Charging Hub has 10 charging points. 


## The total energy consumption (kWh) per site
Clepington Road – 4th Hub has the highest total consumption out of all the sites at 350,983.07kWh. Which is almost 100,000kWh more consumption than the next highest site Princes Street Charging Hub, which sits at 251669.47 kWh.

<img width="1632" height="614" alt="image" src="https://github.com/user-attachments/assets/54223eb0-efec-456c-af6d-50d417400c94" />


## Average session duration over time
Average charging duration was lowest in February 2025, then started to steadily rise onwards and peaked in August 2025. 

<img width="1044" height="570" alt="image" src="https://github.com/user-attachments/assets/8b3df054-1a20-4379-8092-4cfc1db6db4d" />


