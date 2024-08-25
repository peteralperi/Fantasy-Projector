'''

Author: Peter Alperi

This is the file that scrapes all the player statistics into the appropiate .csv files.

This scraper will get statistics of players from all fantasy relevant positions, including
Quarterback (QB), Running Back (RB), Wide Receiver (WR), Tight End (TE), and Kicker (K).
Along with the positions listed above, the scraper also has functions to scrape for player names, 
team abbreviations, and defensive statistics.


'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw





def qb_scraper():
    qb_list1 = []
    qb_list2 = []
    qb_list3 = []
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
                    qb_list1.append(dic)
                    
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
                    qb_list2.append(dic1)
                    
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
                    qb_list3.append(dic2)
   
    df = pd.DataFrame(qb_list1)
    df1 = pd.DataFrame(qb_list2)
    df2 = pd.DataFrame(qb_list3)

    df.to_csv("playerData.csv")               
    df1.to_csv("playerData.csv", mode= "a")
    df2.to_csv("playerData.csv", mode= "a")

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
    df.to_csv("playerData.csv", mode= "a")          
    df1.to_csv("playerData.csv", mode= "a")
    df2.to_csv("playerData.csv", mode= "a")

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

    RBdf.to_csv("playerData.csv", mode= "a")
    RBdf1.to_csv("playerData.csv", mode= "a")    
    RBdf2.to_csv("playerData.csv", mode= "a")    

def te_scraper():
    wr_week1 = []
    wr_week2= []
    wr_week3= []

    for week in range(16,19):
        url = 'https://www.fantasypros.com/nfl/stats/te.php?year=2023&week={}&range=week'.format(week)
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

    df.to_csv("playerData.csv", mode= "a")  
    df1.to_csv("playerData.csv", mode= "a")
    df2.to_csv("playerData.csv", mode= "a")


def player_scraper():
    
    url = ('https://www.pro-football-reference.com/years/2023/fantasy.htm#')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table rows in the table containing fantasy stats
    rows = soup.find_all('tr')
    players_list=[]
    # Loop through the rows to extract player names and teams
    for row in rows:
        dic = {}
        player_td = row.find('td', {'data-stat': 'player'})
        team_td = row.find('td', {'data-stat': 'team'})
        pos_td = row.find('td', {'data-stat': 'fantasy_pos'})

        if player_td and team_td:
            player_name = player_td.get_text()
            team_name = team_td.get_text()
            position = pos_td.get_text()
            
            if '*' in player_name:
                player_name = player_name.replace('*', '')
            
            if '+' in player_name:
                player_name = player_name.replace('+', '')
            
            dic['Player'] = player_name
            dic['Team'] = team_name
            dic['Position'] = position
            players_list.append(dic)
        

    df = pd.DataFrame(players_list)
    df.to_csv("Players.csv")



def defense_scraper():
    players_list = []
    players_list1 = []

    defense_choice = ["passing", "rushing"]

    for i in range(0,2):

        url = 'https://www.nfl.com/stats/team-stats/defense/{}/2023/reg/all'.format(defense_choice[i])

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
                for key in dic.keys():
                    t = dic[key]
                    if ' ' in t:
                        t = t.replace(' ', '')
                    if '\n' in t:
                        t = t.replace('\n', '')
                    dic[key] = t
                players_list.append(dic) 
                
        if i == 1:
            for row in rows:
                dic1 = {}
                            
                dic1['Team'] = row.find('td').find('div', class_='d3-o-club-shortname').text
                dic1['ryds'] = row.find_all('td')[2].text
                dic1['rTds'] = row.find_all('td')[4].text
                dic1['fumbs'] = row.find_all('td')[10].text
                
                for key in dic1.keys():
                    t = dic1[key]
                    if ' ' in t:
                        t = t.replace(' ', '')
                    if '\n' in t:
                        t = t.replace('\n', '')
                    dic1[key] = t
                players_list1.append(dic1)
                
    df = pd.DataFrame(players_list)
    df1 = pd.DataFrame(players_list1)

    df.to_csv("defenseStats.csv")             
    df1.to_csv("defenseStats.csv", mode= "a")

def main():
    qb_scraper()
    rb_scraper()
    wr_scraper()
    te_scraper()
    k_scraper()
    player_scraper()
    defense_scraper()
    print("Done.")
    

if __name__ == "__main__":
    main()