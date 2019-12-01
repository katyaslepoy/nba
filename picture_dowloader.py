import csv
import urllib
from urllib.request import urlopen, urlretrieve

import pandas as pd
from bs4 import BeautifulSoup
from unidecode import unidecode

row2 = 0


for year in range(10,21):
    files = []

    df = pd.read_csv('venv\stats20%.csv'%year)

    players = []
    rowcount = 0
    for row in df.iterrows():
        if rowcount < len(df):
            lastplayer = df.iat[rowcount, 1]
            if lastplayer is None:
                rowcount += 1
                continue
            if lastplayer not in players:
                players.append(lastplayer)

            while rowcount + 1 < len(df) and lastplayer == df.iat[rowcount + 1, 1]:
                rowcount += 1
            rowcount += 1
        else:
            break

    for player in players:
        try:
            firstandlast = player.split()
        except AttributeError:
            continue
        print("Saved")
        first = firstandlast[0]
        newfirst = ''
        # strips dots from first name
        if '.' in first:
            for char in first:
                if char.isalpha():
                    newfirst += char
                    first = newfirst

        last = firstandlast[1].strip('*')
        picstring = "https://www.foxsports.com/nba/%s-%s-player-stats" % (unidecode(first), unidecode(last))
        print(picstring)
        url = picstring
        html2 = urlopen(url)
        soup2 = BeautifulSoup(html2, features="html.parser")
        # try-except places empty photo if site doesnt have an image
        try:
            imgs = soup2.find("img", attrs={'class': 'wisfb_headshotImage wisfb_bioLargeImg'}).get('src')

            urlretrieve(imgs, '/Users/katya/PycharmProjects/teammamba/newheadshots/%s-%s.jpg' % (
            unidecode(first), unidecode(last)))
        except ValueError:
            continue
        except AttributeError:
            continue

        print("%s: saving..." % player)


