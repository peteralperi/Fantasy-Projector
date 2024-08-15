import csv
from datetime import datetime

def get_position(file, player_name):
    with open(file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == player_name:
                    position = row[3]
    if position:
        return position
    
def get_team(file, player_name):
    with open(file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == player_name:
                    team = row[2]
    if team:
        return team


def get_opponent(team, week):
    with open("2024_schedule.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == team:
                    opponent = row[week]
    return opponent


def read_playerData(file_path, player_name):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        player_data = []
        for row in csv_reader:
            if row[1] == player_name:
                    player_data.append(row) 
    return player_data


def avg_stats(data, pos):
    if pos == 'wr' or pos == 'rb' or pos =='te': #wide receivers, running backs, and tight ends all share the same fantasy football relevant stats, called wr_stats
        wr_stats = {
            'rYds': 0,
            'rTds': 0,
            'recs': 0,
            'recYds': 0,
            'recTds': 0,
            'fumbs': 0,
            'games': 0
        }
        
        if pos == 'rb':
            for game in data:
                wr_stats['rYds'] += int(game[2])
                wr_stats['rTds'] += int(game[3])
                wr_stats['recs'] += int(game[4])
                wr_stats['recYds'] += int(game[5])
                wr_stats['recTds'] += int(game[6])
                wr_stats['fumbs'] += int(game[7])
                wr_stats['games'] += int(game[8])
        #,Player,recs,recYds,recTds,rYds,rTds,fumbs,games
        if pos == 'wr' or pos == 'te':
            for game in data:
                wr_stats['rYds'] += int(game[5])
                wr_stats['rTds'] += int(game[6])
                wr_stats['recs'] += int(game[2])
                wr_stats['recYds'] += int(game[3])
                wr_stats['recTds'] += int(game[4])
                wr_stats['fumbs'] += int(game[7])
                wr_stats['games'] += int(game[8])
       
        
        for key in wr_stats.keys():
            if key != 'games':
                wr_stats[key] = wr_stats[key] / wr_stats['games']
                
        return wr_stats
    
    #,Player,pYds,pTds,ints,rYds,rTds,fumbs,games
    if pos == 'qb':
        qb_stats = {
            'pYds': 0,
            'pTds': 0,
            'ints': 0,
            'rYds': 0,
            'rTds': 0,
            'fumbs': 0,
            'games': 0
        }
        
        
        for game in data:
            qb_stats['pYds'] += int(game[2])
            qb_stats['pTds'] += int(game[3])
            qb_stats['ints'] += int(game[4])
            qb_stats['rYds'] += int(game[5])
            qb_stats['rTds'] += int(game[6])
            qb_stats['fumbs'] += int(game[7])
            qb_stats['games'] += int(game[8])
        
        for key in qb_stats.keys():
            if key != 'games':
                qb_stats[key] = qb_stats[key] / qb_stats['games']
                
        return qb_stats
    
    
    #,Player,FG,FGA,1-19,20-29,30-39,40-49,50+,XPT,games
    if pos == 'k':
        k_stats = { 
            'FG': 0,
            'FGA': 0,
            'tier1': 0,
            'tier2': 0,
            'tier3': 0,
            'tier4': 0,
            'tier5': 0,
            'XPT': 0,
            'games': 0
        }
        
        
        for game in data:
            k_stats['FG'] += int(game[2])
            k_stats['FGA'] += int(game[3])
            k_stats['tier1'] += int(game[4])
            k_stats['tier2'] += int(game[5])
            k_stats['tier3'] += int(game[6])
            k_stats['tier4'] += int(game[7])
            k_stats['tier5'] += int(game[8])
            k_stats['XPT'] += int(game[9])
            k_stats['games'] += int(game[10])
        
        for key in k_stats.keys():
            if key != 'games':
                k_stats[key] = k_stats[key] / k_stats['games']
                
        return k_stats
        
        



def fantasy_conversion(avg, pos):
    base_fantasy = 0
    if pos == 'wr' or pos == 'te' or pos == 'rb':
        base_fantasy += avg['rYds'] / 10
        base_fantasy += avg['rTds'] * 6
        base_fantasy += avg['recs'] 
        base_fantasy += avg['recYds'] / 10
        base_fantasy += avg['recTds'] * 6
        base_fantasy += avg['fumbs'] * -2
    
    if pos == 'qb':
        base_fantasy += avg['pYds'] / 25
        base_fantasy += avg['pTds'] * 4
        base_fantasy += avg['ints'] * -2
        base_fantasy += avg['rYds'] / 10
        base_fantasy += avg['rTds'] * 6
        base_fantasy += avg['fumbs'] * -2
    
    if pos == 'k':
        base_fantasy += avg['tier1'] * 3
        base_fantasy += avg['tier2'] * 3.5
        base_fantasy += avg['tier3'] * 3.5
        base_fantasy += avg['tier4'] * 4.5
        base_fantasy += avg['tier5'] * 5.5
        base_fantasy += avg['XPT'] 
            
    return base_fantasy

def get_week():
    cur_date = datetime.now()
    
def analyze(base, opp, pos):
    
    team_names = {
        'ARI': 'Cardinals',
        'ATL': 'Falcons',
        'BAL': 'Ravens',
        'BUF': 'Bills',
        'CAR': 'Panthers',
        'CHI': 'Bears',
        'CIN': 'Bengals',
        'CLE': 'Browns',
        'DAL': 'Cowboys',
        'DEN': 'Broncos',
        'DET': 'Lions',
        'GB': 'Packers',
        'HOU': 'Texans',
        'IND': 'Colts',
        'JAX': 'Jaguars',
        'KC': 'Chiefs',
        'LV': 'Raiders',
        'LAR': 'Rams',
        'LAC': 'Chargers',
        'MIA': 'Dolphins',
        'MIN': 'Vikings',
        'NE': 'Patriots',
        'NO': 'Saints',
        'NYG': 'Giants',
        'NYJ': 'Jets',
        'PHI': 'Eagles',
        'PIT': 'Steelers',
        'SF': '49ers',
        'SEA': 'Seahawks',
        'TB': 'Buccaneers',
        'TN': 'Titans',
        'WSH': 'Commanders',
    }
    #defenseStats 1, team name     2, pyds/attempts    3, ptds/ryds   4, ints/ypc   
    team_name = team_names[opp]
    if pos == 'wr' or pos == 'te' or pos == 'rb':
        with open('defenseStats.csv', mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            i = 0
            for row in csv_reader:
                
                t = row[1]
                if ' ' in t:
                    t = t.replace(' ', '')
                if '\n' in t:
                    t = t.replace('\n', '')
                if t == team_name:
                    team_stats = [row]
                
                    
                i += 1
                
       
        
    
def main():
    data_file = "playerData.csv"
    pos_file = "Players.csv"
    player = "Tyreek Hill" #This variable will be given from website
    week = 1 #This variable will also be given. hopefully from datetime
    position = get_position(pos_file, player)
    position = position.lower() #Converts to lowercase for other functions
    team = get_team(pos_file, player)
    
    opponent = get_opponent(team, week)
    if ' ' in opponent:
        opponent = opponent.replace(' ', '')
        
    player_stats = read_playerData(data_file, player)
    player_avg = avg_stats(player_stats, position)
    fantasy_avg = fantasy_conversion(player_avg, position)
    analyze(fantasy_avg, opponent, position)
    
    

if __name__ == "__main__":
    main()