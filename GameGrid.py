# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:50:36 2021

@author: mrbar
"""
from pygame import mixer
import pygame

pygame.init()

WIDTH = 25
HEIGHT = 28
MARGIN = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
FPS = 1000
HIGH_SCORE = 0 

clock = pygame.time.Clock()

window = (495, 610)
screen = pygame.display.set_mode(window)

PacManStart = pygame.transform.scale(pygame.image.load("PacManStart.png"), (WIDTH - 1, HEIGHT + 1))
PacManStartRect = PacManStart.get_rect(topleft = ((window[0] // 2) - 13, (window[1] // 2) + 131))
PacManLeft = pygame.transform.scale(pygame.image.load("PacManLeft.png"), (WIDTH - 1, HEIGHT + 1))
PacManLeftRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 2, (window[1] // 2) + 11))
PacManRight = pygame.transform.scale(pygame.image.load("PacManRight.png"), (WIDTH - 1, HEIGHT + 1))
PacManRightRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 5, (window[1] // 2) + 11))
PacManUp = pygame.transform.scale(pygame.image.load("PacManUp.png"), (WIDTH - 1, HEIGHT + 1))
PacManUpRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 5, (window[1] // 2) + 11))
PacManDown = pygame.transform.scale(pygame.image.load("PacManDown.png"), (WIDTH - 1, HEIGHT + 1))
PacManDownRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 5, (window[1] // 2) + 11))
Dot = pygame.transform.scale(pygame.image.load("Dot.png"), (WIDTH // 2, HEIGHT // 2))
Background = pygame.transform.scale(pygame.image.load('Background.png'), window)

current_image = PacManStart
current_rect_image = PacManStartRect

matrix = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
          [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
          [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
          [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
          [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
          [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
          [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
          [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
          [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
          [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
          [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
          [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
          [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
          [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
          [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

walls_list, dots_list, power_up_list = [], [], []
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if matrix[row][column] == 1:
            color = WHITE
        if matrix[row][column] == 0:
            color = YELLOW
        if color == WHITE:
            walls_list.append(pygame.draw.rect(screen, color, 
                            [(MARGIN + WIDTH) * column + MARGIN, 
                             (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH, HEIGHT]))
        if row == 2 and column == 1 or row == 2 and column == 17 or \
           row == 15 and column == 1 or row == 15 and column == 17:
           power_up_list.append(pygame.draw.rect(screen, color, 
                              [(MARGIN + WIDTH) * column + MARGIN, 
                               (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH, HEIGHT]))
        if row == 2 and column == 1 or row == 2 and column == 17 or \
           row == 15 and column == 1 or row == 15 and column == 17 or \
           row == 6 and column == 8 or row == 6 and column == 10 or \
           row == 7 and column in range(6, 13) or row == 8 and column == 6 or \
           row == 8 and column == 12 or row  == 10 and column == 6 or \
           row == 10 and column == 12 or row == 11 and column in range(6, 13) or \
           row == 12 and column == 6 or row == 12 and column == 12 or \
           row == 15 and column == 9 or row == 9 and column in range(4) or \
           row == 9 and column in range(5, 7) or row == 9 and column in range(8, 11) or \
           row == 9 and column in range(12, 14) or row == 9 and column in range(15, 19):
               continue
        if color == YELLOW:
            dots_list.append(pygame.draw.circle(Background, color, 
                            [(MARGIN + WIDTH) * column + MARGIN + 12, 
                             (MARGIN + HEIGHT) * row + MARGIN + 15], 2))

def WallDetection(x, y, current_rect_image):
    current_rect_image.right += x
    for wall in walls_list:
        if current_rect_image.colliderect(wall):
            if x < 0: 
                current_rect_image.left = wall.right
            elif x > 0:
                current_rect_image.right = wall.left
            break

    current_rect_image.top += y
    for wall in walls_list:
        if current_rect_image.colliderect(wall):
            if y < 0:
                current_rect_image.top = wall.bottom
            elif y > 0:
                current_rect_image.bottom = wall.top
            break
    
def EatGhosts(PacManRect, HIGH_SCORE):
    for power_up in power_up_list:
        print('PacManRect', PacManRect)
        print('power_up', power_up)
        if PacManRect.center == power_up.center:
            print(PacManRect.center)
            print(power_up.center)
            print('YUM')
            HIGH_SCORE += 60
            print(HIGH_SCORE)
            if power_up not in stack:
                #screen.blit(Background, (0, 0))
                stack.append(power_up)
                mixer.music.load("pacman_eatghost.wav")
                mixer.music.play()
    print()
                        
def Teleport(current_image_rect):
    if current_image_rect.right > window[0] + 20:
        current_image_rect.right = 0
    if current_image_rect.right < 0:
        current_image_rect.right = window[0] + 20

mixer.init()
stack = []
run = True
while True:  

    for power_up in power_up_list:
        if power_up in stack:
            continue
        screen.blit(Dot, (power_up.x + 6, power_up.y + 6))
        pygame.display.update()

    screen.blit(Background, (0, 0))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            pygame.key.set_repeat(70, 75)
            if key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
                current_image = PacManLeft
                PacManLeftRect = current_rect_image
                pygame.draw.rect(PacManLeft, YELLOW, PacManLeftRect)
                WallDetection(-5, 0, PacManLeftRect)
                EatGhosts(PacManLeftRect, HIGH_SCORE)
                Teleport(PacManLeftRect)
            if key[pygame.K_RIGHT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
                current_image = PacManRight
                PacManRightRect = current_rect_image
                pygame.draw.rect(PacManRight, YELLOW, PacManRightRect)
                WallDetection(5, 0, PacManRightRect)
                EatGhosts(PacManRightRect, HIGH_SCORE)
                Teleport(PacManRightRect)  
            if key[pygame.K_UP] and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                current_image = PacManUp
                PacManUpRect = current_rect_image
                pygame.draw.rect(PacManUp, YELLOW, PacManUpRect)
                WallDetection(0, -5, PacManUpRect)
                EatGhosts(PacManUpRect, HIGH_SCORE)
            if key[pygame.K_DOWN] and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                current_image = PacManDown
                PacManDownRect = current_rect_image
                pygame.draw.rect(PacManDown, YELLOW, PacManDownRect)
                WallDetection(0, 5, PacManDownRect)
                EatGhosts(PacManDownRect, HIGH_SCORE)
                
    screen.blit(current_image, current_rect_image)   
    pygame.display.update()             
    screen.blit(PacManStart, PacManStartRect)
pygame.quit()