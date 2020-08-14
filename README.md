# climbing-crag-selection

- Created a tool to help decide which climbing crags to focus on for the next climbing trip for my friend and I, with the goal to improve our climbing grade.
- Scraped over 4000 routes/problems for the climbing destination in question.
- I will report back whether my efforts were successful or not.

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

Based on this data analysis we will be going to Blacknor South, Winspit, and Cheyne Weares Area.

Blacknor South:
Sacred Angel ** 15m (Easy up to ledge, then fingery crux with pockets)
To Wish the Impossible *** 20m (sustained with delicate & fingery climbing, lots of rests, big moves off jugs)
Winspit
Peppercorn Rate ** 20m (tough and pumpy with a blind crack)
Exuberence * 20m (one hard bit at top, not so many onsightsbut alot of redpoints)
Ancient order of Freemarblers ** 20m (steep stamina climbing, decent proportion of onsights)
Gallows' Gore ** 20m (crux at the middle, either fingery or pull hard, can be onsightable by a boulderer)
Agonies of a Dying Mind * 20m (powerful start about a V3/V4, but high rate of onsight and redpoints)
Cheyne Weares Area
The Accelerator * 7m (sounds super soft and pump shouldn't be a factor!)
I will report back to say whether it was a mission success or not :)

# Future Improvements
