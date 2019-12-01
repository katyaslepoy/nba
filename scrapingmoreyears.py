from urllib.request import urlopen, urlretrieve

import pandas as pd
from bs4 import BeautifulSoup
from unidecode import unidecode




"""I used this code to download all the pictures once. It takes about half an hour to run.
Now instead of scraping the web for a headshot every time you click a players name, it just pulls it from the 
headshots file. Now it takes fraction of a second to load a player instead of 5 or 6 seconds. Folder
isn't that big. 66.2 MB
I also used it to  load and save main data table as a pkl so that doesnt happen every time program runs."""



    # URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_2020_totals.html"
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html, features="html.parser")

    # use findALL() to get the column headers
soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
    # avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]for i in range(len(rows))]
stats = pd.DataFrame(player_stats, columns=headers)
players = []
rowcount = 0
    # saves to csv
stats.to_csv('stats2020.csv')
