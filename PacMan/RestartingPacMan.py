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
FPS = 50
# Colors (RED,GREEN,BLUE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Sets the WIDTH and HEIGHT of the window
WINDOW = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Displays the screen
SCREEN = pygame.display.set_mode(WINDOW)
CLOCK = pygame.time.Clock()

PacManStartSurface = pygame.transform.scale(pygame.image.load 
                                           ("PacManStart.png").convert(), 
                                           (25, 25))
PacManSurface = pygame.transform.scale(pygame.image.load 
                                      ("PacManRight.png").convert(), (25, 25))
PacManRect = PacManStartSurface.get_rect(topleft = (((SCREEN_WIDTH - 22) // 2),
                                        (SCREEN_HEIGHT + 225) // 2))

BackgroundSurface = pygame.transform.scale(pygame.image.load
                                          ("Background.png").convert(), 
                                          (SCREEN_WIDTH - 2, 
                                           SCREEN_HEIGHT - 82))
BackgroundRect = BackgroundSurface.get_rect(topleft = (0, 41))
        
class PacMan(pygame.sprite.Sprite):
    def __init__(self):
        # Grabs everything from Sprite Class
        pygame.sprite.Sprite.__init__(self)
        self.image = PacManStartSurface
        self.rect = PacManRect
        self.mask = pygame.mask.from_surface(self.image)
        self.DIRECTION = ""
        self.LIVES = 3
        
class Dot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load 
                                           ("Dot.png").convert(), (4, 4))
        self.mask = pygame.mask.from_surface(self.image)
        
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("PowerUp.png")
                                            .convert(), (23, 23))
        self.mask = pygame.mask.from_surface(self.image)
        
class Ghosts(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.YellowGhostImage = pygame.transform.scale(pygame.image.load 
                                                      ("YellowGhost.png")
                                                       .convert(), (23, 23))
        self.YellowGhostRect = self.YellowGhostImage.get_rect(topleft = 
                                                             (235, 347))
        self.YellowGhostMask = pygame.mask.from_surface(self.YellowGhostImage)
        self.RedGhostImage = pygame.transform.scale(pygame.image.load 
                                                   ("RedGhost.png")
                                                   .convert(), (23, 23))
        self.RedGhostRect = self.RedGhostImage.get_rect(topleft = 
                                                       (235, 347))
        self.RedGhostMask = pygame.mask.from_surface(self.RedGhostImage)
        self.BlueGhostImage = pygame.transform.scale(pygame.image.load 
                                                    ("BlueGhost.png")
                                                    .convert(), (23, 23))
        self.BlueGhostRect = self.BlueGhostImage.get_rect(topleft = 
                                                         (235, 347))
        self.BlueGhostMask = pygame.mask.from_surface(self.BlueGhostImage)
        self.PinkGhostImage = pygame.transform.scale(pygame.image.load 
                                                    ("PinkGhost.png")
                                                    .convert(), (23, 23))
        self.PinkGhostRect = self.PinkGhostImage.get_rect(topleft = 
                                                         (235, 347))
        self.PinkGhostMask = pygame.mask.from_surface(self.PinkGhostImage)
        
class Maze(Dot, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.DOTS = []
        self.WALLS = []
        self.BLOCK_WIDTH = 22
        self.BLOCK_HEIGHT = 22
        self.ROWS = 21
        self.COLUMNS = 20
        self.MARGIN = 3
        # 0 - Dots
        # 1 - Walls
        # 2 - Power Up
        # 3 - Empty Space
        # 4 - Ghosts
        self.MATRIX = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], \
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], \
                      [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1], \
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], \
                      [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1], \
                      [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1], \
                      [1,1,1,1,0,1,1,1,3,1,3,1,1,1,0,1,1,1,1], \
                      [3,3,3,1,0,1,3,3,3,3,3,3,3,1,0,1,3,3,3], \
                      [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1], \
                      [0,0,0,0,0,3,3,1,4,4,4,1,3,3,0,0,0,0,0], \
                      [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1], \
                      [3,3,3,1,0,1,3,3,3,3,3,3,3,1,0,1,3,3,3], \
                      [1,1,1,1,0,1,3,1,1,1,1,1,3,1,0,1,1,1,1], \
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], \
                      [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1], \
                      [1,0,0,1,0,0,0,0,0,3,0,0,0,0,0,1,0,0,1], \
                      [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1], \
                      [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1], \
                      [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1], \
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], \
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        
    def DrawGrid(self):
        for ROW in range(self.ROWS):
            for COLUMN in range(self.COLUMNS - 1):
                if self.MATRIX[ROW][COLUMN] == 0:
                    self.rect = self.image.get_rect(topleft = 
                                                   [((self.MARGIN 
                                                   + self.BLOCK_WIDTH)
                                                   * COLUMN + self.MARGIN) 
                                                   + 10,
                                                   ((self.MARGIN 
                                                   + self.BLOCK_HEIGHT) 
                                                   * ROW + self.MARGIN) + 50])
                    self.DOTS.append(self.rect)
                    '''
                    self.image = pygame.draw.circle(SCREEN, YELLOW, 
                                  [((self.MARGIN + self.BLOCK_WIDTH)
                                  * COLUMN + self.MARGIN) + 10,
                                  ((self.MARGIN + self.BLOCK_HEIGHT) 
                                  * ROW + self.MARGIN) + 50], 2)
                    self.image = pygame.Surface((self.image.width,
                                                self.image.height))
                    self.mask = pygame.mask.from_surface(self.image)
                    self.DOTS.append(self.mask)
                    '''
                if self.MATRIX[ROW][COLUMN] == 1:
                    self.WALLS.append(pygame.draw.rect(SCREEN, WHITE,
                                     [((self.MARGIN + self.BLOCK_WIDTH)
                                     * COLUMN + self.MARGIN) - 2,
                                     ((self.MARGIN + self.BLOCK_HEIGHT) 
                                     * ROW + self.MARGIN) + 40, 
                                     self.BLOCK_WIDTH, self.BLOCK_HEIGHT]))

