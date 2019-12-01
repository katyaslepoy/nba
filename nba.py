import copy
from tkinter import *
import unidecode
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load pkl as pandas dataframe
stats = pd.read_csv('venv/stats2019.csv')

# store headers as list
headers = stats.columns.values

# lists for displaying data later
players = []
rowcount = 0

statscopy = stats.dropna(how='all')
statscopy = stats.drop_duplicates(subset="Player")

# add players to a list skipping duplicates and empties
for row in stats.iterrows():
    if rowcount < len(stats) - 1:
        lastplayer = stats.iat[rowcount, 1]
        if lastplayer is None:
            rowcount += 1
            continue
        players.append(lastplayer)

        while lastplayer == stats.iat[rowcount + 1, 1] and rowcount < len(stats) - 2:
            rowcount += 1
        rowcount += 1
    else:
        break
# store teams
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
fullteam = []
for x in Teams:
    fullteam.append(x[1])
positions = [("SF", "Small Forward"), ("PG", "Point Guard"), ("C", "Center"), ("SG", "Shooting Guard"), ("PF", "Power "
                                                                                                               "Forward")]

files = []
for y in range(10, 20):
    files.append('C:/Users/katya/PycharmProjects/teammamba/venv/stats20%s.csv' % y)

stats = pd.concat(map(pd.read_csv, files))
from pylab import *
list = []
agep = dict()
age=[]
pts = []
aged = dict()
co = 0
while co < len(stats):
    lastplayer = stats.iat[co, 1]
    if pd.isnull(lastplayer) or lastplayer is None or lastplayer == "Empty":
        co += 1
        continue
    agep[stats.iat[co, 3]]=agep.get(stats.iat[co,3], 0)+ stats.iat[co, stats.columns.get_loc('PTS')]
    aged[stats.iat[co, 3]] = aged.get(stats.iat[co, 3], 0) + 1
    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1

for i in sorted(agep):
    age.append(i)
    p=int(agep[i]/int(aged[i]))
    pts.append(p)

plt.plot(age, pts)
plt.xlabel('Age')
plt.ylabel('Pts Scored')
plt.xticks(np.arange(19,45,1))
plt.grid(True)
plt.yticks(np.arange(200, 700, 100))
plt.title("Average Points Scored by Age 2010-2019")
plt.show()

# attempting to plot which positions make the most points
SF = 0
PG = 0
C = 0
SG = 0
PF = 0
co = 0
x = []
y = []
while co < len(stats):
    lastplayer = stats.iat[co, 0]
    if stats.iat[co, 2] == 'SF':
        SF += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 2] == 'PG':
        PG += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 2] == 'C':
        C += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 2] == 'SG':
        SG += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 2] == 'PF':
        PF += int(stats.iat[co, stats.columns.get_loc('PTS')])

    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1

x.append('SF')
x.append('PG')
x.append('C')
x.append('SG')
x.append('PF')
y.append(SF)
y.append(PG)
y.append(C)
y.append(SG)
y.append(PF)
print(x, y)
y_pos = np.arange(len(x))
plt.bar(y_pos, y, align='center', alpha=.5)
plt.xticks(y_pos, x)
plt.ylabel('Points')
plt.title('Points Scored by Positions 2019')

plt.show()

# attempting to plot points by team
co = 0
xx = []
for f in Teams:
    xx.append([f[0], int(0)])
while co < len(stats):
    for t in xx:
        if stats.iat[co, stats.columns.get_loc('Tm')] == t[0]:
            t[1] += int(stats.iat[co, stats.columns.get_loc('PTS')])
    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1

tms = []
pt = []
for i in xx:
    tms.append(i[0])
    pt.append(i[1])
colors = []
y_pos = np.arange(len(tms))
for z in tms:
    if z == 'TOR':
        colors.append('r')
    else:
        colors.append('b')
plt.bar(y_pos, pt, align='center', alpha=.5, color=colors)
plt.xticks(y_pos, tms, rotation=45)
plt.ylim(8000, 10000)
plt.yticks(np.arange(8000, 10000, 100))
plt.ylabel('Points')
plt.title('Points Scored by Teams')

