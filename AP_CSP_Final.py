import pygame
import sys
from pygame import mixer
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("AP CSP Final Project")

width = screen.get_width()
height = screen.get_height()

background = (196, 196, 196)
black = (0,0,0)

musicFont = pygame.font.SysFont("Avenis", 50)
musicTxt = musicFont.render("Music", True, (0,0,0))
musicRect = musicTxt.get_rect(center=(width/2, height/2-50))

running = True
while running:
    
    screen.fill(background)
    screen.blit(musicTxt, musicRect)
    pygame.draw.line(screen, black, (540, 360), (740, 360), 6)
    pygame.draw.rect(screen, black, ((740, 335), (10, 50)))
    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()
pygame.quit()
sys.exit()