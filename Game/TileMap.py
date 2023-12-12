
class TileMap:
    
    '''
    This class is called from the main game class to read the 
    file containing the information for the game map and creates
    a 2D array that contains the actual game map. Also contains an
    x and y constant to be able to create a screen shift.
    '''

    def __init__(self, holdName, tileSize):
        '''
        Recieves a string path to the file with the game map information
        and the size that each piece of the map will be.
        '''
        self.holdName = holdName
        self.tileSize = tileSize

        name = open(holdName)

        self.map = []
    
        rowCount = 0

        self.x = 50
        self.y = 50

        self.smoothScroll = 0.15
        '''
        Iterates over the the file making each line a list of string that goes
        into another list creating the 2D array that will be used as the game map.
        '''
        while True:
            line = name.readline().strip()
            if len(line) == 0:
                break
            self.map.append(line.split(" "))
            rowCount += 1



    def getColTile(self, x):
        '''
        Returns the corresponding column the x value is in the 2D array
        (x is in pixels)
        '''
        return x // self.tileSize
    
    def getRowTile(self, y):
        '''
        Returns the corresponding row the y value is in the 2D array
        (y is in pixels)
        '''
        return y // self.tileSize
    
    def getTile(self, row, col):
        '''
        Returns the value inside the 2D array at the specified
        row and column
        '''
        return int(self.map[round(row)][round(col)])
    
    def setx(self, i):
        '''
        Sets the current x value of the map
        (Used to make screen move)
        '''
        self.x += (i - self.x) * self.smoothScroll

    def sety(self, i):
        '''
        Sets the current y value of the map
        (Used to make screen move)
        '''
        self.y += (i - self.y) * self.smoothScroll