plt.show()

# top 5 players by position
FG = 0
ThP = 0
TwP = 0
TRB = 0
AST = 0
BLK = 0
F = 0
MP = 0
SF = []
PF = []
C = []
PG = []
SG = []
rc = 0
while rc < len(stats):
    guy = stats.iat[rc, 0]
    if pd.isnull(guy) or guy is None or guy == ' ':
        rc += 1
        continue
    FG = float(stats.iat[rc, stats.columns.get_loc('FG')])
    ThP = float(stats.iat[rc, stats.columns.get_loc('3P')])
    TwP = float(stats.iat[rc, stats.columns.get_loc('2P')])
    TRB = float(stats.iat[rc, stats.columns.get_loc('TRB')])
    AST = float(stats.iat[rc, stats.columns.get_loc('AST')])
    BLK = float(stats.iat[rc, stats.columns.get_loc('BLK')])
    STL = float(stats.iat[rc, stats.columns.get_loc('STL')])
    F = float(stats.iat[rc, stats.columns.get_loc('PF')])
    G = float(stats.iat[rc, stats.columns.get_loc('G')])
    MP = float(stats.iat[rc, stats.columns.get_loc('MP')])
    try:
        ThP_ = float(stats.iat[rc, stats.columns.get_loc('3P%')])
    except ValueError:
        ThP_ = 0
    try:
        eFG_ = float(stats.iat[rc, stats.columns.get_loc('eFG%')])
    except ValueError:
        eFG_ = 0
    try:
        TwP_ = float(stats.iat[rc, stats.columns.get_loc('2P%')])
    except ValueError:
        TwP_ = 0
    try:
        FT_ = float(stats.iat[rc, stats.columns.get_loc('FT%')])
    except ValueError:
        FT_ = 0
    FTA = float(stats.iat[rc, stats.columns.get_loc('FTA')])
    ThPA = float(stats.iat[rc, stats.columns.get_loc('3PA')])
    TwPA = float(stats.iat[rc, stats.columns.get_loc('2PA')])
    FGA = float(stats.iat[rc, stats.columns.get_loc('FGA')])
    TOV = float(stats.iat[rc, stats.columns.get_loc('TOV')])
    try:
        rating = (FG + ThP + TwP + TRB + AST + BLK - + (FT_ * FTA) + TOV + ((G - 82) * 2) - F + STL + (
                (ThP_ + eFG_ + TwP_) * (ThPA + TwPA + FGA))) / MP
    except ZeroDivisionError:
        rating = 0
    pos_played = stats.iat[rc, stats.columns.get_loc('Pos')]
    if pos_played == 'SF':
        SF.append((rating, guy))
    elif pos_played == 'PF':
        PF.append((rating, guy))
    elif pos_played == 'C':
        C.append((rating, guy))
    elif pos_played == 'PG':
        PG.append((rating, guy))
    elif pos_played == 'SG':
        SG.append((rating, guy))
    while rc + 1 < len(stats) and str(guy) == stats.iat[rc + 1, 0]:
        rc += 1
    rc += 1
SG.sort(reverse=True)
PG.sort(reverse=True)
C.sort(reverse=True)
PF.sort(reverse=True)
SF.sort(reverse=True)

All = SG + PG + C + PF + SF
All.sort(reverse=True)
for i in range(0, 6):
    print(All[i][1])
for i in range(0, 7):
    print("#%d:SG:%s\nPG:%s\nC:%s\nSF:%s\nPF:%s" % (
        i, SG[i][1], PG[i][1], C[i][1], SF[i][1], PF[i][1]))
# attempting to plot which positions make the most points
SF = 0
PG = 0
C = 0
SG = 0
PF = 0
co = 0
x = []
y = []
while co < len(stats):
    lastplayer = stats.iat[co, 0]
    if stats.iat[co, 1] == 'SF':
        SF += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 1] == 'PG':
        PG += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 1] == 'C':
        C += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 1] == 'SG':
        SG += int(stats.iat[co, stats.columns.get_loc('PTS')])
    elif stats.iat[co, 1] == 'PF':
        PF += int(stats.iat[co, stats.columns.get_loc('PTS')])

    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1

