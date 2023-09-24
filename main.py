import pygame
import sys
from pygame import mixer
from player import Fighter
import button

# Initialize Pygame and Mixer for audio
pygame.init()
mixer.init()

# Set up the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cat Fighting")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# Define Color
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player's score. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

# define fighter variable
CAT_SIZE = 64
CAT_SCALE = 5
CAT_OFFSET = [17, 15]
CAT_DATA = [CAT_SIZE, CAT_SCALE, CAT_OFFSET]
DOG_SIZE = 64
DOG_SCALE = 5
DOG_OFFSET = [20, 15]
DOG_DATA = [DOG_SIZE, DOG_SCALE, DOG_OFFSET]

# load music and sounds
pygame.mixer.music.load("assets/sounds/music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0, 5000)
punch = pygame.mixer.Sound("assets/sounds/punch.mp3")
punch.set_volume(0.5)
jump = pygame.mixer.Sound("assets/sounds/jump.mp3")
jump.set_volume(0.3)

# Uploading the background image
background_image = pygame.image.load("assets/backgrounds/university_background.jpg").convert_alpha()
paused_image = pygame.image.load("assets/backgrounds/unideb.jpg").convert_alpha()

# loading the character
cat_sheet = pygame.image.load("assets/characters/cat_animation.png").convert_alpha()
dog_sheet = pygame.image.load("assets/characters/dog_0.png").convert_alpha()

# Define number of steps in each animation
CAT_ANIMATION_STEPS = [4, 8, 8, 10, 9, 7, 6, 8, 13, 10, 12, 6, 8, 8, 8, 6]
DOG_ANIMATION_STEPS = [4, 8, 8, 10, 9, 7, 6, 8, 13, 10, 12, 6, 8, 8, 8, 6]

# Uploading the player

player1 = Fighter(1, 100, 550, False, CAT_DATA, cat_sheet, CAT_ANIMATION_STEPS, punch, jump)
player2 = Fighter(2, 800, 550, True, DOG_DATA, dog_sheet, DOG_ANIMATION_STEPS, punch, jump)

# Loading the font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 200)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)
paused_font = pygame.font.Font("assets/fonts/turok.ttf", 40)

# Load button images
newgame_img = pygame.image.load("assets/buttons/button_newgame.jpg")
resume_img = pygame.image.load("assets/buttons/button_resume.png")
quit_img = pygame.image.load("assets/buttons/button_quit.png")

# create button instances
newgame_button = button.Button(304, 250, newgame_img, 0.5)
resume_button = button.Button(400, 360, resume_img, 1)
quit_button = button.Button(430, 460, quit_img, 1)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

# Game Pause controller


game_paused = False
game_start = False
show_menu_buttons = True


def draw_bg():
    scaled_bg = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def draw_paused():
    scale_bg = pygame.transform.scale(paused_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))

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

    if show_menu_buttons:
        draw_paused()
        # resume_button.draw(screen)
        newgame_button.draw(screen)
        quit_button.draw(screen)

    if game_paused:
        draw_paused()
        resume_button.draw(screen)
        if show_menu_buttons:
            newgame_button.draw(screen)
        quit_button.draw(screen)

    if game_start:
        show_menu_buttons = False
        draw_health_bar(player1.health, 20, 20)
        draw_health_bar(player2.health, 580, 20)
        draw_text("CAT1: " + str(score[0]), score_font, RED, 20, 60)
        draw_text("CAT2: " + str(score[1]), score_font, RED, 580, 60)

        # update countdown
        if intro_count <= 0:
            # move player
            player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2, round_over)
            player2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player1, round_over)
        else:
            # display count timer
            draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 3)
            # update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()
                print(intro_count)

        # update animation
        player1.update_animation()
        player2.update_animation()

        # draw player
        player1.draw(screen)
        player2.draw(screen)

        # check for player defeat

        if round_over == False:
            if player1.alive == False:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif player2.alive == False:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            draw_text("Victory!!", count_font, RED, SCREEN_WIDTH / 2 - 350, SCREEN_HEIGHT / 3)
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                intro_count = 3
                player1 = Fighter(1, 100, 550, False, CAT_DATA, cat_sheet, CAT_ANIMATION_STEPS, punch)
                player2 = Fighter(2, 800, 550, True, DOG_DATA, dog_sheet, DOG_ANIMATION_STEPS, punch)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                game_start = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if newgame_button.rect.collidepoint(event.pos):
                game_start = True
            if resume_button.rect.collidepoint(event.pos):
                game_paused = False
                game_start = True
            if quit_button.rect.collidepoint(event.pos):
                running = False
        if event.type == pygame.QUIT:
            running = False

    # Draw game elements here

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
