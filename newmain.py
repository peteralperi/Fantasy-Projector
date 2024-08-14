import csv
from datetime import datetime



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
    
def main():
    file = "playerData.csv"
    player = "Patrick Mahomes II"
    data = read_playerData(file, player)
    avg = avg_stats(data, 'qb')
    fantasy_avg = fantasy_conversion(avg, 'qb')
    get_week()
    

if __name__ == "__main__":
    main()