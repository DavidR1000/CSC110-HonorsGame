

class teleport:

    def __init__(self, startX, startY, player, tm):
        self.startX = startX * tm.tileSize
        self.startY = startY * tm.tileSize
        self.endX = self.startX + 20
        self.endY = self.startY + 20
        self.player = player
        self.tm = tm


    def update(self):
        if self.player.x >= self.startX and self.player.x + self.player.width <= self.startX + self.tm.tileSize + 1:
            if self.player.y >= self.startY and self.player.y + self.player.height <= self.startY + self.tm.tileSize:
                self.player.tempx += self.endX - self.startX
                self.player.tempy += self.endY - self.startY