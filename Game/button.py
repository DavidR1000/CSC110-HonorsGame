



class button:
    
    state = 0

    def __init__(self, x, y, width, height, color, hoverColor):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hovorColor = hoverColor
        self.rightX = x - width/2
        self.topY = y - height/2
        self.currentColor = color

    def update(self):
        if self.state == 0:
            self.currentColor = self.color
        else:
            self.currentColor = self.hovorColor