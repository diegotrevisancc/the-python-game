from functions import spawn_circle
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
head_movementx = 0
head_movementy = 0
white = (255, 255, 255)
speed = 10
circle_x = 255
circle_y = 255
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head_movementx += speed * -1
                head_movementy = 0
            elif event.key == pygame.K_RIGHT:
                head_movementx += speed 
                head_movementy = 0 #matar a diagonal
            elif event.key == pygame.K_UP:
                head_movementy += speed * -1
                head_movementx = 0
            elif event.key == pygame.K_DOWN:
                head_movementy += speed
                head_movementx = 0
        elif event.type == pygame.KEYUP:
            head_movementx = 0
            head_movementy = 0

    head_positionx += head_movementx
    head_positiony += head_movementy

    if head_positiony == display_height or head_positiony == 0:
        head_positiony = 300
        #perdeu
    elif head_positionx == display_width or head_positionx == 0:
        head_positionx = 400
        #perdeu


    game_display.blit(background_image, (0, 0))
    head_snake = pygame.draw.rect(game_display, white,(head_positionx, head_positiony, 30, 30))
    head_snake = []
    circle = spawn_circle(circle_x, circle_y, game_display, display_width, display_height, head_positionx, head_positiony)
    circle_x = circle[0]
    circle_y = circle[1]





    pygame.display.update()
    clock.tick(60)