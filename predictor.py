import math
from copy import deepcopy

import pandas as pd

stats = pd.read_csv('venv/stats2020.csv')
rowcount = 0
co = 0
players = []

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

for t in Teams:
    t.insert(0,0)
    t.insert(0, [])
    t.insert(0, 0)
for rowcount in range(0, len(stats)):
    player = stats.loc[rowcount, 'Player']
    if player == '' or player == ' ' or pd.isnull(player):
        continue
    team = stats.loc[rowcount, 'Tm']
    pts = float(stats.iat[rowcount, stats.columns.get_loc('PTS')])
    BLK = float(stats.iat[rowcount, stats.columns.get_loc('BLK')])
    stl = float(stats.iat[rowcount, stats.columns.get_loc('STL')])
    FT = float(stats.iat[rowcount, stats.columns.get_loc('FT')])
    pf = float(stats.iat[rowcount, stats.columns.get_loc('PF')])
    efg = float(stats.iat[rowcount, stats.columns.get_loc('eFG%')])
    tov = float(stats.iat[rowcount, stats.columns.get_loc('TOV')])
    fga = float(stats.iat[rowcount, stats.columns.get_loc('FGA')])
    TRB = float(stats.iat[rowcount, stats.columns.get_loc('TRB')])
    G = stats.loc[rowcount, 'G']
    efg = stats.loc[rowcount, 'eFG%']
    try:
        rating = (TRB + tov + FT + stl)
        # rating = (pts/2)*(TRB+tov+FT+stl)+(BLK/pf)
        if fga > 10:
            if efg > .5:
                rating += (rating * efg)
            else:
                rating -= (rating * efg)
    except ZeroDivisionError:
        rating = 0
    if pd.isnull(rating):
        continue
    for t in Teams:
        if team in t[3]:
            t[1].append(G)
            t[2] += pts
            t[0] += rating
for t in Teams:
    t[0] /= max(t[1])
    t[2] /= max(t[1])
Teams.sort(reverse=True)
for i in Teams:
    print(i[0], i[3])


def predict(a, b):
    a_rate = 0
    b_rate = 0
    a_stars = []
    b_stars = []
    arank = 1
    apts = 0
    bpts = 0
    brank = 1
    afinalrank = 0
    bfinalrank = 0
    for t in Teams:
        if a in t:
            a_rate = t[0]
            apts = t[2]
            afinalrank = arank
        if b in t:
            b_rate = t[0]
            bpts = t[2]
            bfinalrank = brank
        arank += 1
        brank += 1
    alist = [a, a_rate, a_stars, afinalrank, apts]
    blist = [b, b_rate, b_stars, bfinalrank, bpts]
    if a_rate > b_rate:
        higher = alist
        lower = blist
    else:
        lower = alist
        higher = blist
    chances = ((lower[1] * 100) / higher[1])

    print("%s has a %g percent chance of beating %s." % (
        higher[0], 150 - chances, lower[0]))
    print("Predicted score: %d to %d" % (higher[4]+((chances/100)*5), lower[4]))
    print("%s is ranked #%d overall" % (higher[0], higher[3]))
    print("%s is ranked #%d overall" % (lower[0], lower[3]))


choices = input('Enter first team: ')
choices2 = input('enter second team: ')
a = ''
b = ''
for t in Teams:
    if choices.lower() in t[3].lower():
        a = t[4]
    elif choices2.lower() in t[3].lower():
        b = t[4]
predict(a, b)
print("The team we currently predict to win the season is %s" % (Teams[0][3]))
