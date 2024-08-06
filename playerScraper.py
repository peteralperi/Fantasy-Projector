from bs4 import BeautifulSoup
import requests
import pandas as pd

url = ('https://www.pro-football-reference.com/years/2022/fantasy.htm#')
                            
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table').find('tbody').find_all('tr')

players_list=[]

for row in rows:
    dic={}
    word = row.find_all('a')
    dic['Player'] = word.get_text

    players_list.append(dic)


df = pd.DataFrame(players_list)
df.to_excel("players.xlsx")
df.to_csv("players.csv")

print("Done.")
    
    

