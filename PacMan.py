# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:43:07 2021

@author: mrbar
"""
import pygame

pygame.init()

dd = pygame.time.Clock()

SCREEN_WIDTH = 530
SCREEN_HEIGHT = 650
X = SCREEN_WIDTH // 2
Y = SCREEN_HEIGHT // 2
VELOCITY = 0.2

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PacManLeft = pygame.transform.scale(pygame.image.load("PacManLeft.png"), (30, 30))
PacManLeftRect = PacManLeft.get_rect(topleft = (X - 15, Y + 16))
PacManRight = pygame.transform.scale(pygame.image.load("PacManRight.png"), (30, 30))
PacManUp = pygame.transform.scale(pygame.image.load("PacManUp.png"), (30, 30))
PacManDown = pygame.transform.scale(pygame.image.load("PacManDown.png"), (30, 30))
background = pygame.transform.scale(pygame.image.load('Background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pac-Man')
pygame.mouse.set_visible(False)
    
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
    dd.tick(80)
    window.blit(background, (0, 0)) 
    window.blit(PacManLeft, PacManLeftRect)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_DOWN] and X > 15:
        PacManLeftRect.x -= VELOCITY
    if key[pygame.K_RIGHT] and not key[pygame.K_UP] and not key [pygame.K_DOWN] and X < SCREEN_WIDTH - 15:
        X += VELOCITY
    if key[pygame.K_UP] and Y > 17:
        Y -= VELOCITY
    if key[pygame.K_DOWN] and Y < SCREEN_HEIGHT - 75:
        Y += VELOCITY
    
    pygame.display.update()
pygame.quit()