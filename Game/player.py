

class player:
    
    right = False
    left = False
    up = False
    down = False

    moveSpeed = [0, 0]
    
    def update(self):
        if self.right:
            self.moveSpeed[0] = 1
        elif self.left:
            self.moveSpeed[0] = -1
        else:
            self.moveSpeed[0] = 0

        if self.down:
            self.moveSpeed[1] = 1
        elif self.up:
            self.moveSpeed[1] = -1
        else:
            self.moveSpeed[1] = 0

