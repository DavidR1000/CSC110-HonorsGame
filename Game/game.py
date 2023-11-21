import sys, pygame, player, platform, TileMap, teleport, button
pygame.init()

width = 1024
height = 700

screen = width, height
black = 0, 0, 0

blockSize = 64

platforms = []

countTeleport = 5

portalExist = False

gameover = False

state = 0
clickLoc = (0, 0)

screen = pygame.display.set_mode(screen)

tm = TileMap.TileMap("HonorsGame\Game\world.txt", blockSize)

pygame.display.set_caption("Cubeformer")

font = pygame.font.Font('freesansbold.ttf', 80)

titleText = font.render('Cubeformer', True, (0, 255, 0))
titleRect = titleText.get_rect()
titleRect.center = (width/2, height/4)

cText = font.render('Controls', True, (0, 255, 0))
cRect = cText.get_rect()
cRect.center = (width/2, height/4)

font = pygame.font.Font('freesansbold.ttf', 120)

winText = font.render('You Won!', True, (0, 255, 0))
winRect = winText.get_rect()
winRect.center = (width/2, height/3)

win2Text = font.render('Great Job!', True, (0, 255, 0))
win2Rect = win2Text.get_rect()
win2Rect.center = (width/2, height/2)

font = pygame.font.Font('freesansbold.ttf', 32)

play = button.button(width/2, height*5/12, width/4, height/8, (0, 150, 220), (0, 255, 0))
controls = button.button(width/2, height*7/12, width/4, height/8, (0, 150, 220), (0, 255, 0))
exit = button.button(width/2, height*9/12, width/4, height/8, (0, 150, 220), (255, 0, 0))
back = button.button(width/ 6, height*9/11, width/10, height/16, (0, 150, 220), (0, 255, 0))

playText = font.render('Play', True, (255, 0, 0))
playRect = playText.get_rect()
playRect.center = (play.x, play.y)

controlsText = font.render('Controls', True, (255, 0, 0))
controlsRect = controlsText.get_rect()
controlsRect.center = (controls.x, controls.y)

exitText = font.render('Exit', True, (0, 255, 0))
exitRect = exitText.get_rect()
exitRect.center = (exit.x, exit.y)

backText = font.render('Back', True, (255, 0, 0))
backRect = backText.get_rect()
backRect.center = (back.x, back.y)

c2Text = font.render('Use A and D to move', True, (0, 150, 220))
c2Rect = c2Text.get_rect()
c2Rect.center = (width/4, height*2/5)

c3Text = font.render('Use W to jump', True, (0, 150, 220))
c3Rect = c3Text.get_rect()
c3Rect.center = (width*3/4, height*2/5)

c4Text = font.render('This will teleport you', True, (0, 150, 220))
c4Rect = c4Text.get_rect()
c4Rect.center = (width*3/4, back.y)

file = open("controlsMap.txt", 'w')
cols = width//blockSize
rows = height//blockSize
words = ''
for i in range(rows):
    for j in range(cols):
        words += '1 '
    words += '\n'
file.write(words)
file.close()

controlsTM = TileMap.TileMap("controlsMap.txt", blockSize)
for i in range(len(controlsTM.map[7])):
    controlsTM.map[7][i] = 0
controlsTM.map[6][0] = 4
controlsTM.map[5][0] = 4
controlsTM.map[6][len(controlsTM.map[7])-1] = 4
controlsTM.map[5][len(controlsTM.map[7])-1] = 4
playerMove = player.player(controlsTM, 2*blockSize, 6*blockSize, width, height)

for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 2:
                player = player.player(tm, i*blockSize, j*blockSize, width, height)

for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 3:
                platforms.append(platform.platform(tm, j, i, player))
                tm.map[j][i] = 1
            if int(tm.map[j][i]) == 5:
                portal = teleport.teleport(i, j, player, tm)
                portalExist = True
            if int(tm.map[j][i]) == 7:
                gameEndX = i * tm.tileSize
                gameEndY = j * tm.tileSize

if portalExist:            
    for i in range(len(tm.map[0])):
            for j in range(len(tm.map)):            
                if int(tm.map[j][i]) == 6:
                    portal.endX = i * tm.tileSize
                    portal.endY = j * tm.tileSize


