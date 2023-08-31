import pygame
import sys
from player import Fighter

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Letter Fighting")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# Define Color
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# define fighter variable
CAT_SIZE = 40
CAT_SCALE = 5
CAT_OFFSET = [17, 15]
CAT_DATA = [CAT_SIZE, CAT_SCALE, CAT_OFFSET]
GIRLGUN_SIZE = 50
GIRLGUN_SCALE = 5
GIRLGUN_OFFSET = [20, 17]
GIRLGUN_DATA = [GIRLGUN_SIZE, GIRLGUN_SCALE, GIRLGUN_OFFSET]

# Uploading the background image
background_image = pygame.image.load("assets/backgrounds/university_background.jpg").convert_alpha()

# loading the character
cat_sheet = pygame.image.load("assets/characters/cat.png").convert_alpha()
girlgun_sheet = pygame.image.load("assets/characters/girlgun_bg.png").convert_alpha()

# Define number of steps in each animation
CAT_ANIMATION_STEPS = [10, 10, 10, 10, 10, 10]
GIRLGUN_ANIMATION_STEPS = [5, 5, 8, 8, 5, 5, 8, 8]

# Uploading the player

player1 = Fighter(100, 550, False, CAT_DATA, cat_sheet, CAT_ANIMATION_STEPS)
player2 = Fighter(800, 550, False, GIRLGUN_DATA, girlgun_sheet, GIRLGUN_ANIMATION_STEPS)


def draw_bg():
    scaled_bg = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Drawing Health bar


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 405, 35))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# Main game loop



running = True


while running:
    clock.tick(FPS)

    draw_bg()

    # show the player's health
    draw_health_bar(player1.health, 20, 20)
    draw_health_bar(player2.health, 580, 20)

    # move player
    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2)
    # player2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player1)

    # update animation
    player1.update_animation()
    player2.update_animation()

    # draw player
    player1.draw(screen)
    player2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw game elements here

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
