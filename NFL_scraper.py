'''

Author: Peter Alperi

This will be the file that scrapes all the player statistics into the ________.csv file.

This scraper will get statistics of players from all fantasy relevant positions, including
Quarterback (QB), Running Back (RB), Wide Receiver (WR), Tight End (TE), and Kicker (K).



'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw





def qb_scraper():
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

    df.to_csv("Fantasy-Projector/playerData.csv")               
    df1.to_csv("Fantasy-Projector/playerData.csv", mode= "a")
    df2.to_csv("Fantasy-Projector/playerData.csv", mode= "a")

def wr_scraper(): 
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
    df.to_csv("Fantasy-Projector/playerData.csv", mode= "a")          
    df1.to_csv("Fantasy-Projector/playerData.csv", mode= "a")
    df2.to_csv("Fantasy-Projector/playerData.csv", mode= "a")

def rb_scraper():
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

    RBdf.to_csv("Fantasy-Projector/playerData.csv", mode= "a")
    RBdf1.to_csv("Fantasy-Projector/playerData.csv", mode= "a")    
    RBdf2.to_csv("Fantasy-Projector/playerData.csv", mode= "a")    

def te_scraper():
    wr_week1 = []
    wr_week2= []
    wr_week3= []

    for week in range(9,19):
        url = 'https://www.fantasypros.com/nfl/stats/te.php?year=2023&week={}&range=week'.format(week)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find('table').find('tbody').find_all('tr')
            
        for row in rows:
                if week == 9:
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
                    
                if week == 10:
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
                    
                if week == 11:
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

    df.to_csv("Fantasy-Projector/playerData.csv", mode= "a")             
    df1.to_csv("Fantasy-Projector/playerData.csv", mode= "a")
    df2.to_csv("Fantasy-Projector/playerData.csv", mode= "a")


def k_scraper():
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

    df.to_csv("Fantasy-Projector/playerData.csv", mode= "a")  
    df1.to_csv("Fantasy-Projector/playerData.csv", mode= "a")
    df2.to_csv("Fantasy-Projector/playerData.csv", mode= "a")



def main():
    qb_scraper()
    rb_scraper()
    wr_scraper()
    te_scraper()
    k_scraper()
    print("Done.")
    

if __name__ == "__main__":
    main()