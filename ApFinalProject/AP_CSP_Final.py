import pygame
import sys
from pygame import mixer
pygame.init()
pygame.font.init()
pygame.mixer.init()
mixer.music.load("jazzCafe.mp3")
mixer.music.set_volume(0.0)
mixer.music.play(-1)

# Screen
screen = pygame.display.set_mode((1280,720))
ground = pygame.Rect((0, 540), (1280, 30))
pygame.display.set_caption("AP CSP Final Project")

width = screen.get_width()
height = screen.get_height()

# Colors
background = (196, 196, 196)
black = (0,0,0)
grey = (58,58,58)

# Music Settings Stuff
musicFont = pygame.font.Font("roboto\\Roboto-Black.ttf", 50)
musicTxt = musicFont.render("Music", True, (0,0,0))
musicRect = musicTxt.get_rect(center=(width/2, height/2-50))
volFont = pygame.font.Font("roboto\\Roboto-Black.ttf", 20)
track = pygame.Rect((540, 360), (200, 10))
knob = pygame.Rect((540,345), (20,20))
knobR = 10
knob.centery = track.centery

# Player Properties
player = pygame.Rect()
playerRad = 15

track_value = 0.0
running = True
dragging = False

while running:
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            running = False
        
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if knob.collidepoint(ev.pos):
                    dragging = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:
                dragging = False
        elif ev.type == pygame.MOUSEMOTION:
            if dragging:
                knob.centerx = max(track.left, min(ev.pos[0], track.right))
                track_value = (knob.centerx - track.left) / track.width
                mixer.music.set_volume(track_value)
                print(f"Volume: {track_value:.2f}", end="\r")
    
    screen.fill(background)
    pygame.draw.rect(screen, black, ground)
    
    def musicRoom():
        screen.blit(musicTxt, musicRect)
    
        pygame.draw.rect(screen, grey, track)
        pygame.draw.circle(screen, black, knob.center, knobR)
    
        perNum = int(track_value*100)
        pertxt = volFont.render(f"{perNum}%", True, black)
        screen.blit(pertxt, (track.right +15, track.centery-10))
    
    musicRoom()
    pygame.display.flip()
pygame.quit()
sys.exit()