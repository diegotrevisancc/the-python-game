import os
import pygame
import time

pygame.init()
display_width = 800
display_height = 600
game_display = pygame.display.set_mode(display_width, display_height)
clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




            
    pygame.display.update()
    clock.tick(60)