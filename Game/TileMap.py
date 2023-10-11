

class TileMap:
    
    def __init__(self, holdName, tileSize):
        self.holdName = holdName
        self.tileSize = tileSize

        name = open(holdName)
        line = name.readline()
        self.height = int(line)

        self.map = []
    
        rowCount = 0

        self.x = 50
        self.y = 50

        self.smoothScroll = 0.15

        while rowCount < self.height:
            line = name.readline().strip("\n")
            self.map.append(line.split(" "))
            rowCount += 1

    def getColTile(self, x):
        return x // self.tileSize
    
    def getRowTile(self, y):
        return y // self.tileSize
    
    def getTile(self, row, col):
        return int(self.map[round(row)][round(col)])
    
    def setx(self, i):
        self.x += (i - self.x) * self.smoothScroll

    def sety(self, i):
        self.y += (i - self.y) * self.smoothScroll