x.append('SF')
x.append('PG')
x.append('C')
x.append('SG')
x.append('PF')
y.append(SF)
y.append(PG)
y.append(C)
y.append(SG)
y.append(PF)
y_pos = np.arange(len(x))
plt.bar(y_pos, y, align='center', alpha=.5)
plt.xticks(y_pos, x)
plt.ylabel('Points')
plt.title('Points Scored by Positions')

plt.show()

files = []
for y in range(10, 20):
    files.append('C:/Users/katya/PycharmProjects/teammamba/venv/stats20%s.csv' % y)

stats = pd.concat(map(pd.read_csv, files))

# make graphs of everything
list = []
blks = []
pts = []
co = 0
while co < len(stats):
    lastplayer = stats.iat[co, 0]
    if pd.isnull(lastplayer) or lastplayer is None or lastplayer == "Empty":
        co += 1
        continue
    list.append((stats.iat[co, stats.columns.get_loc('PTS')], stats.iat[co, stats.columns.get_loc('AST')]))
    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1
for i in list:
    pts.append(int(i[0]))
    blks.append(int(i[1]))
plt.scatter(pts, blks)
plt.xlabel('Pts')
plt.ylabel('Asts')
plt.yticks(np.arange(min(blks), max(blks) + 1, 50))
plt.xticks(np.arange(min(pts), max(pts) + 1, 500))
plt.show()

list = []
age = []
pts = []
co = 0
while co < len(stats):
    lastplayer = stats.iat[co, 0]
    if pd.isnull(lastplayer) or lastplayer is None or lastplayer == "Empty":
        co += 1
        continue
    list.append((stats.iat[co, 2], stats.iat[co, stats.columns.get_loc('PTS')]))
    while co + 1 < len(stats) and str(lastplayer) == stats.iat[co + 1, 0]:
        co += 1
    co += 1
list.sort()
for i in list:
    age.append(i[0])
    pts.append(int(i[1]))
plt.scatter(age, pts)
plt.xlabel('Age')
plt.ylabel('Pts Scored')
plt.yticks(np.arange(min(pts), max(pts) + 1, 500))

plt.show()

# add players to 2d team list
teamlist = copy.deepcopy(Teams)
for i in range(1, len(stats)):
    current_player = stats.iat[i, stats.columns.get_loc('Player')]
    current_team = stats.iat[i, stats.columns.get_loc("Tm")]
    for x in range(0, len(teamlist)):
        if teamlist[x][0] == current_team:
            teamlist[x].append(current_player)
bestteams = []
for x in range(0, len(teamlist)):
    bestteams.insert(x, teamlist[x])
for i in range(0, len(bestteams)):
    bestteams[i].insert(0, 0)
for i in All:
    for t in bestteams:
        if i[1] in t:
            t[0] += float(i[0])
bestteams.sort(reverse=True)
for x in bestteams:
    for t in Teams:
        if x[1] in t:
            x[1] = t[1]

for i in range(0, len(bestteams)):
    print("rating: %d, team: %s" % (bestteams[i][0], bestteams[i][1]))


# search function


