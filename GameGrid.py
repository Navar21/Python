# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:50:36 2021

@author: mrbar
"""
import pygame

pygame.init()

width = 25
height = 28
margin = 1
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60

clock = pygame.time.Clock()

window = (495, 610)
screen = pygame.display.set_mode(window)

PacManLeft = pygame.transform.scale(pygame.image.load("PacManLeft.png"), (width - 2, height - 2))
PacManLeftRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 13, (window[1] // 2) + 16))
PacManRight = pygame.transform.scale(pygame.image.load("PacManRight.png"), (width - 2, height - 2))
PacManRightRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 13, (window[1] // 2) + 16))
PacManUp = pygame.transform.scale(pygame.image.load("PacManUp.png"), (width - 2, height - 2))
PacManUpRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 13, (window[1] // 2) + 16))
PacManDown = pygame.transform.scale(pygame.image.load("PacManDown.png"), (width - 2, height - 2))
PacManDownRect = PacManLeft.get_rect(topleft = ((window[0] // 2) - 13, (window[1] // 2) + 16))
background = pygame.transform.scale(pygame.image.load('Background.png'), window)

current_image = PacManLeft
current_rect_image = PacManLeftRect

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

walls = {}
walls_list = []
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if matrix[row][column] == 1:
            color = WHITE
        if matrix[row][column] == 0:
            color = BLACK
        if color == WHITE:
            walls_list.append(pygame.draw.rect(screen, color, 
                             [(margin + width) * column + margin, 
                              (margin + height) * row + margin,
                              width, height]))
            
if color not in walls and color == WHITE:
    walls[color] = walls_list

def WallDetection(x, y, current_image, current_rect_image):
    current_rect_image.right += x
    print(current_rect_image.right)
    for key, value in walls.items():
        for v in value:
            if current_rect_image.colliderect(v):
                if x < 0: 
                    print('left')
                    current_rect_image.left = v.right
                elif x > 0:
                    print('right')
                    current_rect_image.right = v.left
                break
    
    current_rect_image.top += y
    for key, value in walls.items():
        for v in value:
            if current_rect_image.colliderect(v):
                if y < 0:
                    current_rect_image.top = v.bottom
                elif y > 0:
                    current_rect_image.bottom = v.top
                break
            
    current_image = current_image
            
def Teleport(current_image_rect):
    if current_image_rect.right > window[0] + 20:
        current_image_rect.right = 0
    if current_image_rect.right < 0:
        current_image_rect.right = window[0] + 20
                
run = True
while True:
    clock.tick(10000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        screen.blit(background, (0, 0))
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            current_image = PacManLeft
            WallDetection(-5, 0, PacManLeft, PacManLeftRect)
            Teleport(PacManLeftRect)
        if key[pygame.K_RIGHT]:
            current_image = PacManRight
            WallDetection(5, 0, PacManRight, PacManRightRect)
            Teleport(PacManRightRect)  
        if key[pygame.K_UP]:
            current_image = PacManUp
            WallDetection(0, -5, PacManUpRect)
        if key[pygame.K_DOWN]:
            current_image = PacManDown
            WallDetection(0, 5, PacManDownRect)

    screen.blit(current_image, current_rect_image)
    pygame.display.update()
pygame.quit()