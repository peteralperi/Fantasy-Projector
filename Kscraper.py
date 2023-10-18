import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

players_list = []
players_list1= []
players_list2= []
players_list3= []
players_list4= []
players_list5= []
players_list6= []
players_list7= []
players_list8= []
players_list9= []


for week in range(9,19):
    url = 'https://www.fantasypros.com/nfl/stats/k.php?year=2022&week={}&range=week'.format(week)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find('table').find('tbody').find_all('tr')

    

        
    for row in rows:
            if week == 9:
                dic = {}
                
                dic['Player'] = row.find('a').text
                dic['FG'] = row.find_all('td')[2].text
                dic['FGA'] = row.find_all('td')[3].text
                dic['1-19'] = row.find_all('td')[6].text
                dic['20-29'] = row.find_all('td')[7].text
                dic['30-39'] = row.find_all('td')[8].text
                dic['40-49'] = row.find_all('td')[9].text
                dic['50+'] = row.find_all('td')[10].text
                dic['XPT'] = row.find_all('td')[11].text
                dic['games'] = row.find_all('td')[13].text
                players_list.append(dic)
                
            if week == 10:
                dic1 = {}

                dic1['Player'] = row.find('a').text
                dic1['FG'] = row.find_all('td')[2].text
                dic1['FGA'] = row.find_all('td')[3].text
                dic1['1-19'] = row.find_all('td')[6].text
                dic1['20-29'] = row.find_all('td')[7].text
                dic1['30-39'] = row.find_all('td')[8].text
                dic1['40-49'] = row.find_all('td')[9].text
                dic1['50+'] = row.find_all('td')[10].text
                dic1['XPT'] = row.find_all('td')[11].text
                dic1['games'] = row.find_all('td')[13].text
                players_list1.append(dic1)
                
            if week == 11:
                dic2 = {}

                dic2['Player'] = row.find('a').text
                dic2['FG'] = row.find_all('td')[2].text
                dic2['FGA'] = row.find_all('td')[3].text
                dic2['1-19'] = row.find_all('td')[6].text
                dic2['20-29'] = row.find_all('td')[7].text
                dic2['30-39'] = row.find_all('td')[8].text
                dic2['40-49'] = row.find_all('td')[9].text
                dic2['50+'] = row.find_all('td')[10].text
                dic2['XPT'] = row.find_all('td')[11].text
                dic2['games'] = row.find_all('td')[13].text
                players_list2.append(dic2)
                
            if week == 12:
                dic3 = {}

                dic3['Player'] = row.find('a').text
                dic3['FG'] = row.find_all('td')[2].text
                dic3['FGA'] = row.find_all('td')[3].text
                dic3['1-19'] = row.find_all('td')[6].text
                dic3['20-29'] = row.find_all('td')[7].text
                dic3['30-39'] = row.find_all('td')[8].text
                dic3['40-49'] = row.find_all('td')[9].text
                dic3['50+'] = row.find_all('td')[10].text
                dic3['XPT'] = row.find_all('td')[11].text
                dic3['games'] = row.find_all('td')[13].text
                players_list3.append(dic3)
                
            if week == 13:
                dic4 = {}

                dic4['Player'] = row.find('a').text
                dic4['FG'] = row.find_all('td')[2].text
                dic4['FGA'] = row.find_all('td')[3].text
                dic4['1-19'] = row.find_all('td')[6].text
                dic4['20-29'] = row.find_all('td')[7].text
                dic4['30-39'] = row.find_all('td')[8].text
                dic4['40-49'] = row.find_all('td')[9].text
                dic4['50+'] = row.find_all('td')[10].text
                dic4['XPT'] = row.find_all('td')[11].text
                dic4['games'] = row.find_all('td')[13].text
                players_list4.append(dic4)
                
            if week == 14:
                dic5 = {}

                dic5['Player'] = row.find('a').text
                dic5['FG'] = row.find_all('td')[2].text
                dic5['FGA'] = row.find_all('td')[3].text
                dic5['1-19'] = row.find_all('td')[6].text
                dic5['20-29'] = row.find_all('td')[7].text
                dic5['30-39'] = row.find_all('td')[8].text
                dic5['40-49'] = row.find_all('td')[9].text
                dic5['50+'] = row.find_all('td')[10].text
                dic5['XPT'] = row.find_all('td')[11].text
                dic5['games'] = row.find_all('td')[13].text
                players_list5.append(dic5)
                
            if week == 15:
                dic6 = {}

                dic6['Player'] = row.find('a').text
                dic6['FG'] = row.find_all('td')[2].text
                dic6['FGA'] = row.find_all('td')[3].text
                dic6['1-19'] = row.find_all('td')[6].text
                dic6['20-29'] = row.find_all('td')[7].text
                dic6['30-39'] = row.find_all('td')[8].text
                dic6['40-49'] = row.find_all('td')[9].text
                dic6['50+'] = row.find_all('td')[10].text
                dic6['XPT'] = row.find_all('td')[11].text
                dic6['games'] = row.find_all('td')[13].text
                players_list6.append(dic6)
                
            if week == 16:
                dic7 = {}

                dic7['Player'] = row.find('a').text
                dic7['FG'] = row.find_all('td')[2].text
                dic7['FGA'] = row.find_all('td')[3].text
                dic7['1-19'] = row.find_all('td')[6].text
                dic7['20-29'] = row.find_all('td')[7].text
                dic7['30-39'] = row.find_all('td')[8].text
                dic7['40-49'] = row.find_all('td')[9].text
                dic7['50+'] = row.find_all('td')[10].text
                dic7['XPT'] = row.find_all('td')[11].text
                dic7['games'] = row.find_all('td')[13].text
                players_list7.append(dic7)
                
            if week == 17:
                dic8 = {}

                dic8['Player'] = row.find('a').text
                dic8['FG'] = row.find_all('td')[2].text
                dic8['FGA'] = row.find_all('td')[3].text
                dic8['1-19'] = row.find_all('td')[6].text
                dic8['20-29'] = row.find_all('td')[7].text
                dic8['30-39'] = row.find_all('td')[8].text
                dic8['40-49'] = row.find_all('td')[9].text
                dic8['50+'] = row.find_all('td')[10].text
                dic8['XPT'] = row.find_all('td')[11].text
                dic8['games'] = row.find_all('td')[13].text
                players_list8.append(dic8)
                
            if week == 18:
                dic9 = {}

                dic9['Player'] = row.find('a').text
                dic9['FG'] = row.find_all('td')[2].text
                dic9['FGA'] = row.find_all('td')[3].text
                dic9['1-19'] = row.find_all('td')[6].text
                dic9['20-29'] = row.find_all('td')[7].text
                dic9['30-39'] = row.find_all('td')[8].text
                dic9['40-49'] = row.find_all('td')[9].text
                dic9['50+'] = row.find_all('td')[10].text
                dic9['XPT'] = row.find_all('td')[11].text
                dic9['games'] = row.find_all('td')[13].text
                players_list9.append(dic9)


