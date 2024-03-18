import pygame
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
BALL_SIZE = BALL_RADIUS * 2
BALL_SPEED = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    
    pygame.display.flip()

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= BALL_SPEED
            elif event.key == pygame.K_DOWN:
                ball_y += BALL_SPEED
            elif event.key == pygame.K_LEFT:
                ball_x -= BALL_SPEED
            elif event.key == pygame.K_RIGHT:
                ball_x += BALL_SPEED

   
    ball_x = max(BALL_RADIUS, min(ball_x, SCREEN_WIDTH - BALL_RADIUS))
    ball_y = max(BALL_RADIUS, min(ball_y, SCREEN_HEIGHT - BALL_RADIUS))

  
    clock.tick(30)