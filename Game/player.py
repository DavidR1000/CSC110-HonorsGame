

class player:
    
    moveSpeed = 1.2
    maxSpeed = 4.2
    maxFallingSpeed = 12
    stopSpeed = 0.3
    jumpStart = -12.0
    gravity = 0.64
    stopJumpSpeed = 1

    right = False
    left = False
    up = False
    down = False

    x = 100
    y = 100

    width = 20
    height = 20

    vel = 10

    xspeed = 0
    yspeed = 0

    dx = 0
    dy = 0  


    def __init__(self, TileMap):
        self.tileMap = TileMap


    def calculateCorners(self, x, y):
        leftTile = self.tileMap.getColTile(x // 1)
        rightTile = self.tileMap.getColTile(((x + 20) // 1) - 1)
        topTile = self.tileMap.getRowTile(y // 1)
        bottomTile = self.tileMap.getRowTile(((y + 20) // 1) - 1)

        self.topLeft = self.tileMap.getTile(topTile, leftTile) == 0
        self.topRight = self.tileMap.getTile(topTile, rightTile) == 0
        self.bottomLeft = self.tileMap.getTile(bottomTile, leftTile) == 0
        self.bottomRight = self.tileMap.getTile(bottomTile, rightTile) == 0




    def checkTileMapCollision(self):
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
                #self.falling = False
                #self.fastFall = False
                self.tempy = (currRow + 1) * self.tileMap.tileSize - 20
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
                self.tempx = (currCol + 1) * self.tileMap.tileSize - 20
            
            else: 
                self.tempx += self.dx


    def setPosition(self):
        self.x = self.tempx
        self.y = self.tempy


    def getNextPosition(self):
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
        
        if self.down:
            self.dy += self.moveSpeed
            if self.dy > self.maxSpeed:
                self.dy = self.maxSpeed
        elif self.up:
            self.dy -= self.moveSpeed
            if self.dy < -self.maxSpeed:
                self.dy = -self.maxSpeed
        else:
            if self.dy > 0:
                self.dy -= self.stopSpeed
                if self.dy < 0:
                    self.dy = 0
            elif self.dy < 0:
                self.dy += self.stopSpeed
                if self.dy > 0:
                    self.dy = 0



    def update(self):
        self.getNextPosition()
        self.checkTileMapCollision()
        self.setPosition()


