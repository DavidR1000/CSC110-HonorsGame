'''
This class is called in the main game class
and has all the properties of the player
and controls movement of the character
'''

class player:
    # Basic movement properties used to create
    # movement and gravity
    moveSpeed = 1.2
    maxSpeed = 5.2
    maxFallingSpeed = 12
    stopSpeed = 0.6
    jumpStart = -12.0
    gravity = 0.64
    stopJumpSpeed = 1

    right = False
    left = False

    falling = False
    fastFall = False
    jumping = False

    width = 16
    height = 16

    dx = 0
    dy = 0  

    tempx = 100
    tempy = 100

    def __init__(self, TileMap, startx, starty, width, height):
        '''
        This function gives the player class information of the
        actual game map and the screen properties
        '''
        self.tileMap = TileMap
        
        self.x = startx + self.tileMap.tileSize/4
        self.y = starty + self.tileMap.tileSize/4

        self.tempx = startx + self.tileMap.tileSize/4
        self.tempy = starty + self.tileMap.tileSize/4

        self.gameWidth = width
        self.gameHeight = height

        self.xTiles = len(TileMap.map[0])
        self.yTiles = len(TileMap.map)


    def calculateCorners(self, x, y):
        '''
        This function checks the 4 tiles on the screen around the player to check if they are solid blocks
        '''
        leftTile = self.tileMap.getColTile((x) // 1)
        rightTile = self.tileMap.getColTile(((x + self.width) // 1) - 1)
        topTile = self.tileMap.getRowTile((y) // 1)
        bottomTile = self.tileMap.getRowTile(((y + self.height) // 1) - 1)

        self.topLeft = self.tileMap.getTile(topTile, leftTile) == 0 or self.tileMap.getTile(topTile, leftTile) == 4
        self.topRight = self.tileMap.getTile(topTile, rightTile) == 0 or self.tileMap.getTile(topTile, rightTile) == 4
        self.bottomLeft = self.tileMap.getTile(bottomTile, leftTile) == 0 or self.tileMap.getTile(bottomTile, leftTile) == 4
        self.bottomRight = self.tileMap.getTile(bottomTile, rightTile) == 0 or self.tileMap.getTile(bottomTile, rightTile) == 4




    def checkTileMapCollision(self):
        '''
        This function checks collisions for player to ensure it is moving to an open tile
        '''
        currCol = self.tileMap.getColTile(self.x // 1)
        currRow = self.tileMap.getRowTile(self.y // 1)

        self.tox = self.x + self.dx
        self.toy = self.y + self.dy

        self.tempx = self.x
        self.tempy = self.y

        self.calculateCorners(self.x, self.toy)
        if self.dy < 0:
            if self.topLeft or self.topRight:
                self.dy = 0
                self.tempy = currRow * self.tileMap.tileSize
            else: 
                self.tempy += self.dy
            
        
        if self.dy > 0: 
            if self.bottomLeft or self.bottomRight:
                self.dy = 0
                self.falling = False
                self.fastFall = False
                self.tempy = (currRow + 1) * self.tileMap.tileSize - self.height
            else:
                self.tempy += self.dy
    

        self.calculateCorners(self.tox, self.y)
        if self.dx < 0:
            if self.topLeft or self.bottomLeft:
                self.dx = 0
                self.tempx = currCol * self.tileMap.tileSize
            else:
                self.tempx += self.dx
        
        if self.dx > 0: 
            if self.topRight or self.bottomRight: 
                self.x = 0
                self.tempx = (currCol + 1) * self.tileMap.tileSize - self.width
            
            else: 
                self.tempx += self.dx

        if not self.falling:
            hold = self.y + 1
            self.calculateCorners(self.x, hold)
            if not self.bottomLeft and not self.bottomRight:
                self.falling = True


    def setPosition(self):
        '''
        This function sets the players next location based on the results of
        collision detection function
        '''
        self.x = self.tempx
        self.y = self.tempy


    def getNextPosition(self):
        '''
        This gets the next accepteable position for the player
        based on the user's input and depending on the results of the
        collision detection
        '''
        if self.right:
            self.dx += self.moveSpeed
            if self.dx > self.maxSpeed:
                self.dx = self.maxSpeed
        elif self.left:
            self.dx -= self.moveSpeed
            if self.dx < -self.maxSpeed:
                self.dx = -self.maxSpeed
        else:
            if self.dx > 0:
                self.dx -= self.stopSpeed
                if self.dx < 0:
                    self.dx = 0
            elif self.dx < 0:
                self.dx += self.stopSpeed
                if self.dx > 0:
                    self.dx = 0
        
        

        if self.jumping and not self.falling:
            self.dy = self.jumpStart
            self.falling = True

        if self.falling:
            self.dy += self.gravity

            if self.dy > 0:
                    self.jumping = False

            if self.dy < 0 and not self.jumping:
                self.dy += self.stopJumpSpeed
                       
            if self.dy > self.maxFallingSpeed:
                self.dy = self.maxFallingSpeed

            if self.fastFall:
                self.dy = self.maxFallingSpeed
                self.fastFall = False

        else:
            self.dy = 0
        
        self.x = self.tempx
        self.y = self.tempy

        if self.yTiles > self.gameHeight // self.tileMap.tileSize:    
            if self.y < (7 * self.tileMap.tileSize):
                self.tileMap.sety(0)
            elif self.y // self.tileMap.tileSize > self.yTiles - 5:
                self.tileMap.sety(round(self.gameHeight/2 + 100 - ((self.yTiles - 4) * self.tileMap.tileSize)))
            else:
                self.tileMap.sety(round(self.gameHeight/2 - self.y + 100))
        else:
            self.tileMap.sety(0)


        if self.xTiles > self.gameWidth // self.tileMap.tileSize:    
            if self.x < (8 * self.tileMap.tileSize):
                self.tileMap.setx(0)
            elif self.x // self.tileMap.tileSize > self.xTiles - 9:
                self.tileMap.setx(round(self.gameWidth/2 - ((self.xTiles - 8) * self.tileMap.tileSize)))
            else:
                self.tileMap.setx(round(self.gameWidth/2 - self.x))
        else:
            self.tileMap.setx(0)


    def update(self):
        '''
        This function updates charcters location by checking the see the next position for 
        the character based on user input and then ensures the desired location is open and then moves
        the player to the next acceptable location
        '''
        self.getNextPosition()
        self.checkTileMapCollision()
        self.setPosition()