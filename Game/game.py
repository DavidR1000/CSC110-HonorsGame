import sys, pygame, player, platform, TileMap, teleport, button
pygame.init()

width = 1000
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

font = pygame.font.Font('freesansbold.ttf', 32)

play = button.button(width/2, height*5/12, width/4, height/8, (0, 150, 220), (0, 255, 0))
controls = button.button(width/2, height*7/12, width/4, height/8, (0, 150, 220), (0, 255, 0))
exit = button.button(width/2, height*9/12, width/4, height/8, (0, 150, 220), (255, 0, 0))

playText = font.render('Play', True, (255, 0, 0))
playRect = playText.get_rect()
playRect.center = (play.x, play.y)

controlsText = font.render('Controls', True, (255, 0, 0))
controlsRect = controlsText.get_rect()
controlsRect.center = (controls.x, controls.y)

exitText = font.render('Exit', True, (0, 255, 0))
exitRect = playText.get_rect()
exitRect.center = (exit.x, exit.y)

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

    if player.x >= gameEndX and player.x + player.width <= gameEndX + tm.tileSize + 1:
            if player.y >= gameEndY and player.y + player.height <= gameEndY + tm.tileSize:
                pygame.quit()
                sys.exit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

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
        print("controls")
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
                    pygame.draw.rect(screen, (100, 100, 100), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                if int(tm.map[j][i]) == 5:
                    pygame.draw.rect(screen, (250, 0, 250), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                    pygame.draw.rect(screen, (250, 250, 250), (blockSize * i + tm.x + (tm.tileSize/8), blockSize * j + tm.y + (tm.tileSize/8), blockSize*3/4, blockSize*3/4))
                    pygame.draw.rect(screen, (250, 0, 250), (blockSize * i + tm.x + (tm.tileSize/4), blockSize * j + tm.y + (tm.tileSize/4), blockSize/2, blockSize/2))
                    pygame.draw.rect(screen, (250, 250, 250), (blockSize * i + tm.x + (tm.tileSize*3/8), blockSize * j + tm.y + (tm.tileSize*3/8), blockSize/4, blockSize/4))
                if int(tm.map[j][i]) == 6:
                    pygame.draw.rect(screen, (250, 0, 250), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                    pygame.draw.rect(screen, (0, 0, 0), (blockSize * i + tm.x + (tm.tileSize/8), blockSize * j + tm.y + (tm.tileSize/8), blockSize*3/4, blockSize*3/4))
                    pygame.draw.rect(screen, (250, 0, 250), (blockSize * i + tm.x + (tm.tileSize/4), blockSize * j + tm.y + (tm.tileSize/4), blockSize/2, blockSize/2))
                    pygame.draw.rect(screen, (0, 0, 0), (blockSize * i + tm.x + (tm.tileSize*3/8), blockSize * j + tm.y + (tm.tileSize*3/8), blockSize/4, blockSize/4))
                if int(tm.map[j][i]) == 3 or int(tm.map[j][i]) == 4:
                    pygame.draw.rect(screen, (0, 0, 250), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize/4))
                    pygame.draw.rect(screen, (210, 180, 140), (blockSize * i + tm.x, blockSize * j + tm.y + blockSize/4, blockSize, blockSize*3/4))
                if int(tm.map[j][i]) == 7:
                    pygame.draw.rect(screen, (0, 255, 0), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
        pygame.draw.rect(screen, (255, 0, 0), (player.x + tm.x, player.y + tm.y, player.width, player.height))
    
    pygame.display.update()

        