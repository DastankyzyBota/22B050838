import pygame
import sys
from time import localtime
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Часы с Микки Маусом')
clock = pygame.time.Clock()

mickey_image = pygame.image.load('mickey.png')
mickey_image = pygame.transform.scale(mickey_image, (200, 200))

def rotate_mickey(image, angle):
    return pygame.transform.rotate(image, angle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    cur_time = datetime.now().strftime('%H:%M:%S').split(':')
    hour = int(cur_time[0])
    minute = int(cur_time[1])
    sec = int(cur_time[2])

    minute_angle = minute * 6  
    sec_angle = sec * 6 

    
    minute_hand = rotate_mickey(mickey_image, minute_angle)
    sec_hand = rotate_mickey(mickey_image, sec_angle)

    screen.fill((255, 255, 255))
    screen.blit(minute_hand, (100, 100))
    screen.blit(sec_hand, (100, 100))

    pygame.display.update()
    clock.tick(1)