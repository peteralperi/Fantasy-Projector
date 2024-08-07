import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

players_list = []
players_list1 = []

defense_choice = ["passing", "rushing", "receiving"]

for i in range(0,2):

    url = 'https://www.nfl.com/stats/team-stats/defense/{}/2022/reg/all'.format(defense_choice[i])

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find('table').find('tbody').find_all('tr')
    
    
    
    if i == 0:
        for row in rows:
            dic = {}
                        
            dic['Team'] = row.find('td').find('div', class_='d3-o-club-shortname').text
            dic['pYds'] = row.find_all('td')[5].text
            dic['pTds'] = row.find_all('td')[6].text
            dic['ints'] = row.find_all('td')[7].text
            players_list.append(dic) 
            
    if i == 1:
        for row in rows:
            dic1 = {}
                        
            dic1['Team'] = row.find('td').find('div', class_='d3-o-club-shortname').text
            dic1['attempts'] = row.find_all('td')[1].text
            dic1['ryds'] = row.find_all('td')[2].text
            dic1['ypc'] = row.find_all('td')[3].text
            dic1['rTds'] = row.find_all('td')[4].text
            players_list1.append(dic1)
            
df = pd.DataFrame(players_list)
df1 = pd.DataFrame(players_list1)
            

# wb_name = "bigboy.xlsx"
# sheet_name = "Defense"
# df_mapping = {"A1": df, "G1": df1}

# #open excel in background
# with xw.App(visible=False) as app:
#     wb = app.books.open(wb_name)


#     # add sheet if it doesnt exist
#     current_sheets = [sheet.name for sheet in wb.sheets]
#     if sheet_name not in current_sheets:
#         wb.sheets.add(sheet_name)
    
#     #write dataframe to cell range
#     for cell_target, df in df_mapping.items():
#         wb.sheets(sheet_name).range(cell_target).options(pd.DataFrame, index = False).value = df
    
#     wb.save()