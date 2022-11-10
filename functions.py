import random
import pygame
import time
def spawn_circle(circle_x, circle_y,game_display, width, height, head_x, head_y, score_counter):
    circle_radius = 60
    if ((circle_x+circle_radius) > head_x > (circle_x - circle_radius)) and ((circle_y+circle_radius) > head_y > (circle_y - circle_radius)):
        circle_x = random.randrange(width)
        circle_y = random.randrange(height)
        score_counter += 1
    circle_color = (0, 255, 0)
    pygame.draw.circle(game_display, circle_color ,(circle_x, circle_y), circle_radius)
    return [circle_x, circle_y, score_counter]

def draw_snake(snake_body, white, game_display, snake_size):
    for item in snake_body:
        pygame.draw.rect(game_display, white, [item[0], item[1], snake_size, snake_size])