while True:
    pygame.time.delay(15)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if state == 1:
        
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_w:
                    playerMove.jumping = True
                if event.key == pygame.K_a:
                    playerMove.left = True
                if event.key == pygame.K_s:
                    playerMove.fastFall = True
                if event.key == pygame.K_d:
                    playerMove.right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                        playerMove.left = False
                if event.key == pygame.K_d:
                        playerMove.right = False
            
        if state == -1:
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    player.jumping = True
                if event.key == pygame.K_a:
                    player.left = True
                if event.key == pygame.K_s:
                    player.fastFall = True
                if event.key == pygame.K_d:
                    player.right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                        player.left = False
                if event.key == pygame.K_d:
                        player.right = False

    mouse = pygame.mouse.get_pos()
    
    mouseClicks = pygame.mouse.get_pressed(num_buttons = 3)
    
    for press in mouseClicks:
         if press:
            clickLoc = pygame.mouse.get_pos()

    if state == 0:
        if mouse[0] > play.rightX and mouse[0] < play.rightX + play.width and mouse[1] > play.topY and mouse[1] < play.topY + play.height:
            play.state = 1
        else:
            play.state = 0
        if mouse[0] > controls.rightX and mouse[0] < controls.rightX + controls.width and mouse[1] > controls.topY and mouse[1] < controls.topY + controls.height:
            controls.state = 1
        else:
            controls.state = 0
        if mouse[0] > exit.rightX and mouse[0] < exit.rightX + exit.width and mouse[1] > exit.topY and mouse[1] < exit.topY + exit.height:
            exit.state = 1
        else:
            exit.state = 0

        if clickLoc[0] > play.rightX and clickLoc[0] < play.rightX + play.width and clickLoc[1] > play.topY and clickLoc[1] < play.topY + play.height:
            state = -1
        elif clickLoc[0] > controls.rightX and clickLoc[0] < controls.rightX + controls.width and clickLoc[1] > controls.topY and clickLoc[1] < controls.topY + controls.height:
            state = 1
        elif clickLoc[0] > exit.rightX and clickLoc[0] < exit.rightX + exit.width and clickLoc[1] > exit.topY and clickLoc[1] < exit.topY + exit.height:
            pygame.quit()
            sys.exit()

        play.update()
        controls.update()
        exit.update()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, 64))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 64, height))
        pygame.draw.rect(screen, (0, 0, 0), (0,height - 64, width, 64))
        pygame.draw.rect(screen, (0, 0, 0), (width - 64, 0, 64, height))
        pygame.draw.rect(screen, (210, 180, 140), (64, 64, width - 128, height - 128))

        screen.blit(titleText, titleRect)

        pygame.draw.rect(screen, play.currentColor, (play.rightX, play.topY, play.width, play.height))
        screen.blit(playText, playRect)
        pygame.draw.rect(screen, controls.currentColor, (controls.rightX, controls.topY, controls.width, controls.height))
        screen.blit(controlsText, controlsRect)
        pygame.draw.rect(screen, exit.currentColor, (exit.rightX, exit.topY, exit.width, exit.height))
        screen.blit(exitText, exitRect)

    elif state == 1:
        if mouse[0] > back.rightX and mouse[0] < back.rightX + back.width and mouse[1] > back.topY and mouse[1] < back.topY + back.height:
            back.state = 1
        else:
            back.state = 0

        if clickLoc[0] > back.rightX and clickLoc[0] < back.rightX + back.width and clickLoc[1] > back.topY and clickLoc[1] < back.topY + back.height:
            state = 0
        
        back.update()
        playerMove.update()

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, 64))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 64, height))
        pygame.draw.rect(screen, (0, 0, 0), (0,height - 64, width, 64))
        pygame.draw.rect(screen, (0, 0, 0), (width - 64, 0, 64, height))
        pygame.draw.rect(screen, (210, 180, 140), (64, 64, width - 128, height - 128))

        for i in range(len(controlsTM.map[0])):
            for j in range(len(controlsTM.map)):
                if int(controlsTM.map[j][i]) == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (blockSize * i, blockSize * j, blockSize, blockSize))
        pygame.draw.rect(screen, (255, 0, 0), (playerMove.x, playerMove.y, playerMove.width, playerMove.height))

        pygame.draw.rect(screen, (250, 0, 250), (width*3/4 - 250, back.y - blockSize/2, blockSize, blockSize))
        pygame.draw.rect(screen, (255, 255, 255), (width*3/4 - 250 + (blockSize/8), back.y - blockSize/2 + (blockSize/8), blockSize*3/4, blockSize*3/4))
        pygame.draw.rect(screen, (250, 0, 250), (width*3/4 - 250 + (blockSize/4), back.y - blockSize/2 + (blockSize/4), blockSize/2, blockSize/2))
        pygame.draw.rect(screen, (255, 255, 255), (width*3/4 - 250 + (blockSize*3/8), back.y - blockSize/2 + (blockSize*3/8), blockSize/4, blockSize/4))

        pygame.draw.rect(screen, (92, 64, 51), (width*3/4 - 250, back.y - blockSize/2, blockSize, blockSize))
        pygame.draw.rect(screen, (255, 255, 255), (width*3/4 - 250 + (blockSize*3/16), back.y - blockSize/2 + (blockSize/4), blockSize*5/8, blockSize*3/4))

        screen.blit(cText, cRect)
        screen.blit(c2Text, c2Rect)
        screen.blit(c3Text, c3Rect)
        screen.blit(c4Text, c4Rect)

        pygame.draw.rect(screen, back.currentColor, (back.rightX, back.topY, back.width, back.height))
        screen.blit(backText, backRect)

    elif state == 2:

        if mouse[0] > exit.rightX and mouse[0] < exit.rightX + exit.width and mouse[1] > exit.topY and mouse[1] < exit.topY + exit.height:
            exit.state = 1
        else:
            exit.state = 0

        if clickLoc[0] > exit.rightX and clickLoc[0] < exit.rightX + exit.width and clickLoc[1] > exit.topY and clickLoc[1] < exit.topY + exit.height:
            pygame.quit()
            sys.exit()
        
        exit.update()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, 64))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 64, height))
        pygame.draw.rect(screen, (0, 0, 0), (0,height - 64, width, 64))
        pygame.draw.rect(screen, (0, 0, 0), (width - 64, 0, 64, height))
        pygame.draw.rect(screen, (210, 180, 140), (64, 64, width - 128, height - 128))

        screen.blit(winText, winRect)
        screen.blit(win2Text, win2Rect)

        pygame.draw.rect(screen, exit.currentColor, (exit.rightX, exit.topY, exit.width, exit.height))
        screen.blit(exitText, exitRect)

    else:
        player.update()
        for i in range(len(platforms)):
            platforms[i].update()
        portal.update()
        screen.fill(black)
        for i in range(len(tm.map[0])):
            for j in range(len(tm.map)):
                if int(tm.map[j][i]) == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                if int(tm.map[j][i]) == 1:
                    pygame.draw.rect(screen, (210, 180, 140), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                if int(tm.map[j][i]) == 2:
                    pygame.draw.rect(screen, (92, 64, 51), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                    pygame.draw.rect(screen, (0), (blockSize * i + tm.x + (tm.tileSize*3/16), blockSize * j + tm.y+ (tm.tileSize/4), blockSize*5/8, blockSize*3/4))
                if int(tm.map[j][i]) == 5:
                    pygame.draw.rect(screen, (92, 64, 51), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                    pygame.draw.rect(screen, (255, 255, 255), (blockSize * i + tm.x + (tm.tileSize*3/16), blockSize * j + tm.y+ (tm.tileSize/4), blockSize*5/8, blockSize*3/4))
                if int(tm.map[j][i]) == 6:
                    pygame.draw.rect(screen, (92, 64, 51), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                    pygame.draw.rect(screen, (0), (blockSize * i + tm.x + (tm.tileSize*3/16), blockSize * j + tm.y+ (tm.tileSize/4), blockSize*5/8, blockSize*3/4))
                if int(tm.map[j][i]) == 3 or int(tm.map[j][i]) == 4:
                    pygame.draw.rect(screen, (0, 0, 250), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize/4))
                    pygame.draw.rect(screen, (210, 180, 140), (blockSize * i + tm.x, blockSize * j + tm.y + blockSize/4, blockSize, blockSize*3/4))
                if int(tm.map[j][i]) == 7:
                    pygame.draw.rect(screen, (92, 64, 51), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                    pygame.draw.rect(screen, (255, 255, 255), (blockSize * i + tm.x + (tm.tileSize*3/16), blockSize * j + tm.y+ (tm.tileSize/4), blockSize*5/8, blockSize*3/4))
        pygame.draw.rect(screen, (255, 0, 0), (player.x + tm.x, player.y + tm.y, player.width, player.height))
        if player.x >= gameEndX and player.x + player.width <= gameEndX + tm.tileSize + 1:
            if player.y >= gameEndY and player.y + player.height <= gameEndY + tm.tileSize:
                state = 2

    pygame.display.update()

        