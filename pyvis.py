import networkx as nx
import pandas as pd
from copy import deepcopy
import matplotlib.pyplot as plt

net = nx.Graph()
Teams = [
    ['ATL', 'Atlanta Hawks'],
    ['BRK', 'Brooklyn Nets'],
    ['BOS', 'Boston Celtics'],
    ['CHO', 'Charlotte Hornets'],
    ['CHI', 'Chicago Bulls'],
    ['CLE', 'Cleveland Cavaliers'],
    ['DAL', 'Dallas Mavericks'],
    ['DEN', 'Denver Nuggets'],
    ['DET', 'Detroit Pistons'],
    ['GSW', 'Golden State Warriors'],
    ['HOU', 'Houston Rockets'],
    ['IND', 'Indiana Pacers'],
    ['LAC', 'Los Angeles Clippers'],
    ['LAL', 'Los Angeles Lakers'],
    ['MEM', 'Memphis Grizzlies'],
    ['MIA', 'Miami Heat'],
    ['MIL', 'Milwaukee Bucks'],
    ['MIN', 'Minnesota Timberwolves'],
    ['NOP', 'New Orleans Pelicans'],
    ['NYK', 'New York Knicks'],
    ['OKC', 'Oklahoma City Thunder'],
    ['ORL', 'Orlando Magic'],
    ['PHI', 'Philadelphia 76ers'],
    ['PHO', 'Phoenix Suns'],
    ['POR', 'Portland Trail Blazers'],
    ['SAC', 'Sacramento Kings'],
    ['SAS', 'San Antonio Spurs'],
    ['TOR', 'Toronto Raptors'],
    ['UTA', 'Utah Jazz'],
    ['WAS', 'Washington Wizards']
]
list1 = []
list2 = []
players = []
counter = 0
x = 0
newteamlist=[]
for year in range(10, 21):
    stats = pd.read_csv('C:/Users/katya/PycharmProjects/teammamba/venv/stats20%s.csv' % year)
    newteamlist.append((year, deepcopy(Teams)))
    for x in newteamlist:
        if x[0]==year:
            for rowcount in range(0,len(stats)):
                if stats.iat[rowcount,stats.columns.get_loc('PTS')]>1300:
                    player=stats.iat[rowcount,1]
                    team=stats.iat[rowcount,4]

                    for i in x[1]:
                        if team==i[0]:
                            i.append(player)
                            if player not in players:
                                players.append(player)
player1=[]
player2=[]
for x in newteamlist:
    for xx in x[1]:
        for xxx in xx[2:]:
            for xxxx in xx[2:]:
                player1.append(xxx)
                player2.append(xxxx)


list3 = []
for i in player1:
    list3.append(1)
df = pd.DataFrame(list(zip(player1, player2, list3)),
                  columns=['Player', 'Teammate', 'weight'])
print(df)
list4=[]
for p in players:
    list4.append(p)
df2=pd.DataFrame(list4)
print(df2)
df.to_csv('starteams.csv')
df2.to_csv('nodes.csv')
