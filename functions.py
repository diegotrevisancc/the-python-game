import random
import pygame
import time

def spawn_circle(circle_x, circle_y,game_display, width, height, head_x, head_y, score_counter, snake_size):
    circle_radius = 30
    if ((circle_x+circle_radius) > head_x+snake_size > (circle_x - circle_radius)) and ((circle_y+circle_radius) > head_y+snake_size > (circle_y - circle_radius)):
        circle_x = random.randrange(70, width - 70)
        circle_y = random.randrange(70, height - 70)
        score_counter += 1
    circle_color = (0, 0, 0)
    pygame.draw.circle(game_display, circle_color ,(circle_x, circle_y), circle_radius)
    return [circle_x, circle_y, score_counter]

def draw_snake(snake_body, color, game_display, snake_size):
    for item in snake_body:
        pygame.draw.rect(game_display, color, [item[0], item[1], snake_size, snake_size])
