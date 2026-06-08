import pygame
import sys
pygame.init()

screenW=1440
screenH=720
screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()

floorY = screenH - 120

# Player Properties
playerW = 20
playerH = 20
playerX = 50
playerY = floorY
playerSpeed = 5
gravity = 1
jumpForce = 15

velY = 0
isJump = False

font1 = pygame.font.Font("roboto/Roboto-Regular.ttf", 50)
font2 = pygame.font.Font("roboto/Roboto-Regular.ttf", 40)
endGametxt = font1.render("Congrats", True, (0,0,0), (58,58,58))
startOvertxt = font2.render("Press 'R' to start over", True, (0,0,0), (58,58,58))
endGame = endGametxt.get_rect(center=(screenW/2, screenH/2))
startOver = startOvertxt.get_rect(center=(screenW/2, screenH/2-50))

# Game Platforms
platforms = [
    # Platforms
    pygame.Rect(100, 570, 100, 50),
    pygame.Rect(300, 520, 100, 50),
    pygame.Rect(500, 470, 100, 50),
    pygame.Rect(700, 420, 100, 50),
    pygame.Rect(700, 320, 100, 50),
    pygame.Rect(700, 220, 100, 50),
    pygame.Rect(850, 400, 100, 50),
    pygame.Rect(850, 300, 100, 50),
    pygame.Rect(850, 200, 100, 50),
    pygame.Rect(950, 200, 25, 250),
    pygame.Rect(1050, 400, 100, 50),
    pygame.Rect(1250, 500, 290, 50)
]
LevelIndex = 0
running = True
reachedEnd = False
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if not reachedEnd:
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and playerX > 0:
            playerX -= playerSpeed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and playerX < screenW - playerW:
            playerX += playerSpeed
            
        playerX_HB = pygame.Rect(playerX, playerY + 2, playerW, playerH - 4)
        
        for plat in platforms:
            if playerX_HB.colliderect(plat):
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    playerX = plat.left - playerW
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    playerX = plat.right
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and not isJump:
            velY = -jumpForce
            isJump = True
            
        # Gravity Stuff
        velY += gravity
        playerY += velY
        

        playerHB = pygame.Rect(playerX, playerY, playerW, playerH)
        
        onPlatform = False
        
        for plat in platforms:
            if playerHB.colliderect(plat):
                if velY > 0:
                    if (playerHB.bottom - velY) <= plat.top:
                        playerY = plat.top - playerH
                        velY = 0
                        isJump = False
                        onPlatform = True
                elif velY < 0:
                    if (playerHB.top - velY) >= plat.bottom:
                        playerY = plat.bottom
                        velY = 0
        

        if playerY >= floorY and playerX <= 200:
            playerY = floorY
            velY = 0
            isJump = False
            onPlatform = True
            
        if not onPlatform and velY == 0:
            isJump = True

        if playerY > screenH:
            playerX = 50       
            playerY = floorY   
            velY = 0           
            isJump = False
        if playerX >= screenW - playerW:
            reachedEnd = True
    else:
        if keys[pygame.K_r]:
            playerX = 50       
            playerY = floorY   
            velY = 0           
            isJump = False
            reachedEnd = False

    screen.fill((182,182,182))
    
    # Draw Menu/Ground
    pygame.draw.rect(screen, (0,0,0), [0, 620, 200, 100])
    for object in platforms:
        pygame.draw.rect(screen, (0,0,0), object)
    pygame.draw.rect(screen, (65,65,65), pygame.Rect(playerX, playerY, playerW, playerH))
    if reachedEnd:
        screen.blit(endGametxt, endGame)
        screen.blit(startOvertxt, startOver)
        
    pygame.display.flip()
    clock.tick(60)