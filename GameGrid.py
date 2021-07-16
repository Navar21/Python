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
VELOCITY = 5
FPS = 60

clock = pygame.time.Clock()

window = (495, 610)
screen = pygame.display.set_mode(window)

#19x20
matrix = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
          [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
          [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
          [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
          [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
          [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
          [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
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

PacManLeft = pygame.transform.scale(pygame.image.load("PacManLeft.png"), (width, height))
PacManLeftRect = PacManLeft.get_rect(topright = (260, 319))
#background = pygame.transform.scale(pygame.image.load('Background.png'), window)

current_image = PacManLeft
current_rect_image = PacManLeftRect

run = True
while True:
    clock.tick(10000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos() 
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Set that location to one
            matrix[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

        screen.fill(BLACK)
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                color = BLACK
                if matrix[row][column] == 1:
                    color = WHITE
                wall = pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])  
    
                        
        screen.blit(current_image, current_rect_image)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
            if PacManLeftRect.colliderect(wall) == False:
                print(PacManLeftRect)
                print(wall)
                print()
                current_image = PacManLeft
                current_rect_image.right -= VELOCITY 
            else:
                current_image = PacManLeft
                current_rect_image.right += VELOCITY // 2
        if key[pygame.K_RIGHT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
            if PacManLeftRect.colliderect(wall) == False:
                print(PacManLeftRect)
                print(wall)
                print()
                current_image = PacManLeft
                current_rect_image.right += VELOCITY
            else:
                current_image = PacManLeft
                current_rect_image.right -= VELOCITY // 1.0
                current_rect_image = current_rect_image.right
                print(current_rect_image)
        if key[pygame.K_UP] and not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            if PacManLeftRect.colliderect(wall) == False:
                print(PacManLeftRect)
                print(wall)
                print()
                current_image = PacManLeft
                current_rect_image.top -= VELOCITY
            else:
                current_image = PacManLeft
                current_rect_image.right += VELOCITY // 3
        if key[pygame.K_DOWN] and not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            if PacManLeftRect.colliderect(wall) == False:
                print(PacManLeftRect)
                print(wall)
                print()
                current_image = PacManLeft
                current_rect_image.top += VELOCITY
            else:
                current_image = PacManLeft
                current_rect_image.right -= VELOCITY // 3
    
    pygame.display.update()
pygame.quit()