import random
import pygame
import time
def spawn_circle(circle_x, circle_y,game_display, width, height, head_x, head_y):
    if ((circle_x+30) > head_x > (circle_x - 30)) and ((circle_y+30) > head_y > (circle_y - 30)):
        circle_x = random.randrange(width)
        circle_y = random.randrange(height) 
    circle_color = (0, 255, 0)
    pygame.draw.circle(game_display, circle_color ,(circle_x, circle_y), 30)
    return [circle_x, circle_y]
