import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("AP CSP Final Project")

width = screen.get_width
height = screen.get_height
background = (196, 196, 196)

buttonFont = pygame.font.Font('Vogue.ttf', 50)
Txt1 = buttonFont.render('Press Here', True, (0,0,0))
Txtrect = Txt1.get_rect()
Txtrect.center = (640, 360)

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        
        screen.fill(background)
        pygame.draw.rect(screen, (82, 88, 209), [440, 310, 400, 100], 0)
        screen.blit(Txt1, Txtrect)
        pygame.display.update()
        
        
pygame.quit()
sys.exit()