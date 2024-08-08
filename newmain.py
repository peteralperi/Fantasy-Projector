import csv




def read_playerData(file_path, player_name):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        player_data = []
        for row in csv_reader:
            if row[1] == player_name:
                    player_data.append(row)
    return player_data

#,Player,rYds,rTds,recs,recYds,recTds,fumbs,games
#,Player,recs,recYds,recTds,rYds,rTds,fumbs,games
def avg_stats(data, pos):
    print(data)
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
            'tieir5': 0,
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
            k_stats['tier5'] += int(game[9])
            k_stats['XPT'] += int(game[10])
            k_stats['games'] += int(game[11])
        
        for key in k_stats.keys():
            if key != 'games':
                k_stats[key] = k_stats[key] / k_stats['games']
                
        return k_stats
        
        

def main():
    file = "playerData.csv"
    player = "George Pickens"
    data = read_playerData(file, player)
    result = avg_stats(data, 'wr')
    print(result)
    

if __name__ == "__main__":
    main()