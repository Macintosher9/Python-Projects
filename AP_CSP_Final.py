import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("AP CSP Final Project")
background = (196, 196, 196)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        screen.fill(background)
        pygame.draw.rect(screen, (82, 88, 209),
                        [440, 310, 400, 100], 0)
        pygame.display.update()
        
pygame.quit()
sys.exit()