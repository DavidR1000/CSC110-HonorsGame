import sys, pygame, player, time, TileMap
pygame.init()

blockSize = 64

width = blockSize * 11
height = blockSize * 11

screen = width, height
black = 0, 0, 0

#flags = pygame.OPENGL | pygame.FULLSCREEN
#screen = pygame.display.set_mode((1000, 1000), flags)

screen = pygame.display.set_mode(screen)

tm = TileMap.TileMap("HonorsGame\Game\world.txt", blockSize)
player = player.player(tm)


while True:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                player.up = True
            if event.key == pygame.K_a:
                player.left = True
            if event.key == pygame.K_s:
                player.down = True
            if event.key == pygame.K_d:
                player.right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.up = False
            if event.key == pygame.K_a:
                player.left = False
            if event.key == pygame.K_s:
                player.down = False
            if event.key == pygame.K_d:
                player.right = False

    player.update()
    screen.fill(black)
    for i in range(len(tm.map[0])):
        for j in range(len(tm.map)):
            #print("j: ", j)
            if int(tm.map[j][i]) == 0:
                pygame.draw.rect(screen, (0, 0, 0), (64 * i, 64 * j, 64, 64))
            if int(tm.map[j][i]) == 1:
                pygame.draw.rect(screen, (210, 180, 140), (64 * i, 64 * j, 64, 64))
    pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.width, player.height))
    pygame.display.update()

        