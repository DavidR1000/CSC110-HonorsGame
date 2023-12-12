'''
This class is called from the main game class
to create interactable platforms the character
can jump on
'''

class platform:

    def __init__(self, tm, row, col, player):
        '''
        Recieves the position of the platfrom in the map
        and recieves the player to be able to check to 
        see if the player is above the platform
        '''
        self.tm = tm
        self.row = row
        self.col = col
        self.player = player
        self.solid = False

    def update(self):
        '''
        This function checks the height of the player and 
        if the player is above the platform then the platform
        becomes solid if the player is above the platform.
        '''
        yHold = self.player.y
        # Checks if the platform is currently solid
        if self.solid:
            # Keeps platform solid if player is above the platform
            # Otherwise the platform is not solid
            if self.row*self.tm.tileSize >= yHold:
                self.tm.map[self.row][self.col] = 4
                self.sold = True
            else:
                self.tm.map[self.row][self.col] = 3
                self.solid = False
        else:
            # Checks that the player is fully above the platform
            # before making it solid
            if self.row*self.tm.tileSize - 20 >= yHold:
                self.tm.map[self.row][self.col] = 4
                self.solid = True
            else:
                self.tm.map[self.row][self.col] = 3
                self.solid = False