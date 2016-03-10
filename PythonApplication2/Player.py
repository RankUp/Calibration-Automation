class Player(object):
    """description of class"""
    def __init__(self, rowDict):
       self.name = rowDict["Name"]
       self.points = rowDict["Points"]
       self.position = rowDict["Position"]

