import sys, pygame, player, time, TileMap
pygame.init()

width = 1000
height = 700

screen = width, height
black = 0, 0, 0

blockSize = 64

screen = pygame.display.set_mode(screen)

tm = TileMap.TileMap("HonorsGame\Game\world.txt", blockSize)
for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 2:
                player = player.player(tm, i*64, j*64, width, height)


while True:
    pygame.time.delay(10)
    
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
    screen.fill(black)
    for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            if int(tm.map[j][i]) == 0:
                pygame.draw.rect(screen, (0, 0, 0), (64 * i + tm.x, 64 * j + tm.y, 64, 64))
            if int(tm.map[j][i]) == 1 or int(tm.map[j][i]) == 2:
                pygame.draw.rect(screen, (210, 180, 140), (64 * i + tm.x, 64 * j + tm.y, 64, 64))
    pygame.draw.rect(screen, (255, 0, 0), (player.x + tm.x, player.y + tm.y, player.width, player.height))
    pygame.display.update()

        