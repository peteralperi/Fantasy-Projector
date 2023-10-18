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
    url = 'https://www.fantasypros.com/nfl/stats/qb.php?year=2022&week={}&range=week'.format(week)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find('table').find('tbody').find_all('tr')

    

        
    for row in rows:
            if week == 9:
                dic = {}
                
                dic['Player'] = row.find('a').text
                dic['pYds'] = row.find_all('td')[5].text
                dic['pTds'] = row.find_all('td')[7].text
                dic['ints'] = row.find_all('td')[8].text
                dic['rYds'] = row.find_all('td')[11].text
                dic['rTds'] = row.find_all('td')[12].text
                dic['fumbs'] = row.find_all('td')[13].text
                dic['games'] = row.find_all('td')[14].text
                players_list.append(dic)
                
            if week == 10:
                dic1 = {}

                dic1['Player'] = row.find('a').text
                dic1['pYds'] = row.find_all('td')[5].text
                dic1['pTds'] = row.find_all('td')[7].text
                dic1['ints'] = row.find_all('td')[8].text
                dic1['rYds'] = row.find_all('td')[11].text
                dic1['rTds'] = row.find_all('td')[12].text
                dic1['fumbs'] = row.find_all('td')[13].text
                dic1['games'] = row.find_all('td')[14].text
                players_list1.append(dic1)
                
            if week == 11:
                dic2 = {}

                dic2['Player'] = row.find('a').text
                dic2['pYds'] = row.find_all('td')[5].text
                dic2['pTds'] = row.find_all('td')[7].text
                dic2['ints'] = row.find_all('td')[8].text
                dic2['rYds'] = row.find_all('td')[11].text
                dic2['rTds'] = row.find_all('td')[12].text
                dic2['fumbs'] = row.find_all('td')[13].text
                dic2['games'] = row.find_all('td')[14].text
                players_list2.append(dic2)
                
            if week == 12:
                dic3 = {}

                dic3['Player'] = row.find('a').text
                dic3['pYds'] = row.find_all('td')[5].text
                dic3['pTds'] = row.find_all('td')[7].text
                dic3['ints'] = row.find_all('td')[8].text
                dic3['rYds'] = row.find_all('td')[11].text
                dic3['rTds'] = row.find_all('td')[12].text
                dic3['fumbs'] = row.find_all('td')[13].text
                dic3['games'] = row.find_all('td')[14].text
                players_list3.append(dic3)
                
            if week == 13:
                dic4 = {}

                dic4['Player'] = row.find('a').text
                dic4['pYds'] = row.find_all('td')[5].text
                dic4['pTds'] = row.find_all('td')[7].text
                dic4['ints'] = row.find_all('td')[8].text
                dic4['rYds'] = row.find_all('td')[11].text
                dic4['rTds'] = row.find_all('td')[12].text
                dic4['fumbs'] = row.find_all('td')[13].text
                dic4['games'] = row.find_all('td')[14].text
                players_list4.append(dic4)
                
            if week == 14:
                dic5 = {}

                dic5['Player'] = row.find('a').text
                dic5['pYds'] = row.find_all('td')[5].text
                dic5['pTds'] = row.find_all('td')[7].text
                dic5['ints'] = row.find_all('td')[8].text
                dic5['rYds'] = row.find_all('td')[11].text
                dic5['rTds'] = row.find_all('td')[12].text
                dic5['fumbs'] = row.find_all('td')[13].text
                dic5['games'] = row.find_all('td')[14].text
                players_list5.append(dic5)
                
            if week == 15:
                dic6 = {}

                dic6['Player'] = row.find('a').text
                dic6['pYds'] = row.find_all('td')[5].text
                dic6['pTds'] = row.find_all('td')[7].text
                dic6['ints'] = row.find_all('td')[8].text
                dic6['rYds'] = row.find_all('td')[11].text
                dic6['rTds'] = row.find_all('td')[12].text
                dic6['fumbs'] = row.find_all('td')[13].text
                dic6['games'] = row.find_all('td')[14].text
                players_list6.append(dic6)
                
            if week == 16:
                dic7 = {}

                dic7['Player'] = row.find('a').text
                dic7['pYds'] = row.find_all('td')[5].text
                dic7['pTds'] = row.find_all('td')[7].text
                dic7['ints'] = row.find_all('td')[8].text
                dic7['rYds'] = row.find_all('td')[11].text
                dic7['rTds'] = row.find_all('td')[12].text
                dic7['fumbs'] = row.find_all('td')[13].text
                dic7['games'] = row.find_all('td')[14].text
                players_list7.append(dic7)
                
            if week == 17:
                dic8 = {}

                dic8['Player'] = row.find('a').text
                dic8['pYds'] = row.find_all('td')[5].text
                dic8['pTds'] = row.find_all('td')[7].text
                dic8['ints'] = row.find_all('td')[8].text
                dic8['rYds'] = row.find_all('td')[11].text
                dic8['rTds'] = row.find_all('td')[12].text
                dic8['fumbs'] = row.find_all('td')[13].text
                dic8['games'] = row.find_all('td')[14].text
                players_list8.append(dic8)
                
            if week == 18:
                dic9 = {}

                dic9['Player'] = row.find('a').text
                dic9['pYds'] = row.find_all('td')[5].text
                dic9['pTds'] = row.find_all('td')[7].text
                dic9['ints'] = row.find_all('td')[8].text
                dic9['rYds'] = row.find_all('td')[11].text
                dic9['rTds'] = row.find_all('td')[12].text
                dic9['fumbs'] = row.find_all('td')[13].text
                dic9['games'] = row.find_all('td')[14].text
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
sheet_name = "QB"
df_mapping = {"A1": df, "A275": df1, "A550": df2, "A825":df3, "A1100":df4, "A1375":df5, "A1650":df6, "A1925":df7, "A2200":df8, "A2475":df9}

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