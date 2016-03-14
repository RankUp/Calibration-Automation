class Player(object):
    """description of class"""
    def __init__(self, rowDict):
       self.name = rowDict["Name"]
       self.points = float(rowDict["Points"])
       self.position = rowDict["Position"]

    def outputDict(self):
        output = {}
        output["Rank"] = self.rank
        output["Name"] = self.name
        output["Position"] = self.position
        output["Rank Up Points"] = self.pointsRU
        return output

