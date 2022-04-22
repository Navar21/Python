# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:40:02 2022

@author: mrbar
"""

import pygame

class Constants():
    def __init__(self):        
        # Sets the size of the screen via (WIDTH, HEIGHT)
        self.WIDTH = 490
        self.HEIGHT = 621
        # Resizing the rectangle that wraps around the surface images
        self.SURFACE_RESIZE = 35
        # Speed of Characters
        self.VELOCITY = 1
        # Frames per second, how fast the game runs
        self.FPS = 60
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.YELLOW = (255,255,0)
        self.DIRECTION = ""

class Initialize(Constants):
    pygame.init()
    pygame.display.set_caption("Pac-Man")
    def __init__(self):
        Constants.__init__(self)
        # Sets the WIDTH and HEIGHT of the window
        self.window = (self.WIDTH, self.HEIGHT)
        # Displays the screen
        self.screen = pygame.display.set_mode(self.window)
        self.clock = pygame.time.Clock()
        
class SurfacesAndRects(Constants):
    def __init__(self):
        Constants.__init__(self)
        # When an image is loaded, a new Surface is created
        self.PacManStartSurface = pygame.transform.scale(pygame.image.load \
            ("PacManStart.png"), (self.SURFACE_RESIZE, self.SURFACE_RESIZE))
        # A rect object wraps around a Surface and plots its coordinates 
        # relative to the Surface attached, not the screen
        self.PacManRect = self.PacManStartSurface.get_rect(topleft = \
                         (self.WIDTH // 2, self.HEIGHT // 2))
        self.PacManLeftSurface = pygame.transform.scale(pygame.image.load \
            ("PacManLeft.png"), (self.SURFACE_RESIZE, self.SURFACE_RESIZE))
        self.PacManLeftRect = self.PacManLeftSurface.get_rect(topleft = \
                             (self.WIDTH // 2, self.HEIGHT // 2))
        self.PacManRightSurface = pygame.transform.scale(pygame.image.load \
            ("PacManRight.png"), (self.SURFACE_RESIZE, self.SURFACE_RESIZE))
        self.PacManRightRect = self.PacManRightSurface.get_rect(topleft = \
                              (self.WIDTH // 2, self.HEIGHT // 2))
        self.PacManUpSurface = pygame.transform.scale(pygame.image.load \
            ("PacManUp.png"), (self.SURFACE_RESIZE, self.SURFACE_RESIZE))
        self.PacManUpRect = self.PacManUpSurface.get_rect(topleft = \
                           (self.WIDTH // 2, self.HEIGHT // 2))
        self.PacManDownSurface = pygame.transform.scale(pygame.image.load \
            ("PacManDown.png"), (self.SURFACE_RESIZE, self.SURFACE_RESIZE))
        self.PacManDownRect = self.PacManDownSurface.get_rect(topleft = \
                             (self.WIDTH // 2, self.HEIGHT // 2))
        # Rotates images
        self.CurrentSurface = self.PacManStartSurface
        self.CurrentRect = self.PacManRect

class PacMan(Initialize, SurfacesAndRects, Constants):
    def __init__(self):
        Initialize.__init__(self)
        SurfacesAndRects.__init__(self)
        Constants.__init__(self)
        
    def Movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.PacManRect.x -= self.VELOCITY
            self.DIRECTION = "LEFT"
        if key[pygame.K_RIGHT]:
            self.PacManRect.x += self.VELOCITY
            self.DIRECTION = "RIGHT"
        if key[pygame.K_UP]:
            self.PacManRect.y -= self.VELOCITY
            self.DIRECTION = "UP"
        if key[pygame.K_DOWN]:
            self.PacManRect.y += self.VELOCITY
            self.DIRECTION = "DOWN"
            
    def ContinueMovement(self):
        if self.DIRECTION == "LEFT":
            self.PacManRect.x -= self.VELOCITY
        if self.DIRECTION == "RIGHT":
            self.PacManRect.x += self.VELOCITY
        if self.DIRECTION == "UP":
            self.PacManRect.y -= self.VELOCITY
        if self.DIRECTION == "DOWN":
            self.PacManRect.y += self.VELOCITY

    def ChangeImage(self, CurrentSurface, CurrentRect):
        if self.DIRECTION == "LEFT":
            self.CurrentSurface = self.PacManLeftSurface
            self.PacManLeftRect = self.CurrentRect
        if self.DIRECTION == "RIGHT":
            self.CurrentSurface = self.PacManRightSurface
            self.PacManRightRect = self.CurrentRect
        if self.DIRECTION == "UP":
            self.CurrentSurface = self.PacManUpSurface
            self.PacManUpRect = self.CurrentRect
        if self.DIRECTION == "DOWN":
            self.CurrentSurface = self.PacManDownSurface
            self.PacManDownRect = self.CurrentRect
    
    def Draw(self):
        pygame.draw.rect(self.screen, Player.BLACK, (self.PacManRect.x, self.PacManRect.y, 35, 35))
        
    def Teleport(self, CurrentRect):
        if self.CurrentRect.right < 0:
            self.CurrentRect.left = self.WIDTH
            
Player = PacMan()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            Player.Movement()
            Player.ChangeImage(Player.CurrentSurface, Player.CurrentRect)
            Player.Draw()
            Player.Teleport(Player.CurrentRect)
    
    Player.ContinueMovement()
    
    Player.screen.fill(Player.BLACK)
    Player.screen.blit(Player.CurrentSurface, Player.CurrentRect)
    pygame.display.update()
    Player.screen.blit(Player.PacManStartSurface, Player.PacManRect)
    Player.clock.tick(Player.FPS)
            
pygame.quit()