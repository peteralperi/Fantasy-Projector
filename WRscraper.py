import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

wr_week1 = []
wr_week2= []
wr_week3= []


for week in range(16,19):
    url = 'https://www.fantasypros.com/nfl/stats/wr.php?year=2023&week={}&range=week'.format(week)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find('table').find('tbody').find_all('tr')

    for row in rows:
            if week == 16:
                dic = {}
                
                dic['Player'] = row.find('a').text
                dic['recs'] = row.find_all('td')[2].text
                dic['recYds'] = row.find_all('td')[4].text
                dic['recTds'] = row.find_all('td')[8].text
                dic['rYds'] = row.find_all('td')[10].text
                dic['rTds'] = row.find_all('td')[11].text
                dic['fumbs'] = row.find_all('td')[12].text
                dic['games'] = row.find_all('td')[13].text
                wr_week1.append(dic)
                
            if week == 17:
                dic1 = {}

                dic1['Player'] = row.find('a').text
                dic1['recs'] = row.find_all('td')[2].text
                dic1['recYds'] = row.find_all('td')[4].text
                dic1['recTds'] = row.find_all('td')[8].text
                dic1['rYds'] = row.find_all('td')[10].text
                dic1['rTds'] = row.find_all('td')[11].text
                dic1['fumbs'] = row.find_all('td')[12].text
                dic1['games'] = row.find_all('td')[13].text
                wr_week2.append(dic1)
                
            if week == 18:
                dic2 = {}

                dic2['Player'] = row.find('a').text
                dic2['recs'] = row.find_all('td')[2].text
                dic2['recYds'] = row.find_all('td')[4].text
                dic2['recTds'] = row.find_all('td')[8].text
                dic2['rYds'] = row.find_all('td')[10].text
                dic2['rTds'] = row.find_all('td')[11].text
                dic2['fumbs'] = row.find_all('td')[12].text
                dic2['games'] = row.find_all('td')[13].text
                wr_week3.append(dic2)
                
            

df = pd.DataFrame(wr_week1)
df1 = pd.DataFrame(wr_week2)
df2 = pd.DataFrame(wr_week3)






df.to_csv("playerData.csv", mode= "a")          
df1.to_csv("playerData.csv", mode= "a")
df2.to_csv("playerData.csv", mode= "a")


    
print("Done.")