class Main(PacMan, Maze):
    def __init__(self):
        super().__init__()
        # Inherits PacMan class
        PacMan.__init__()
        # Inherits Maze class
        Maze.__init__()
        self.SCORE = 0
        self.HIGH_SCORE = 0
        
    def Movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not key[pygame.K_UP] \
                              and not key[pygame.K_DOWN]:
            self.rect.x -= SPEED
            self.DIRECTION = "LEFT"
        if key[pygame.K_RIGHT] and not key[pygame.K_UP] \
                               and not key[pygame.K_DOWN]:
            self.rect.x += SPEED
            self.DIRECTION = "RIGHT"
        if key[pygame.K_UP] and not key[pygame.K_LEFT] \
                            and not key[pygame.K_RIGHT]:
            self.rect.y -= SPEED
            self.DIRECTION = "UP"
        if key[pygame.K_DOWN] and not key[pygame.K_LEFT] \
                              and not key[pygame.K_RIGHT]:
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
        if self.DIRECTION == "RIGHT":
            self.image = PacManSurface
        if self.DIRECTION == "UP":
            self.image = pygame.transform.rotate(PacManSurface, 90)
        if self.DIRECTION == "DOWN":
            self.image = pygame.transform.rotate(PacManSurface, 270)
        
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
                elif x > 0:
                    self.rect.right = wall.left
                break
        
        self.rect.top += y
        for wall in self.WALLS:
            collide = self.rect.colliderect(wall)
            if collide:
                if y < 0:
                    self.rect.top = wall.bottom
                if y > 0:
                    self.rect.bottom = wall.top
                break
            
    def EatDots(self):
        pygame.sprite.spritecollideany(PacManRect, MazeDotSprites, True)
            
    def ShowText(self):
        font = pygame.font.Font("emulogic.ttf", 15)
        OneUpText = font.render("1UP", True, WHITE)
        OneUpTextRect = OneUpText.get_rect(center = (70, 10))
        OneUpScoreText = font.render("00", True, WHITE)
        OneUpScoreRect = OneUpScoreText.get_rect(center = 
                                                ((SCREEN_WIDTH - 290) 
                                                 // 2, 26))
        HighScoreText = font.render("High Score", True, WHITE)
        HighScoreTextRect = HighScoreText.get_rect(center = 
                                                  (SCREEN_WIDTH // 2, 10))
        HighScoreNumber = font.render("00", True, WHITE)
        HighScoreNumberRect = HighScoreNumber.get_rect(center = 
                                                      ((SCREEN_WIDTH + 90) 
                                                       // 2, 26))

        SCREEN.blit(HighScoreText, HighScoreTextRect)
        SCREEN.blit(HighScoreNumber, HighScoreNumberRect)
        SCREEN.blit(OneUpText, OneUpTextRect)
        SCREEN.blit(OneUpScoreText, OneUpScoreRect)
        
    def PacManBite(self):
        SCREEN.blit(PacManStartSurface, PacManRect)
        pygame.display.update() 
        
PacMan = PacMan()
PacManSprite = pygame.sprite.Group()
PacManSprite.add(PacMan)

Maze = Maze()
MazeDotSprites = pygame.sprite.Group()
MazeDotSprites.add(Maze) 

Player = Main()
Sprites = pygame.sprite.Group() 
Sprites.add(Player)
    
run = True
while run:
    Player.PacManBite()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            Player.Movement()
            Player.ChangeImage()
            Player.Teleport()   
            
    Player.ContinueMovement()
    Player.EatDots()
    
    pygame.display.update()
    SCREEN.fill(BLACK)
    Player.DrawGrid()
    #SCREEN.blit(BackgroundSurface, BackgroundRect)
    CLOCK.tick(FPS)
    Sprites.draw(SCREEN)
    Player.ShowText()
            
pygame.quit()