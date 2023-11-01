import sys, pygame, player, platform, TileMap, teleport

pygame.init()

width = 1000
height = 700

screen = width, height

black = 0, 0, 0

blockSize = 64

platforms = []

countTeleport = 5

portalExist = False

screen = pygame.display.set_mode(screen)

tm = TileMap.TileMap("HonorsGame\Game\world.txt", blockSize)
for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 2:
                player = player.player(tm, i*blockSize, j*blockSize, width, height)
                tm.map[j][i] = 1

for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 3:
                platforms.append(platform.platform(tm, j, i, player))
                tm.map[j][i] = 1
            if int(tm.map[j][i]) == 5:
                portal = teleport.teleport(i, j, player, tm)
                portalExist = True

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

    player.update()
    for i in range(len(platforms)):
        platforms[i].update()
    portal.update()
    screen.fill(black)
    for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 0:
                pygame.draw.rect(screen, (0, 0, 0), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
            if int(tm.map[j][i]) == 1 or int(tm.map[j][i]) == 2:
                pygame.draw.rect(screen, (210, 180, 140), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
            if int(tm.map[j][i]) == 5 or int(tm.map[j][i]) == 6:
                pygame.draw.rect(screen, (250, 0, 250), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize))
                pygame.draw.rect(screen, (250, 250, 250), (blockSize * i + tm.x + (tm.tileSize/8), blockSize * j + tm.y + (tm.tileSize/8), blockSize*3/4, blockSize*3/4))
                pygame.draw.rect(screen, (250, 0, 250), (blockSize * i + tm.x + (tm.tileSize/4), blockSize * j + tm.y + (tm.tileSize/4), blockSize/2, blockSize/2))
                pygame.draw.rect(screen, (250, 250, 250), (blockSize * i + tm.x + (tm.tileSize*3/8), blockSize * j + tm.y + (tm.tileSize*3/8), blockSize/4, blockSize/4))
            if int(tm.map[j][i]) == 3 or int(tm.map[j][i]) == 4:
                pygame.draw.rect(screen, (0, 0, 250), (blockSize * i + tm.x, blockSize * j + tm.y, blockSize, blockSize/4))
                pygame.draw.rect(screen, (210, 180, 140), (blockSize * i + tm.x, blockSize * j + tm.y + blockSize/4, blockSize, blockSize*3/4))
    pygame.draw.rect(screen, (255, 0, 0), (player.x + tm.x, player.y + tm.y, player.width, player.height))
    pygame.display.update()

        