import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

screenW = 1440
screenH = 720
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


start_ticks = 0
timer_started = False
time_string = "00:00.00"
final_time_string = "" 

fontPath = resource_path("roboto/Roboto-Regular.ttf")
font1 = pygame.font.Font(fontPath, 50)
font2 = pygame.font.Font(fontPath, 40)
font_timer = pygame.font.Font(fontPath, 35)

endGametxt = font1.render("Congrats", True, (0,0,0), (72,72,72))
startOvertxt = font2.render("Press 'R' to start over", True, (0,0,0), (72,72,72))
endGame = endGametxt.get_rect(center=(screenW/2, screenH/2))
startOver = startOvertxt.get_rect(center=(screenW/2, screenH/2+50))

# Game Platforms
platforms = [
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
        if not timer_started:
            movement_keys = [
                keys[pygame.K_a], keys[pygame.K_LEFT],
                keys[pygame.K_d], keys[pygame.K_RIGHT],
                keys[pygame.K_w], keys[pygame.K_UP], keys[pygame.K_SPACE]
            ]
            if any(movement_keys):
                timer_started = True
                start_ticks = pygame.time.get_ticks()

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
            final_time_string = time_string

    else:
        if keys[pygame.K_r]:
            playerX = 50       
            playerY = floorY   
            velY = 0           
            isJump = False
            reachedEnd = False
            timer_started = False 
            time_string = "00:00.00"


    if timer_started and not reachedEnd:
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        minutes = elapsed_ms // 60000
        seconds = (elapsed_ms % 60000) // 1000
        milliseconds = (elapsed_ms % 1000) // 10
        time_string = f"{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
    elif reachedEnd:
        time_string = final_time_string


    timer_color = (238, 75, 43) if reachedEnd else (0, 0, 0)
    timer_surface = font_timer.render(time_string, True, timer_color)


    screen.fill((182,182,182))
    
    pygame.draw.rect(screen, (0,0,0), [0, 620, 200, 100])
    for object in platforms:
        pygame.draw.rect(screen, (0,0,0), object)
        
    pygame.draw.rect(screen, (65,65,65), pygame.Rect(playerX, playerY, playerW, playerH))
    

    screen.blit(timer_surface, (30, 30))

    if reachedEnd:
        screen.blit(endGametxt, endGame)
        screen.blit(startOvertxt, startOver)
        
    pygame.display.flip()
    clock.tick(60)