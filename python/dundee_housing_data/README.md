# Dundee Housing Datasets - Data Exploration and Analysis
A small Python project exploring Dundee's housing datasets, including CSV housing site information and GeoJSON spatial boundaries.
The project focuses on understanding tenure types, site capacity, and boundary complexity to reveal planning and development patterns across Dundee.

## Technologies Used
- Python
- pandas for data handling
- Jupyter Notebook enviroment

# Summaries from the Analysis
## Relationship Between Tenure Types and Projected Build Volume
This breif analysis explored the relationship between tenure type and projected build volume within Dundee's housing site dataset. Total site capacity was calculated for each tenure type, showing that the Private sector dominates overall capacity - contributing 3503 units, far more than any other category. Social housing providers - RSLs (Registered Social Landlords) also contribute a significant volume (840 units), while Local Authority and Housing Association sites make up only a small portion of the total supply.

When this was compared with the total projected build volume for 2024-2027 (1412 units), this indicates that although the private sector holds most long-term capacity, it does not necessarily represent the majority of short-term delivery. Much of the private capacity appears to be related to sites at thier early planning stages or with long-term build periods. This suggests that tenure type likely influences the likelihood and timing of delivery. This has implications for Dundee's overall housing mix, future affordability, and the reliability of supply coming forward in the next few years.


## How Site Capacity Varies with Site Size and Status
The analysis of Dundee's housing sites shows a clear relationship between site size and development status, which in turn influences how much capacity each site is likely to deliver. The largest sites on average are those still 'Allocated in the Local Development Plan (LDP)' or 'Under Construction', with mean areas of around 14.8 ha and 13.3 ha respectively. 

Sites that have reached 'Planning Consent' are noticeably smaller, averaging 7.5 ha, suggesting these are mid-scale developments progressing through the planning stages. In comparison, 'Completed' sites have the smallest average area at around 6.4 ha, indicating that smaller sites tend to reach completion more quickly and contribute to short-term delivery.

Overall, larger sites mainly contribute to future potential capacity but are more likely to be in early stages of development, while smaller sites are more likely to be built already. This analysis highlights how site size influences delivery speed, with small sites providing immediate capacity, and large sites contributing to long-term supply.

## How the Complexity of Site Boundaries May Affect Spatial Analysis
Spatial analysis of housing sites in Dundee relies heavily on the accuracy and structure of the polygon boundaries stored within the GeoJSON data. The complexity of these boundaries increases with the number of vertices, their shape irregularity, and the detail of the surveyed outlines, which can influence both the performance of spatial operations/analysis and the reliability of any outputs.

**Performance**:
Sites with very detailed or irregular boundaries will require more processing time during spatial operations. Each additional coordinate point increases computational effort, which means that operations on larger sites may take noticeably longer compared to smaller, more compact sites.

**Accuracy**:
Boundary complexity can distort geometric measurements. Highly detailed outlines may artificially increase the computed perimeter, and very fine warping in the boundary can slightly inflate calculated area. For Dundee's housing sites, this could affect comparisons of site size, capacity-per-hectare calculations.

**Joins**:
Irregular boundaries can lead to misclassification when determining which administrative ward, neighbourhood, or land-use zone a site falls within. This may be relevant in Dundee where boundaries for electoral wards, settlement areas, and planning zones differ in their level of detail.

**Interpretation**:
Highly detailed site polygons can reduce clarity in maps, especially when many sites are shown together (e.g. completed vs in-progress vs planning). Complex boundaries may clutter the map, making it harder to visually interpret development patterns across Dundee. Simplified versions often provide a clearer overview without losing essential spatial meaning.
