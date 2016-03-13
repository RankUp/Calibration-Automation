import csv
from Player import Player
from scipy import stats

positions = ["QB", "WR"]

#Read data from csv
dataFile = open("c:\users\jk12559\desktop\sampleData.csv")
dataDict = csv.DictReader(dataFile)
#assign data to player class
players = [Player(row) for row in dataDict]

playersGroup = {}
for pos in positions:
    posList = [player for player in players if player.position == pos]
    playersGroup[pos] = posList

for group in playersGroup.itervalues():
    group.sort(key = lambda x: x.points, reverse = True)
    for player in group:
        player.rank = group.index(player) + 1

#do linear regression with points as dependent and rank as independent variables
for pos, players in playersGroup.iteritems():
    x = map(lambda player: player.rank,players)
    y = map(lambda player: player.points,players)
    result = stats.linregress(x,y)
    print (pos, result)
#return smoothed values for each player rank