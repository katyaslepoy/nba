import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# make graphs of everything
files=[]
for y in range(10, 20):
    files.append('C:/Users/katya/PycharmProjects/teammamba/venv/stats20%s.csv' % y)

stats = pd.concat(map(pd.read_csv, files))

lebron = []

steph = []
harden = []
durant = []
rose = []
westbrook = []
list=(lebron,steph,harden,durant,rose,westbrook)

for f in files:
    stats = pd.read_csv(f)
    rc = 0
    for row in stats.iterrows():
        if rc<len(stats):
            if stats.iat[rc, stats.columns.get_loc('Player')] == 'LeBron James':
                lebron.append(stats.iat[rc, stats.columns.get_loc('PTS')]/stats.iat[rc,stats.columns.get_loc('G')])
            elif stats.iat[rc, stats.columns.get_loc('Player')] == 'Stephen Curry':
                steph.append(stats.iat[rc, stats.columns.get_loc('PTS')]/stats.iat[rc,stats.columns.get_loc('G')])
            elif stats.iat[rc, stats.columns.get_loc('Player')] == 'James Harden':
                harden.append(stats.iat[rc, stats.columns.get_loc('PTS')]/stats.iat[rc,stats.columns.get_loc('G')])
            elif stats.iat[rc, stats.columns.get_loc('Player')] == 'Kevin Durant':
                durant.append(stats.iat[rc, stats.columns.get_loc('PTS')]/stats.iat[rc,stats.columns.get_loc('G')])
            elif stats.iat[rc, stats.columns.get_loc('Player')] == 'Russell Westbrook':
                westbrook.append(stats.iat[rc, stats.columns.get_loc('PTS')]/stats.iat[rc,stats.columns.get_loc('G')])
            elif stats.iat[rc, stats.columns.get_loc('Player')] == 'Derrick Rose':
                rose.append(stats.iat[rc, stats.columns.get_loc('PTS')]/stats.iat[rc,stats.columns.get_loc('G')])
                if stats.iat[rc + 1, stats.columns.get_loc('Player')] == 'Derrick Rose':
                    rc += 1

        rc += 1

print(lebron)
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
df=pd.DataFrame(zip(x,lebron,steph,harden,westbrook,rose,durant), columns=["year","lebron","steph","harden","westbrook","rose","durant"])
print(df)
df.to_csv('10year.csv')
from pylab import *

df[
    df['Player'] == 'LeBron James'
].set_index('Year')['Life Ladder'].plot(
    kind='line',
    figsize=(12,8)
)
t = arange(2010, 2020, 1)

s = lebron
plt.plot(t, s)
plt.yticks(np.arange(15, 30, 5))
plt.xlabel('Year')
plt.ylabel('Pts')
plt.title('LeBron James')
plt.grid(True)
plt.show()
plt.savefig('lebronppg.png')

t = arange(2010, 2020, 1)
s = westbrook
plt.plot(t, s)
plt.yticks(np.arange(15, 45, 5))
plt.xlabel('Year')
plt.ylabel('Pts')
plt.title('Russell Westbrook')
plt.grid(True)
plt.show()
plt.savefig('westbrookppg.png')

x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
from pylab import *

t = arange(2010, 2020, 1)
s = rose
plt.plot(t, s)
plt.yticks(np.arange(15, 30, 5))
plt.xlabel('Year')
plt.ylabel('Pts')
plt.title('Derrick Rose')
plt.grid(True)
plt.show()
plt.savefig('roseppg.png')
print(harden)
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

from pylab import *

t = arange(2010, 2020, 1)
s = harden
plt.plot(t, s)
plt.yticks(np.arange(15, 45, 5))
plt.xlabel('Year')
plt.ylabel('Pts')
plt.title('James Harden')
plt.grid(True)
plt.show()
plt.savefig('hardenppg.png')

print(durant)
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
from pylab import *

t = arange(2010, 2020, 1)
s = durant
plt.plot(t, s)
plt.yticks(np.arange(15, 40, 5))
plt.xlabel('Year')
plt.ylabel('Pts')
plt.title('Kevin Durant')
plt.grid(True)
plt.show()
plt.savefig('durantppg.png')

t = arange(2010, 2020, 1)
s = steph
plt.plot(t, s)
plt.yticks(np.arange(15, 45, 5))
plt.xlabel('Year')
plt.ylabel('Pts')
plt.title('Stephen Curry')
plt.grid(True)
plt.show()
plt.savefig('headshots/stephppg.png')