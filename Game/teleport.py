'''
This class handles the implementation of the player telporting when it reaches a
portal. It recieves the position of the entry portal and the player to see if 
player has entered the portal or not. Exit location of the portal is set in game class.
'''

class teleport:

    def __init__(self, startX, startY, player, tm):
        '''
        Recieves location of the entry portal and the player on the game map
        '''
        self.startX = startX * tm.tileSize
        self.startY = startY * tm.tileSize
        self.endX = 0
        self.endY = 0
        self.player = player
        self.tm = tm


    def update(self):
        '''
        Checks to see if the player's location is inside the bounds of the entry portal. If the 
        player is inside that location then player will be move to exit portal location.
        '''
        # Checks to see if player's x position is within the portal's x location
        if self.player.x >= self.startX and self.player.x + self.player.width <= self.startX + self.tm.tileSize + 1:
            # Checks to see if player's y position is within the portal's y location
            if self.player.y >= self.startY and self.player.y + self.player.height <= self.startY + self.tm.tileSize:
                self.player.tempx += self.endX - self.startX
                self.player.tempy += self.endY - self.startY