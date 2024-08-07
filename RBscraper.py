import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw


rb_week1 = []
rb_week2= []
rb_week3= []



for week in range(16,19):
    RBurl = 'https://www.fantasypros.com/nfl/stats/rb.php?year=2023&week={}&range=week'.format(week)

    RBresponse = requests.get(RBurl)
    RBsoup = BeautifulSoup(RBresponse.text, 'html.parser')

    RBrows = RBsoup.find('table').find('tbody').find_all('tr')

        
    for row in RBrows:
            if week == 16:
                RBdic = {}
                
                RBdic['Player'] = row.find('a').text
                RBdic['rYds'] = row.find_all('td')[3].text
                RBdic['rTds'] = row.find_all('td')[7].text
                RBdic['recs'] = row.find_all('td')[8].text
                RBdic['recYds'] = row.find_all('td')[10].text
                RBdic['recTds'] = row.find_all('td')[12].text
                RBdic['fumbs'] = row.find_all('td')[13].text
                RBdic['games'] = row.find_all('td')[14].text
                rb_week1.append(RBdic)
                
            if week == 17:
                RBdic1 = {}

                RBdic1['Player'] = row.find('a').text
                RBdic1['rYds'] = row.find_all('td')[3].text
                RBdic1['rTds'] = row.find_all('td')[7].text
                RBdic1['recs'] = row.find_all('td')[8].text
                RBdic1['recYds'] = row.find_all('td')[10].text
                RBdic1['recTds'] = row.find_all('td')[12].text
                RBdic1['fumbs'] = row.find_all('td')[13].text
                RBdic1['games'] = row.find_all('td')[14].text
                rb_week2.append(RBdic1)
                
            if week == 18:
                RBdic2 = {}

                RBdic2['Player'] = row.find('a').text
                RBdic2['rYds'] = row.find_all('td')[3].text
                RBdic2['rTds'] = row.find_all('td')[7].text
                RBdic2['recs'] = row.find_all('td')[8].text
                RBdic2['recYds'] = row.find_all('td')[10].text
                RBdic2['recTds'] = row.find_all('td')[12].text
                RBdic2['fumbs'] = row.find_all('td')[13].text
                RBdic2['games'] = row.find_all('td')[14].text
                rb_week3.append(RBdic2)
                
            

RBdf = pd.DataFrame(rb_week1)
RBdf1 = pd.DataFrame(rb_week2)
RBdf2 = pd.DataFrame(rb_week3)


RBdf.to_csv("playerData.csv", mode= "a")
RBdf1.to_csv("playerData.csv", mode= "a")    
RBdf2.to_csv("playerData.csv", mode= "a")    




    
print("Done.")