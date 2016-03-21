import csv
from Player import Player
from scipy import stats

#Read data from csv
dataFile = open("c:\users\jk12559\desktop\sampleData.csv")
dataDict = csv.DictReader(dataFile)

#assign data to player class
players = [Player(row) for row in dataDict]
dataFile.close()

#Extract list of positions from data
positions = set([player.position for player in players])

#Group players by position
playersGroup = {}
for pos in positions:
    posList = [player for player in players if player.position == pos if player.points != 0]
    playersGroup[pos] = posList

#Rank players
for group in playersGroup.itervalues():
    group.sort(key = lambda x: x.points, reverse = True)
    for player in group:
        player.rank = group.index(player) + 1

outputFile = open("c:\users\jk12559\desktop\outputData.csv", "w")
outputWriter = csv.DictWriter(outputFile,["Rank","Name","Position","Rank Up Points"])
outputWriter.writeheader()

#do linear regression with points as dependent and rank as independent variables
for pos, players in playersGroup.iteritems():
    x = [player.rank for player in players]
    y = [player.points for player in players]
    result = stats.linregress(x,y)
    
    #return smoothed values for each player rank
    for player in players:
        player.pointsRU = result.slope * player.rank + result.intercept
        outputWriter.writerow(player.outputDict())

outputFile.close()