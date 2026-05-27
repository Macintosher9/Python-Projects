import pygame
import sys
from pygame import mixer
pygame.init()
pygame.font.init()
pygame.mixer.init()
mixer.music.load("jazzCafe.mp3")
mixer.music.set_volume(0.0)
mixer.music.play(-1)

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("AP CSP Final Project")

width = screen.get_width()
height = screen.get_height()

background = (196, 196, 196)
black = (0,0,0)
grey = (58,58,58)

musicFont = pygame.font.SysFont("Avenis", 50)
musicTxt = musicFont.render("Music", True, (0,0,0))
musicRect = musicTxt.get_rect(center=(width/2, height/2-50))
ground = pygame.Rect((0, 540), (1280, 00))
track = pygame.Rect((540, 360), (200, 10))
knob = pygame.Rect((540,345), (10, 40))
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
    screen.blit(musicTxt, musicRect)
    pygame.draw.rect(screen, grey, track)
    pygame.draw.rect(screen, black, knob)
    pygame.draw.rect(screen, black, ground)
    
    pygame.display.flip()
pygame.quit()
sys.exit()