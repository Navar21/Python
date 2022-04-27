# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:40:02 2022

@author: mrbar
"""

import pygame

pygame.init()
pygame.display.set_caption("Pac-Man")

# Sets the size of the screen via (WIDTH, HEIGHT)
SCREEN_WIDTH = 475
SCREEN_HEIGHT = 608
# Speed of Characters
SPEED = 1
# Frames per second, how fast the game runs
FPS = 100
# Colors (RED,GREEN,BLUE)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (0,0,255)

# Sets the WIDTH and HEIGHT of the window
window = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Displays the screen
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()

# When an image is loaded, a new Surface is created
# Resizes the surface to (35,35)
PacManStartSurface = pygame.transform.scale(pygame.image.load 
                     ("PacManStart.png").convert(), (23, 23))
PacManSurface = pygame.transform.scale(pygame.image.load 
                ("PacManRight.png").convert(), (23, 23))
# A rect object wraps around a Surface and plots its coordinates 
# relative to the Surface attached, not the screen
PacManRect = PacManStartSurface.get_rect(topleft = (((SCREEN_WIDTH - 22) // 2),
                                                    (SCREEN_HEIGHT + 26) // 2))
ImageSurface = pygame.transform.scale(pygame.image.load
                               ("Background.png").convert(), 
                               (SCREEN_WIDTH - 1, SCREEN_HEIGHT - 82))
ImageRect = ImageSurface.get_rect(topleft = (0, 41))
PowerUp = pygame.transform.scale(pygame.image.load("Dot.png").convert(), 
                                 (24, 24))
PowerUpRect = PowerUp.get_rect(topleft = (235, 347))

class Maze():
    def __init__(self):
        self.WALLS = []
        self.DOT = []
        self.BLOCK_WIDTH = 22
        self.BLOCK_HEIGHT = 22
        self.ROWS = 21
        self.COLUMNS = 20
        self.MARGIN = 3
        # 0 - Dots
        # 1 - Walls
        # 2 - PowerUp
        self.MATRIX = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], \
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], \
                      [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1], \
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], \
                      [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1], \
                      [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1], \
                      [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1], \
                      [0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0], \
                      [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1], \
                      [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0], \
                      [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1], \
                      [0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0], \
                      [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1], \
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], \
                      [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1], \
                      [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1], \
                      [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1], \
                      [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1], \
                      [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1], \
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], \
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        
    def DrawGrid(self):
        for ROW in range(self.ROWS):
            for COLUMN in range(self.COLUMNS - 1):
                if self.MATRIX[ROW][COLUMN] == 0:
                    pass
                if self.MATRIX[ROW][COLUMN] == 1:
                    self.WALLS.append(pygame.draw.rect(screen, WHITE,
                             [((self.MARGIN + self.BLOCK_WIDTH) * COLUMN 
                              + self.MARGIN) - 2,
                              ((self.MARGIN + self.BLOCK_HEIGHT) * ROW 
                              + self.MARGIN) + 40, 
                              self.BLOCK_WIDTH, self.BLOCK_HEIGHT]))
                
class PacMan(pygame.sprite.Sprite):
    def __init__(self):
        # Grabs everything from Sprite Class
        super().__init__()
        self.image = PacManStartSurface
        self.rect = PacManRect
        self.DIRECTION = ""

class Main(PacMan, Maze):
    def __init__(self):
        # Inherits PacMan class
        PacMan.__init__(self)
        # Inherits Maze class
        Maze.__init__(self)
        self.SCORE = 0
        self.HIGH_SCORE = 0
        
    def Movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= SPEED
            self.DIRECTION = "LEFT"
        if key[pygame.K_RIGHT]:
            self.rect.x += SPEED
            self.DIRECTION = "RIGHT"
        if key[pygame.K_UP]:
            self.rect.y -= SPEED
            self.DIRECTION = "UP"
        if key[pygame.K_DOWN]:
            self.rect.y += SPEED
            self.DIRECTION = "DOWN"
            
    def ContinueMovement(self):
        if self.DIRECTION == "LEFT":
            self.rect.x -= SPEED
            Main.WallDetection(self, -1, 0)
        if self.DIRECTION == "RIGHT":
            self.rect.x += SPEED
            Main.WallDetection(self, 1, 0)
        if self.DIRECTION == "UP":
            self.rect.y -= SPEED
            Main.WallDetection(self, 0, -1)
        if self.DIRECTION == "DOWN":
            self.rect.y += SPEED
            Main.WallDetection(self, 0, 1)

    def ChangeImage(self):
        if self.DIRECTION == "LEFT":
            self.image = pygame.transform.rotate(PacManSurface, 180)
            PacManLeftRect = self.rect
        if self.DIRECTION == "RIGHT":
            self.image = PacManSurface
            PacManRightRect = self.rect
        if self.DIRECTION == "UP":
            self.image = pygame.transform.rotate(PacManSurface, 90)
            PacManUpRect = self.rect
        if self.DIRECTION == "DOWN":
            self.image = pygame.transform.rotate(PacManSurface, 270)
            PacManDownRect = self.rect
        
    def Teleport(self):
        if self.rect.right < 0:
            self.rect.right = SCREEN_WIDTH + 20
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
    
    def WallDetection(self, x, y):
        self.rect.right += x
        for wall in self.WALLS:
            collide = self.rect.colliderect(wall)
            if collide:
                if x < 0: 
                    self.rect.left = wall.right
                elif x > 0 :
                    self.rect.right = wall.left
                break

        self.rect.top += y
        for wall in self.WALLS:
            collide = self.rect.colliderect(wall)
            if collide:
                if y < 0:
                    self.rect.top = wall.bottom
                elif y > 0:
                    self.rect.bottom = wall.top
                break
        
Player = Main()
# Sprites come with Surface and Rect
AllSprites = pygame.sprite.Group() 
AllSprites.add(Player)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            Player.Movement()
            Player.ChangeImage()
            Player.Teleport()   
            
    Player.ContinueMovement()
    
    AllSprites.draw(screen)
    screen.blit(Player.image, Player.rect)
    pygame.display.update()
    screen.fill(BLACK)
    Player.DrawGrid()
    screen.blit(ImageSurface, ImageRect)
    clock.tick(FPS)
            
pygame.quit()