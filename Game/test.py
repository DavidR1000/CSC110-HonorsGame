import sys, pygame, player
pygame.init()

screen = 600, 600
black = 0, 0, 0

moveSpeed = [0, 0]

screen = pygame.display.set_mode(screen)

ball = pygame.image.load("HonorsGame\Example\intro_ball.gif")
playerImage = ball.get_rect()

player = player.player()

while True:
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
    playerImage = playerImage.move(player.moveSpeed)

    screen.fill(black)
    screen.blit(ball, playerImage)
    pygame.display.flip()
        