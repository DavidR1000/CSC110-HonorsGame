

class platform:

    def __init__(self, tm, row, col, player):
        self.tm = tm
        self.row = row
        self.col = col
        self.player = player
        self.solid = False

    def update(self):
        yHold = self.player.y

        if self.solid:
            if self.row*self.tm.tileSize >= yHold:
                self.tm.map[self.row][self.col] = 4
                self.sold = True
            else:
                self.tm.map[self.row][self.col] = 3
                self.solid = False
        else:
            if self.row*self.tm.tileSize - 20 >= yHold:
                self.tm.map[self.row][self.col] = 4
                self.solid = True
            else:
                self.tm.map[self.row][self.col] = 3
                self.solid = False