import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Detecting Key inputs")

WHITE = (255, 255, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
sys.exit()