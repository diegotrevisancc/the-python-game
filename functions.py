import random
import os
import time
import sys
import pygame


def spawn_circle(circle_x, circle_y,game_display, width, height, head_x, head_y, score_counter, snake_size, score_sound):
    circle_radius = 30
    if ((circle_x+circle_radius) > head_x+snake_size > (circle_x - circle_radius)) and ((circle_y+circle_radius) > head_y+snake_size > (circle_y - circle_radius)):
        circle_x = random.randrange(70, width - 70)
        circle_y = random.randrange(70, height - 70)
        score_counter += 1
        # score_sound.set_volume(1)
        pygame.mixer.Sound.play(score_sound)
    circle_color = (0, 200, 0)
    pygame.draw.circle(game_display, circle_color ,(circle_x, circle_y), circle_radius)
    return [circle_x, circle_y, score_counter]

def draw_snake(snake_body, color, game_display, snake_size):
    for item in snake_body:
        pygame.draw.rect(game_display, color, [item[0], item[1], snake_size, snake_size])

def game_over(game_display, red, black):
    font = pygame.font.SysFont('system', 90)
    game_display.fill(black)
    game_over_text = font.render('YOU DIED', True, red)
    game_display.blit(game_over_text, (150, 100))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def show_score(game_display, green, score_counter):
    font = pygame.font.SysFont('system', 35)
    text_display = font.render('Score: ' + str(score_counter),True,green)
    game_display.blit(text_display, (20,25))
    pygame.display.update()

def save_match(name, email):
    os.system("cls")
    file = open("historico.txt", "r")
    last_match = file.readlines()
    file.close()
    file = open("historico.txt", "w")
    for item in last_match:
        file.write(item)
    file.write(name + "\n")
    file.write(email + "\n")
    file.close()