df = pd.DataFrame(players_list)
df1 = pd.DataFrame(players_list1)
df2 = pd.DataFrame(players_list2)
df3 = pd.DataFrame(players_list3)
df4 = pd.DataFrame(players_list4)
df5 = pd.DataFrame(players_list5)
df6 = pd.DataFrame(players_list6)
df7 = pd.DataFrame(players_list7)
df8 = pd.DataFrame(players_list8)
df9 = pd.DataFrame(players_list9)


wb_name = "bigboy.xlsx"
sheet_name = "K"
df_mapping = {"A1": df, "A100": df1, "A200": df2, "A300":df3, "A400":df4, "A500":df5, "A600":df6, "A700":df7, "A800":df8, "A900":df9}

#open excel in background
with xw.App(visible=False) as app:
    wb = app.books.open(wb_name)


    # add sheet if it doesnt exist
    current_sheets = [sheet.name for sheet in wb.sheets]
    if sheet_name not in current_sheets:
        wb.sheets.add(sheet_name)
    
    #write dataframe to cell range
    for cell_target, df in df_mapping.items():
        wb.sheets(sheet_name).range(cell_target).options(pd.DataFrame, index = False).value = df
    
    wb.save()
    


df.to_csv("bigboy.csv")    
            
df1.to_csv("bigboy.csv")


    
print("Done.")