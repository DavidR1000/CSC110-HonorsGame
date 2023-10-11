import TileMap

class player:

    moveSpeed = 1.2
    maxSpeed = 4
    maxFallingSpeed = 12
    stopSpeed = 0.3
    jumpStart = -12.0
    gravity = 0.64
    stopJumpSpeed = 1

    right = False
    left = False
    

    falling = False
    jumping = False

    x = 64
    y = 64

    width = 20
    height = 20

    changeX = 0
    changeY = 0

    tempx = 196
    tempy = 196

    tox = 0
    toy = 0

    topLeft = False
    topRight = False
    bottomLeft = False
    bottomRight = False

    xTile = 0
    yTile = 0

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

        self.tox = self.x + self.changeX
        self.toy = self.y + self.changeY

        self.tempx = self.x
        self.tempy = self.y

        self.calculateCorners(self.x, self.toy)
        if self.changeY < 0:
            if self.topLeft or self.topRight:
                self.changeY = 0
                self.tempy = currRow * self.tileMap.tileSize + 20
            else: 
                self.tempy += self.changeY
            
        
        if self.changeY > 0: 
            if self.bottomLeft or self.bottomRight:
                self.changeY = 0
                self.falling = False
                self.fastFall = False
                self.tempy = (currRow + 1) * self.tileMap.tileSize - 20
            else:
                self.tempy += self.changeY
    

        self.calculateCorners(self.tox, self.y)
        if self.changeX < 0:
            if self.topLeft or self.bottomLeft:
                self.changeX = 0
                self.tempx = currCol * self.tileMap.tileSize + 20
            else:
                self.tempx += self.changeX
        
        if self.changeX > 0: 
            if self.topRight or self.bottomRight: 
                self.x = 0
                self.tempx = (currCol + 1) * self.tileMap.tileSize - 20
            
            else: 
                self.tempx += self.changeX
            
        
        if(not self.falling): 
            hold = self.y + 1
            self.calculateCorners(self.x, hold)
            if(not self.bottomLeft and not self.bottomRight): 
                self.falling = True
            
    def getNextPosition(self):
        if self.right:
            self.changeX += self.moveSpeed
            if self.changeX > self.maxSpeed:
                self.changeX = self.maxSpeed
        elif self.left:
            self.changeX -= self.moveSpeed
            if self.changeX < -self.maxSpeed:
                self.changeX = -self.maxSpeed
        else:
            if self.changeX > 0:
                self.changeX -= self.stopSpeed
                if self.changeX < 0:
                    self.changeX = 0
            elif self.changeX < 0:
                self.changeX += self.stopSpeed
                if self.changeX > 0:
                    self.changeX = 0
        
        if self.jumping and not self.falling:
            self.changeY = self.jumpStart
            self.falling = True
        
        if self.falling:
            self.changeY += self.gravity

            if(self.changeY > 0):
                self.jumping = False
            
            if self.changeY < 0 and not self.jumping:
                self.changeY += self.stopJumpSpeed

            if self.changeY > self.maxFallingSpeed:
                self.changeY = self.maxFallingSpeed

        else:
            self.changeY = 0
        
        self.x = self.tempx
        self.y = self.tempy

        self.tileMap.setx((320 - self.x) - 200)
        self.tileMap.sety((320 - self.y))
    
    def setPosition(self):
        self.x = self.tempx
        self.y = self.tempy
    
    def update(self):
        self.getNextPosition()
        self.checkTileMapCollision()
        self.setPosition()
        
        self.xTile = self.x/self.tileMap.tileSize // 1
        self.yTile = self.y/self.tileMap.tileSize // 1


