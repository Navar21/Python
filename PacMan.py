# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:43:07 2021

@author: mrbar
"""
import pygame

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 530
SCREEN_HEIGHT = 650
X = SCREEN_WIDTH // 2
Y = SCREEN_HEIGHT // 2
VELOCITY = 1

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PacManLeft = pygame.transform.scale(pygame.image.load("PacManLeft.png"), (30, 30))
PacManLeftRect = PacManLeft.get_rect(topleft = (X - 15, Y + 16))
PacManRight = pygame.transform.scale(pygame.image.load("PacManRight.png"), (30, 30))
PacManRightRect = PacManRight.get_rect(topleft = (X - 15, Y + 16))
PacManUp = pygame.transform.scale(pygame.image.load("PacManUp.png"), (30, 30))
PacManUpRect = PacManUp.get_rect(topleft = (X - 15, Y + 16))
PacManDown = pygame.transform.scale(pygame.image.load("PacManDown.png"), (30, 30))
PacManDownRect = PacManDown.get_rect(topleft = (X - 15, Y + 16))
background = pygame.transform.scale(pygame.image.load('Background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

index = 0
image = [PacManLeft, PacManRight, PacManUp, PacManDown]
rect_image = [PacManLeftRect, PacManRightRect, PacManUpRect, PacManDownRect]
current_image = image[index]
current_rect_image = rect_image[index]

pygame.display.set_caption('Pac-Man')
pygame.mouse.set_visible(False)
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
        
        clock.tick(100)
        window.blit(background, (0, 0)) 
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            current_image = image[0]
            current_rect_image = rect_image[0]
            PacManLeftRect.top = PacManRightRect.top
            PacManLeftRect.right -= 1
            print(PacManLeftRect.right)
        if key[pygame.K_RIGHT]:
            current_image = image[0]
            current_rect_image = rect_image[0]
            PacManRightRect.top = PacManLeftRect.top
            PacManRightRect.right = PacManLeftRect.right
            PacManRightRect.right += 1
            print(PacManRightRect.right)
        if key[pygame.K_UP]:
            current_image = image[0]
            current_rect_image = rect_image[0]
            PacManUpRect.top -= VELOCITY
        if key[pygame.K_DOWN]:
            current_image = image[0]
            current_rect_image = rect_image[0]
            PacManDownRect.top += VELOCITY
    
        window.blit(current_image, current_rect_image)
    pygame.display.update()
pygame.quit()