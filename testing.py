import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption(("Hello World"))
Background = (255,255,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
    screen.fill(Background)
    pygame.display.flip()
    
pygame.quit()
sys.exit()