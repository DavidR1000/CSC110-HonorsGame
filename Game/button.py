'''
This class is called from the main game class to
create interactable buttons that can be pressed
'''

class button:
    
    state = 0

    def __init__(self, x, y, width, height, color, hoverColor):
        '''
        Gets the postiion of the button and click and
        hover color
        '''
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
        # Checks if the cursor is hovering over the button and 
        # if it is then it will change the color to hover color
        if self.state == 0:
            self.currentColor = self.color
        else:
            self.currentColor = self.hovorColor