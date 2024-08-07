import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

qb_list = []


for week in range(16,19):
    url = 'https://www.fantasypros.com/nfl/stats/qb.php?year=2023&week={}&range=week'.format(week)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find('table').find('tbody').find_all('tr')

    

        
    for row in rows:
            if week == 16:
                dic = {}
                
                dic['Player'] = row.find('a').text
                dic['pYds'] = row.find_all('td')[5].text
                dic['pTds'] = row.find_all('td')[7].text
                dic['ints'] = row.find_all('td')[8].text
                dic['rYds'] = row.find_all('td')[11].text
                dic['rTds'] = row.find_all('td')[12].text
                dic['fumbs'] = row.find_all('td')[13].text
                dic['games'] = row.find_all('td')[14].text
                qb_list.append(dic)
                
            if week == 17:
                dic1 = {}

                dic1['Player'] = row.find('a').text
                dic1['pYds'] = row.find_all('td')[5].text
                dic1['pTds'] = row.find_all('td')[7].text
                dic1['ints'] = row.find_all('td')[8].text
                dic1['rYds'] = row.find_all('td')[11].text
                dic1['rTds'] = row.find_all('td')[12].text
                dic1['fumbs'] = row.find_all('td')[13].text
                dic1['games'] = row.find_all('td')[14].text
                qb_list.append(dic1)
                
            if week == 18:
                dic2 = {}

                dic2['Player'] = row.find('a').text
                dic2['pYds'] = row.find_all('td')[5].text
                dic2['pTds'] = row.find_all('td')[7].text
                dic2['ints'] = row.find_all('td')[8].text
                dic2['rYds'] = row.find_all('td')[11].text
                dic2['rTds'] = row.find_all('td')[12].text
                dic2['fumbs'] = row.find_all('td')[13].text
                dic2['games'] = row.find_all('td')[14].text
                qb_list.append(dic2)
                
            


df = pd.DataFrame(qb_list)
df1 = pd.DataFrame(qb_list)
df2 = pd.DataFrame(qb_list)


df.to_csv("playerData.csv")               
df1.to_csv("playerData.csv")
df2.to_csv("playerData.csv")


    
print("Done.")