def searcher(searchq):
    # find player and pull up their row
    popup = Toplevel()

    pos = []
    teams = []
    searchq = unidecode.unidecode(searchq)
    # in case someone searches for god of the court
    if searchq.lower() == 'gary thai':
        Label(popup, text="Gary Thai \n Supreme God of the Court \n Age: Immortal \n"
                          "Played with: Montgomery College Raptors\n"
                          "No need to view stats. 100%. 10/10. \n"
                          "Quality man. Triple doubles all day \n").pack()
        img = PhotoImage(file='headshots/thai.png')
        img = img.subsample(3, 3)
        pic = Label(popup, image=img).pack()

    # checks if search query is in list of players

    elif searchq.casefold() in unidecode.unidecode(str(stats.Player.values).casefold()):
        count = 0
        current = 0
        for row2 in stats.iterrows():

            # completes name if only partial name is typed,
            # goes to first instance of found substring, so 'a' will pull up first player
            # with an a in their name
            if searchq.casefold() in unidecode.unidecode(
                    str(stats.iat[count, stats.columns.get_loc("Player")]).casefold()):
                searchq = str(stats.iat[count, stats.columns.get_loc("Player")])

            # checks every row and retrieves rows for specified player
            currplayer = unidecode.unidecode(str(stats.iat[count, stats.columns.get_loc("Player")]).casefold())
            if currplayer.casefold() == unidecode.unidecode(searchq.casefold()):
                pos.append(count)

                # assigns age
                age = stats.iat[count, stats.columns.get_loc("Age")]
                # translate position abbreviation to full name from positions list
                # ex: turns "C" into "Center"
                position = stats.iat[count, stats.columns.get_loc("Pos")]
                for item in positions:
                    if position in item:
                        position = item[1]
                current = count
            count += 1

        # creates list of teams played on
        for x in pos:
            t = stats.iat[x, stats.columns.get_loc("Tm")]

            # translates team abbreviation to full name
            for item in teamlist:
                if t in item:
                    teams.append(item[1])
        teamstring = "\n"
        teamstring = teamstring.join(teams)

        # prints name age teams and position
        currentplayer = stats.iat[current, stats.columns.get_loc("Player")]
        s = "%s\n\
    %s\n\
    Age: %s\n\
    Played with:\n%s" % (
            currentplayer, position, age, teamstring)
        Label(popup, text=s).pack()

        # searching for saved headshot
        firstandlast = currentplayer.split()

        first = firstandlast[0]
        newfirst = ''
        # strips dots from first name
        if '.' in first:
            for char in first:
                if char.isalpha():
                    newfirst += char
                    first = newfirst
        last = firstandlast[1]

        # pulls up image or if not found pulls up "nophoto.png"
        try:
            img = PhotoImage(file="headshots/%s-%s.jpg" % (unidecode.unidecode(first), unidecode.unidecode(last)))
        except TclError:
            img = PhotoImage(file='headshots/nophoto.png')
            img = img.subsample(2, 2)
        except AttributeError:
            img = PhotoImage(file='headshots/nophoto.png')
            img = img.subsample(2, 2)
        label = Label(popup, image=img)
        label.pack()

        # drop down menu to view player stats
        variable = StringVar(popup)
        variable.set("Choose Data to View")  # default value
        w = OptionMenu(popup, variable, *headers[4:])
        w.pack()

        # choose data to view
        def ok():
            stat = variable.get()
            sums = []
            avg = 0
            total = 0
            displaystring = ''
            m = 0
            # cycle through rows and add up stats
            skipped = False
            for xx in pos:
                # skips totals column in data table if there are multiple entried
                if len(pos) > 1 and not skipped:
                    skipped = True
                    continue
                things = stats.iat[xx, stats.columns.get_loc(stat)]
                sums.append(things)

            # displays selected stat for all teams played on, including total and average
            for item in sums:
                if item == ' ' or item == '':
                    item = 0
                total += float(item)
            avg = total / len(sums)
            thingstring = ", "
            thingstring = thingstring.join(sums)
            display_stats = Toplevel()
            Label(display_stats, text=currentplayer).pack()
            Label(display_stats, text=stat).pack()
            while m < len(teams) and m < len(sums):
                displaystring += 'Team: %s, %s: %s \n' % (teams[m], stat, sums[m])
                m += 1
            Label(display_stats, text=displaystring).pack()
            Label(display_stats, text="Average: %.2f" % avg).pack()
            Label(display_stats, text="Total: %.2f" % total).pack()
            display_stats.title('Stats')

            display_stats.mainloop()

        button = Button(popup, text="OK", command=ok)
        button.pack()


    else:
        s = "Player not Found. You need to enter their entire name, spelled correctly."
        display = Label(popup, text=s)
        display.pack()
    popup.title('Stats')
    popup.mainloop()


