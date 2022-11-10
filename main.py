from functions import spawn_circle, draw_snake
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
score_counter = 1
snake_body = []
snake_size = 30
while True: 
    old_movement_x = head_movementx
    olld_movement_y = head_movementy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head_movementx = speed * -1
                head_movementy = 0
                #if event.key == pygame.K_RIGHT:
                    #head_movementx = 0
                    #head_movementy += speed
                    #head_movementx = 0
            elif event.key == pygame.K_RIGHT:
                head_movementx = speed 
                head_movementy = 0 #matar a diagonal
                #if event.key == pygame.K_LEFT:
                    #head_movementx = 0
                    #head_movementy += speed
                    #head_movementx = 0
            elif event.key == pygame.K_UP:
                head_movementy = speed * -1
                head_movementx = 0
            elif event.key == pygame.K_DOWN:
                head_movementy = speed
                head_movementx = 0

    head_positionx += head_movementx
    head_positiony += head_movementy

    if head_positiony > display_height or head_positiony < 0:
        head_positiony = 300
        #perdeu
    elif head_positionx > display_width or head_positionx < 0:
        head_positionx = 400
        #perdeu


    game_display.blit(background_image, (0, 0))
    head_snake = []
    head_snake.append(head_positionx)
    head_snake.append(head_positiony)
    snake_body.append(head_snake)

    if len(snake_body) > score_counter:
        del snake_body[0]
    
    for item in snake_body[:-1]:
        if item == head_snake:
            print("Perdeu")

    draw_snake(snake_body, white, game_display, snake_size)
    
    circle = spawn_circle(circle_x, circle_y, game_display, display_width, display_height, head_positionx, head_positiony, score_counter)
    circle_x = circle[0]
    circle_y = circle[1]
    score_counter = circle[2]





    pygame.display.update()
    clock.tick(60)