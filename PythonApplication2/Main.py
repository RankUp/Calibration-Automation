import csv
from Player import Player

positions = ["QB", "WR"]

#Read data from csv
dataFile = open("c:\users\jk12559\desktop\sampleData.csv")
dataDict = csv.DictReader(dataFile)
#assign data to player class
players = [Player(row) for row in dataDict]
QB = [player for player in players if player.position == "QB"]
WR = [player for player in players if player.position == "WR"]
playersGroup = {"QB": QB, "WR": WR}

for group in playersGroup.itervalues():
    group.sort(key = lambda x: x.points, reverse = True)
    for player in group:
        player.rank = group.index(player) + 1


#do linear regression with points as dependent and rank as independent variables

#return smoothed values for each player rank