# main GUI
main = Tk()
main.geometry("500x500")
search = Label(main, text='Enter Player Name')
search.grid(row=0, column=1)
e = Entry(main)
e.grid(row=1, column=1)
search_button = Button(main, text="Search", command=lambda: searcher(e.get()))

search_button.grid(row=2, column=1)
# drop down menu
var2 = StringVar(main)
var2.set("Choose Player")  # default value
w3 = OptionMenu(main, var2, *players)
w3.grid(row=3, column=1)
button = Button(main, text="Look at Player", command=lambda: searcher(var2.get()))
button.grid(row=4, column=1)


# pick out top 10 from any passed stat
def view_top10():
    top_players = []
    x = 0

    # create list of players
    while x < len(players):
        top_players.append([])
        x += 1
    for d in range(0, len(players)):
        top_players[d].append(players[d])
    current_stat = var3.get()
    top10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = -1
    p = 0

    # attaches relevant stat value to each player
    while p < len(players) and i + 1 < len(stats):
        i += 1
        cell = stats.iat[i, stats.columns.get_loc(current_stat)]
        check = stats.iat[i, stats.columns.get_loc('Player')]
        if cell == '' or cell == ' ':
            cell = 0
        elif cell is None:
            continue
        cell = float(cell)
        top_players[p].insert(0, cell)

        # skips duplicates rows
        while i + 1 < len(stats) and stats.iat[i, stats.columns.get_loc('Player')] == \
                stats.iat[i + 1, stats.columns.get_loc('Player')]:
            i += 1
        p += 1

        # sort in descending order by stat
    top_players.sort(reverse=True)

    # add first 10 to list to display
    for yy in range(0, 10):
        top10[yy] = top_players[yy]

        # top 10 popup GUI
    popup = Toplevel()
    Label(popup, text='10 Players with Highest "%s"' % current_stat).pack()
    listbox = Listbox(popup, width=25, selectmode=SINGLE)

    for item in top10:
        listbox.insert(END, "%g - %s" % (item[0], item[1]))
    listbox.pack()

    # allows you to select players from statbox to view
    def onselect(event):
        ww = event.widget
        idx = int(ww.curselection()[0])
        value = ww.get(idx)
        value = value.split(" - ")
        searcher(value[1])

    listbox.bind('<<ListboxSelect>>', onselect)
    popup.mainloop()


# displays listbox with team roster
def view_teams(passedteam):
    try:
        team = var4.get()
    except:
        team = passedteam
    count = 0
    curr = 0

    for r in Teams:
        if r[1] in team:
            curr = count
            break
        count += 1

    popup = Toplevel()
    Label(popup, text=r[1]).pack()

    listbox = Listbox(popup, width=25, selectmode=SINGLE)
    for y in range(2, len(teamlist[curr])):
        listbox.insert(END, teamlist[curr][y])
    listbox.pack()

    # allows you to select players from teambox to view
    def onselect(event):
        ww = event.widget
        idx = int(ww.curselection()[0])
        value = ww.get(idx)
        searcher(value)

    listbox.bind('<<ListboxSelect>>', onselect)
    popup.mainloop()


# view top 10 drop down
var3 = StringVar(main)
var3.set("Choose Stat to View Top 10")  # default value
w = OptionMenu(main, var3, *headers[4:])
w.config(width=25)
w.grid(row=0, column=0)
l2 = Button(main, text="View Top 10", command=view_top10)
l2.grid(row=1, column=0)

# view team drop down
var4 = StringVar(main)
var4.set("Choose Team to View")  # default value
w2 = OptionMenu(main, var4, *fullteam)
w2.grid(row=0, column=2)
l3 = Button(main, text="View Team", command=lambda: view_teams(var4))
l3.grid(row=1, column=2)

main.title('2018-2019 Season NBA Player Stats')
main.mainloop()
