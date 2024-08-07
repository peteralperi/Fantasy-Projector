import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

k_week1 = []
k_week2= []
k_week3= []



for week in range(16,19):
    url = 'https://www.fantasypros.com/nfl/stats/k.php?year=2023&week={}&range=week'.format(week)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find('table').find('tbody').find_all('tr')


    for row in rows:
            if week == 16:
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
                k_week1.append(dic)
                
            if week == 17:
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
                k_week2.append(dic1)
                
            if week == 18:
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
                k_week3.append(dic2)
                
            

df = pd.DataFrame(k_week1)
df1 = pd.DataFrame(k_week2)
df2 = pd.DataFrame(k_week3)


df.to_csv("playerData.csv", mode= "a")  
df1.to_csv("playerData.csv", mode= "a")
df2.to_csv("playerData.csv", mode= "a")

    
print("Done.")