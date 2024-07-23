# Fantasy-Projector

Description:
- Utilized Python, Pandas, Openpyxl, Excel, and BeautifulSoup4, to WebScrape weekly NFL player data and convert it to an Excel spreadsheet. 
- Gives a prediction of how many Fantasy Football points a player will score based on opponent defense statistics and rankings, and individual player data from previous weeks.


Notes:
- Projections are based on individual player data from their previous ten performances. If the player is a rookie, it will only take into account the games they have played during the first year of the NFL season.
- Projections are also based on strength of defense, as this projector only projects player scores for offensive skill players.
- To get projection, user must first run all of the scraper scripts to get the data into the "bigboy" file, where main can then be ran to create a projection.
