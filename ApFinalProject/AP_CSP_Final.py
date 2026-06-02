import pygame
import sys
from pygame import mixer
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Screen Setup
screenwidth = 1440
screenheight = 720
screen = pygame.display.set_mode((screenwidth, screenheight))
# Colors
Black = (0,0,0)
gray1 = (82,82,82)
gray2 = (140,140,140)
gray3 = (183,183,183)
gray4 = (232,232,232)

# Music Setup
mFont = pygame.font.Font("roboto\\Roboto-Medium", 48)
mTxt = mFont.render("Music Volume", True, Black)
mRect = mTxt.get_rect(center=(screen//2, 80))
vFont = pygame.font.Font("roboto\\Roboto-Medium", 28)

class slider:
    def __init__(self, x, y, width):
        self.track = pygame.Rect((x, y), (width, 10))
        self.knob = pygame.Rect((x, y-15), (20, 20))
        self.knobR = 10
        self.knob.centery = self.track.centery
        self.dragging = False
        self.vol = 0.5
        self.knob.centerx = self.track.left + int(self.vol*self.track.width)
    
    def handlevent(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            self.dragging = True
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            self.dragging = False
        elif ev.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.knob.centerx = max(self.track.left, min(ev.pos[0], self.track.right))
                self.vol = (self.knob.centerx - self.track.right) / self.track.width
    def draw(self, surface):
        pygame.draw.rect(surface, gray3, self.track)
        pygame.draw.circle(surface, Black, self.knob.center, self.knobR)
        numPer = int(self.vol * 100)
        txtPer = vFont.render(f"{numPer}%", True, Black)
        surface.blit(txtPer, (self.track.right + 15, self.track.centery - 12))

class level:
    def __init__ (self, mapLayout, tileSize, blockColor, bgColor)
        self.mapyLayout = mapLayout
        self.tileSize = tileSize
        self.blockColor = blockColor
        self.bgColor = bgColor
        self.platform = []
        self.generateLvl()
    def generateLvl(self):
        for rowInd, row in enumerate(self.mapyLayout):
            for colInd, cell in enumerate(row):
                if cell == "X":
                    x = colInd * self.tileSize
                    y = rowInd * self.tileSize
                    rect = pygame.Rect(x, y, self.tileSize, self.tileSize)
                    self.platform.append(rect)
    def draw(self, surface):
        for platform in self.platform:
            pygame.draw.rect(surface, self.blockColor, platform)

class Player:
    def __init__ (self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.speed = 7
        self.xVal = 0
        self.yVal = 0
        self.grav = 0.8
        self.jumpStrength = -16
        self.grounded = False
    def update(self, platforms):
        keys = pygame.key.get_just_pressed
        self.xVal = 0
        if keys[pygame.K_LEFT] or [pygame.K_a]
            self.xVal = -self.speed
        if keys[pygame.K_RIGHT] or [pygame.k_d]:
            self.xval = self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.grounded:
            self.yVal += self.jumpStrength
            self.grounded = False
        
        self.yVal += self.grav
        self.rect.x += self.xVal
        for platform in platforms:
            if self.rect.collidepoint(platform):
                if self.xVal > 0: self.rect.right == platform.left
                if self.xVal < 0: self.rect.left == platform.right
        
        self.rect.y += self.yVal
        self.grounded = False
        for platform in platforms:
            # for Falling
            if self.yVal > 0:
                self.rect.bottom = platform.top
                self.yVal = 0
                self.grounded = True
            # for jumping
            if self.yVal < 0:
                self.rect.top = self.rect.bottom
                self.yVal = 0
    def draw(self, surface):
        pygame.draw.rect(surface, gray3, self.rect)

volSlider = Slider(540, 140, 200)