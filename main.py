from functions import spawn_circle, draw_snake, game_over, show_score, save_match
import os
import pygame
import time

name = input("Insira seu nome: ")
email = input("Insira seu email: ")
save_match(name, email)

pygame.init()
pygame.display.set_caption("The Python Game")
display_width = 600
display_height = 400
game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
background_image = pygame.image.load("assets/background-image.png")
background_image = pygame.transform.scale(background_image, (display_width, display_height))
head_positionx = 300
head_positiony = 200
head_movementx = 0
head_movementy = 0
green = (34,139,34)
black = (0, 0, 0)
red = (200, 0, 0)
speed = 6
circle_x = 255
circle_y = 255
score_counter = 1
snake_body = []
snake_size = 20
current_direction = ""
current_movement = ""
play = True
score_sound = pygame.mixer.Sound("assets/score.wav")
score_sound.set_volume(-1)
while play: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_movement = "UP"
            if event.key == pygame.K_DOWN:
                current_movement = "DOWN"
            if event.key == pygame.K_LEFT:
                current_movement = "LEFT"
            if event.key == pygame.K_RIGHT:
                current_movement = "RIGHT"

    if current_movement == "UP" and current_direction != "DOWN":
        current_direction = "UP"
    elif current_movement == "DOWN" and current_direction != "UP":
        current_direction = "DOWN"
    elif current_movement == "LEFT" and current_direction != "RIGHT":
        current_direction = "LEFT"
    elif current_movement == "RIGHT" and current_direction!= "LEFT":
        current_direction = "RIGHT"

        
    if current_direction == "UP":
        head_movementy = speed*-1
        head_movementx = 0
    elif current_direction == "DOWN":
        head_movementy = speed
        head_movementx = 0
    elif current_direction == "LEFT":
        head_movementy = 0
        head_movementx = speed*-1
    elif current_direction == "RIGHT":
        head_movementy = 0
        head_movementx = speed


    head_positionx += head_movementx
    head_positiony += head_movementy

    if head_positiony > display_height or head_positiony < 0:
        head_positiony = 200
        game_over(game_display, red, black)
    elif head_positionx > display_width or head_positionx < 0:
        head_positionx = 150
        game_over(game_display, red, black)


    game_display.blit(background_image, (0, 0))
    head_snake = []
    head_snake.append(head_positionx)
    head_snake.append(head_positiony)
    snake_body.append(head_snake)

    if len(snake_body) > score_counter:
        del snake_body[0]
    
    for item in snake_body[:-1]:
        if item == head_snake:
            game_over(game_display, red, black)

    draw_snake(snake_body, green, game_display, snake_size)
    
    
    circle = spawn_circle(circle_x, circle_y, game_display, display_width, display_height, head_positionx, head_positiony, score_counter, snake_size, score_sound)
    circle_x = circle[0]
    circle_y = circle[1]
    score_counter = circle[2]

    show_score(game_display, green, score_counter)
    pygame.display.update()
    clock.tick(60)