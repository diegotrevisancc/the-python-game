import os
import pygame
import time

pygame.init()
pygame.display.set_caption("The Python Game")
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
background_image = pygame.image.load("assets/background-image.png")
head_positionx = 400
head_positiony = 300
white = (255, 255, 255)
speed = 10
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head_positionx += speed * -1
            elif event.key == pygame.K_RIGHT:
                head_positionx += speed 
            elif event.key == pygame.K_UP:
                head_positiony += speed * -1
            elif event.key == pygame.K_DOWN:
                head_positiony += speed
            elif event.type == pygame.KEYUP:
                head_positionx = 0
                head_positiony = 0


    game_display.blit(background_image, (0, 0))
    head_snake = pygame.draw.rect(game_display, white,(head_positionx, head_positiony, 30, 30))
    



    pygame.display.update()
    clock.tick(60)