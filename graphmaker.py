import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# make graphs of everything
files = []
for y in range(17, 20):
    files.append('C:/Users/katya/PycharmProjects/teammamba/venv/stats20%s.csv' % y)

stats = pd.concat(map(pd.read_csv, files))
headers = stats.columns.values

from itertools import chain

headers2 = list(chain(headers[8:]))
h = headers[29]
x = []
y = []
list = []
co = 0
playerppg = dict()
ppglist = []

while co < len(stats):
    lastplayer = stats.iat[co, 1]
    if pd.isnull(lastplayer) or lastplayer is None or lastplayer == "Empty":
        co += 1
        continue
    if not pd.isnull(stats.iat[co, stats.columns.get_loc('G')]) and stats.iat[co, stats.columns.get_loc('G')]>50:
        playerppg.setdefault(lastplayer,[]).append([stats.iat[co, stats.columns.get_loc('PTS')] / stats.iat[co, stats.
                                              columns.get_loc('G')]])
    else:
        co+=1
        continue
    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1
lister=[]
for i in playerppg:
    if len(playerppg[i]) > 2:
        lister.append((playerppg[i][2][0]-playerppg[i][0][0], i,playerppg[i][0][0],playerppg[i][1][0],playerppg[i][2][0] ))
lister.sort(reverse=True)
print(lister)
total1=0
total2=0
total3=0
count=0
for i in lister:
    total1+=i[2]
    total2+=i[3]
    total3+=i[4]
    count+=1
total1/=count
total2/=count
total3/=count
year=[2017,2018,2019]
Ingram=[playerppg['Brandon Ingram'][0][0],playerppg['Brandon Ingram'][1][0],playerppg['Brandon Ingram'][2][0]]
Oubre=[playerppg['Kelly Oubre'][0][0],playerppg['Kelly Oubre'][1][0],playerppg['Kelly Oubre'][2][0]]
Dinwiddie=[playerppg['Spencer Dinwiddie'][0][0],playerppg['Spencer Dinwiddie'][1][0],playerppg['Spencer Dinwiddie'][2][0]]
Siakam=[playerppg['Pascal Siakam'][0][0],playerppg['Pascal Siakam'][1][0],playerppg['Pascal Siakam'][2][0]]
Murray=[playerppg['Jamal Murray'][0][0],playerppg['Jamal Murray'][1][0],playerppg['Jamal Murray'][2][0]]
avg=[total1,total2,total3]
df = pd.DataFrame(zip(year,Ingram,Oubre,Dinwiddie,Siakam,Murray,avg), columns=['year','Brandon Ingram','Kelly Oubre','Spencer Dinwiddie','Pascal Siakam','Jamal Murray', 'Average'])
print(df)
df.to_csv("improving.csv")

