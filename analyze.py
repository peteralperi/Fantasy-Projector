import csv
from datetime import datetime


def store_user_input(input_string):
    global user_input
    user_input = input_string
    player = user_input
    week = 1 #This variable will also be given. hopefully from datetime
    position = get_position(player)
    position = position.lower() #Converts to lowercase for other functions
    team = get_team(player)
    date = get_week()
    print(date)
    opponent = get_opponent(team, week)
    if ' ' in opponent:
        opponent = opponent.replace(' ', '')
    if '@' in opponent:
        opponent = opponent.replace('@', '')
        
    player_stats = read_playerData(player)
    player_avg = avg_stats(player_stats, position)
    
    fantasy_avg = fantasy_conversion(player_avg, position)
    
    score = analyze(fantasy_avg, opponent, position)
    score = round(score, 2)
    print(score)

    return score


def get_week():
    date = datetime.now()
    currdate = date.strftime("%m/%Y")
    return currdate
    
    

def get_position(player_name):
    position = ''
    with open("Players.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == player_name:
                    position = row[3]
    if position:
        return position
    
def get_team(player_name):
    with open("Players.csv", mode='r', newline='') as file:
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


def read_playerData(player_name):
    with open("playerData.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        player_data = []
        for row in csv_reader:
            if row[1] == player_name:
                    player_data.append(row) 
    return player_data


def avg_stats(data, pos):
    if pos == 'wr' or  pos =='te': #wide receivers, running backs, and tight ends all share the same fantasy football relevant stats, called wr_stats
        wr_stats = {
            'rYds': 0,
            'rTds': 0,
            'recs': 0,
            'recYds': 0,
            'recTds': 0,
            'fumbs': 0,
            'games': 0
        }
        
        
        #,Player,recs,recYds,recTds,rYds,rTds,fumbs,games
        
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
    
    if pos == 'rb':
        rb_stats = {
            'rYds': 0,
            'rTds': 0,
            'recs': 0,
            'recYds': 0,
            'recTds': 0,
            'fumbs' : 0,
            'games' : 0
        }
        
        
        for game in data:
            rb_stats['rYds'] += int(game[2])
            rb_stats['rTds'] += int(game[3])
            rb_stats['recs'] += int(game[4])
            rb_stats['recYds'] += int(game[5])
            rb_stats['recTds'] += int(game[6])
            rb_stats['fumbs'] += int(game[7])
            rb_stats['games'] += int(game[8])

        for key in rb_stats.keys():
            if key != 'games':
                rb_stats[key] = rb_stats[key] / rb_stats['games']
                
        return rb_stats
    
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
    
    league_avg_pyds = 0
    league_avg_ptds = 0
    league_avg_ints = 0
    league_avg_ryds = 0
    league_avg_rtds = 0
    league_avg_fumbs = 0
    
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
        'SFO': '49ers',
        'SEA': 'Seahawks',
        'TB': 'Buccaneers',
        'TN': 'Titans',
        'WSH': 'Commanders',
    }
    
    
    
    team_name = team_names[opp]
    
    with open('defenseStats.csv', mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        i = 1
        for row in csv_reader:
            if row[1] == team_name:
                opp_pyds = int(row[2])
                opp_ptds = int(row[3])
                opp_ints = int(row[4])
                
            if i > 1  and i <= 33:
                league_avg_pyds += int(row[2])
                league_avg_ptds += int(row[3])
                league_avg_ints += int(row[4])
                
            
            if i > 34  and i <= 67:
                if row[1] == team_name:
                    opp_ryds = int(row[2])
                    opp_rtds = int(row[3])
                    opp_fumbs = int(row[4])
                league_avg_ryds += int(row[2])
                league_avg_rtds += int(row[3])
                league_avg_fumbs += int(row[4])

            
            i+=1
        
        
        if pos != 'k':
            league_avg_pyds /= 32
            diff_pyds = league_avg_pyds - opp_pyds
            if diff_pyds >= 0:
                pyds_percent = diff_pyds / league_avg_pyds
                if pyds_percent <.333:
                    base += .6
                elif pyds_percent <.666:
                    base += 1.4
                else:
                    base += 2
            else:
                pyds_percent = abs(diff_pyds) / league_avg_pyds
                if pyds_percent <.333:
                    base -= .6
                elif pyds_percent <.666:
                    base -= 1.4
                else:
                    base -= 2
                    
            
            league_avg_ptds /= 32
            
            diff_ptds = league_avg_ptds - opp_ptds
            if diff_ptds >= 0:
                ptds_percent = diff_ptds / league_avg_ptds
                if ptds_percent <.333:
                    base += .6
                elif ptds_percent <.666:
                    base += 1.4
                else:
                    base += 2
            else:
                ptds_percent = abs(diff_ptds) / league_avg_ptds
                if ptds_percent <.333:
                    base -= .6
                elif ptds_percent <.666:
                    base -= 1.4
                else:
                    base -= 2
            
            league_avg_ints /= 32
            
            
            if pos == 'qb':
                diff_ints = league_avg_ints - opp_ints
                if diff_ints >= 0:
                    ints_percent = diff_ints / league_avg_ints
                    if ints_percent <.333:
                        base += .3
                    elif ptds_percent <.666:
                        base += .6
                    else:
                        base += .9
                else:
                    ints_percent = abs(diff_ints) / league_avg_ints
                    if ints_percent <.333:
                        base -= .3
                    elif ints_percent <.666:
                        base -= .6
                    else:
                        base -= .9
                        
        if pos == 'rb':     
            league_avg_ryds /= 32
            diff_ryds = league_avg_ryds - opp_ryds
            if diff_ryds >= 0:
                ryds_percent = diff_ryds / league_avg_ryds
                if ryds_percent <.333:
                    base += .6
                elif ryds_percent <.666:
                    base += 1.4
                else:
                    base += 2
            else:
                ryds_percent = abs(diff_ryds) / league_avg_ryds
                if pyds_percent <.333:
                    base -= .6
                elif pyds_percent <.666:
                    base -= 1.4
                else:
                    base -= 2
            
            
            league_avg_rtds /= 32
            diff_rtds = league_avg_rtds - opp_rtds
            if diff_rtds >= 0:
                rtds_percent = diff_rtds / league_avg_rtds
                if rtds_percent <.333:
                    base += .6
                elif rtds_percent <.666:
                    base += 1.4
                else:
                    base += 2
            else:
                rtds_percent = abs(diff_rtds) / league_avg_rtds
                if ptds_percent <.333:
                    base -= .6
                elif ptds_percent <.666:
                    base -= 1.4
                else:
                    base -= 2
            league_avg_fumbs /= 32
            diff_fumbs = league_avg_fumbs - opp_fumbs
            if diff_fumbs >= 0:
                fumbs_percent = diff_fumbs / league_avg_fumbs
                if fumbs_percent <.333:
                    base += .6
                elif fumbs_percent <.666:
                    base += 1.4
                else:
                    base += 2
            else:
                fumbs_percent = abs(diff_fumbs) / league_avg_fumbs
                if fumbs_percent <.333:
                    base -= .6
                elif fumbs_percent <.666:
                    base -= 1.4
                else:
                    base -= 2
            
    return base

       
        
    
def main():
    player = "Breece Hall" #This variable will be given from website
    week = 1 #This variable will also be given. hopefully from datetime
    position = get_position(player)
    position = position.lower() #Converts to lowercase for other functions
    team = get_team(player)
    get_week()
    opponent = get_opponent(team, week)
    if ' ' in opponent:
        opponent = opponent.replace(' ', '')
    if '@' in opponent:
        opponent = opponent.replace('@', '')
        
    player_stats = read_playerData(player)
    player_avg = avg_stats(player_stats, position)
    
    fantasy_avg = fantasy_conversion(player_avg, position)
    
    score = analyze(fantasy_avg, opponent, position)
    print(score)
    

if __name__ == "__main__":
    main()