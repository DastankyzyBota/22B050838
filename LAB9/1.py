import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CAR_WIDTH, CAR_HEIGHT = 50, 100
COIN_SIZE = 20
FPS = 60
CAR_SPEED = 5

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Racer")

clock = pygame.time.Clock()

# Player car class
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -CAR_SPEED
        if keys[pygame.K_RIGHT]:
            self.speedx = CAR_SPEED
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((COIN_SIZE, COIN_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speedy = random.randrange(1, 5)

# Sprite groups
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player car
player_car = Car()
all_sprites.add(player_car)

# Function to create coins
def create_coins():
    for _ in range(10):
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

# Create enemy cars
def create_enemies():
    for _ in range(8):
        enemy = EnemyCar()
        all_sprites.add(enemy)
        enemies.add(enemy)

# Enemy car class
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speedy = random.randrange(1, 5)

# Function to draw text on screen
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Game loop
running = True
score = 0
create_enemies()
create_coins()
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player_car, enemies, False)
    if hits:
        running = False

    # Check for coin collection
    coin_hits = pygame.sprite.spritecollide(player_car, coins, True)
    for coin in coin_hits:
        score += 1

    # Render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_text(screen, "Score: " + str(score), 24, BLACK, WIDTH - 100, 10)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()

#3
import turtle


t = turtle.Turtle()


def draw_square():
    for _ in range(4):
        t.forward(100)  
        t.right(90)     


def draw_right_triangle():
    for _ in range(3):
        t.forward(100)  
        t.right(120)    


def draw_equilateral_triangle():
    for _ in range(3):
        t.forward(100) 
        t.left(120)     


def draw_rhombus():
    for _ in range(2):
        t.forward(100)  
        t.right(60)     
        t.forward(100)  
        t.right(120)    


turtle.setup(width=600, height=600)
t.speed(1)  

draw_square()
t.penup()        
t.goto(-150, 0)  
t.pendown()
draw_right_triangle()
t.penup()
t.goto(-150, -150)
t.pendown()

draw_equilateral_triangle()
t.penup()
t.goto(0, -150)
t.pendown()

draw_rhombus()


turtle.done()