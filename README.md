# climbing-crag-selection

- Created a tool to help decide which climbing crags to focus on for future climbing trips, with the goal to improve the climbing grades of my friends and I.
- Scraped over 4000 routes/problems for the climbing destination in question.
- I will update this repositry as I analyse more climbing destinations and update whether my efforts were successful.

# Code and Resources Used
**Python Version:** 3.8

**Packages:** pandas, numpy, matplotlib, selenium, beautiful soup

# Web scraping
I made a python script to scrape all the climbing routes in the area that my friend and I will be heading next month. Each routes provides the following information:
- Name of the route
- Grade
- Stars (i.e. quality of the route, with 3 stars being a classic)
- Type of climb
- Logs 
- Crag

# Data Cleaning
After scraping the data, I need to clean it before analysis. The following changes were made:
- Drop rows which were subheadings and not useful route data.
- Dropped 'Unnamed: 7' column.
- Convert columns 'Stars' and 'Logs' to integers for more flexible analysis.

# EDA
Below are a few insights gleamed from the routes analysis.
![Climbing disciplines in Dorset](/images/disciplines.png)

![Sport grade distribution](/images/sport-grade-distribution.png)

![7a routes sorted by popularity](/images/logged-7a.PNG)

![Chosen crags](/images/crags.PNG)


Based on this data analysis we will be going to Blacknor South, Winspit, and Cheyne Weares Area.

|  Crag | Route  | Star | Height (m)  | Notes  |
|---|---|---|---|---|
| Blacknor South  | Sacred Angel  | ** | 15  | Easy up to ledge, then fingery crux with pockets |
| Blacknor South  | To Wish the Impossible   | *** | 20  | Sustained with delicate & fingery climbing, lots of rests, big moves off jugs  |
| Winspit  | Peppercorn Rate  | **  | 20  | Tough and pumpy with a blind crack  | 
| Winspit  | Exuberence  |  * | 20  | One hard bit at top, not so many onsightsbut alot of redpoints  | 
| Winspit  | Ancient order of Freemarblers  | **  | 20  | Steep stamina climbing, decent proportion of onsights  | 
| Winspit  | Gallows' Gore  |  ** | 20  | Powerful start about a V3/V4, but high rate of onsight and redpoints  | 
| Winspit  | Agonies of a Dying Mind  |  * | 20  | Powerful start about a V3/V4, but high rate of onsight and redpoints  | 
| Cheyne Weares Area  | The Accelerator  | *  | 7  |  Sounds super soft and pump shouldn't be a factor! | 

# Future Improvements
- Automate the analysis process for future climbing trips, likely destinations include the Peak Districtm Southern Sandstone, Costa Blanca, and Chamonix.
- Screenshot and scrape the bar chart information on style of ascents and voting of the route diffulty, and sort the routes by highest percent that have been onsighted or by 'softness'.


