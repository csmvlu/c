import pygame, random
pygame.init()
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = pygame.Rect(200, 250, 20, 20)
bullets, enemies = [], []
bullet_speed, enemy_speed, speed = 7, 3, 5
space_pressed = False

def move_bullets():
    for b in bullets:
        b.y -= bullet_speed
        if b.y < 0: bullets.remove(b)

def move_enemies():
    for e in enemies:
        e.y += enemy_speed
        if e.y > 300: enemies.remove(e)

def draw_game():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for b in bullets: pygame.draw.rect(screen, (255, 255, 0), b)
    for e in enemies: pygame.draw.rect(screen, (255, 0, 0), e)
    pygame.display.flip()

def check_collision():
    for e in enemies:
        if player.colliderect(e): return True
        for b in bullets:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                break
    return False

done = False
while not done:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed

    if keys[pygame.K_SPACE] and not space_pressed:
        bullets.append(pygame.Rect(player.x + 8, player.y, 4, 10))
        space_pressed = True
    if not keys[pygame.K_SPACE]:
        space_pressed = False

    if random.randint(1, 50) == 1:
        enemies.append(pygame.Rect(random.randint(0, 380), 0, 20, 20))

    move_bullets()
    move_enemies()
    if check_collision(): done = True

    draw_game()

pygame.quit()
#
#
#
#
#

"""
#What is pygame
'''Pygame is a Python library designed for creating 2D games and
multimedia applications.
It provides functionalities for handling graphics, sounds, and user inputs in an
easy-to-use framework.'''

#Configuration
'''To install Pygame, use the following command in your terminal or command prompt:
pip install pygame
Explanation of Basic Functions:
pygame.init():

Initializes all imported Pygame modules. This is required before using Pygame’s functionalities like rendering graphics, handling input, etc.
pygame.display.set_mode():

Sets up the game window's width and height, returning a Surface object that represents the screen.
pygame.display.set_caption():

Sets the title of the game window.
pygame.event.get():

Gets a list of all events (keyboard, mouse, window events, etc.) that have happened since the last loop iteration.
pygame.QUIT:

This event is triggered when the player clicks the close button on the game window.
screen.fill():

Fills the screen with a solid color. (0, 0, 0) represents black in RGB color values.
pygame.display.flip():

Updates the contents of the entire display to the screen. This is necessary to reflect any drawing or updates.
pygame.time.Clock():

Manages the frame rate (FPS). By calling clock.tick(60), you ensure the game runs at 60 frames per second.
pygame.quit():

Uninitializes all Pygame modules. This is necessary to clean up resources when exiting the game.
sys.exit():

Ensures the program exits cleanly after quitting Pygame.
This setup is the foundation for building more complex games using Pygame
"""
#
#
#
#
#

"""
#if requirement is Score and game over panel

import pygame, random

pygame.init()
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Font
font = pygame.font.SysFont(None, 35)

# Player, bullet, and enemy variables
player = pygame.Rect(200, 250, 20, 20)
bullets, enemies = [], []
bullet_speed, enemy_speed, speed = 7, 3, 5
space_pressed = False
score = 0
game_over = False

# Functions to handle game logic
def move_bullets():
    for b in bullets:
        b.y -= bullet_speed
        if b.y < 0: bullets.remove(b)

def move_enemies():
    for e in enemies:
        e.y += enemy_speed
        if e.y > 300: enemies.remove(e)

def draw_game():
    screen.fill(black)
    pygame.draw.rect(screen, green, player)
    for b in bullets: pygame.draw.rect(screen, yellow, b)
    for e in enemies: pygame.draw.rect(screen, red, e)
    show_score()
    pygame.display.flip()

def check_collision():
    global score
    for e in enemies:
        if player.colliderect(e): return True
        for b in bullets:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                score += 1
                break
    return False

def show_score():
    score_text = font.render("Score: " + str(score), True, yellow)
    screen.blit(score_text, [10, 10])

def game_over_screen():
    screen.fill(black)
    game_over_text = font.render("Game Over! Score: " + str(score), True, red)
    screen.blit(game_over_text, [100, 100])
    restart_text = font.render("Press R to Restart or Q to Quit", True, red)
    screen.blit(restart_text, [50, 150])
    pygame.display.flip()

# Main game loop
while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed

    if keys[pygame.K_SPACE] and not space_pressed:
        bullets.append(pygame.Rect(player.x + 8, player.y, 4, 10))
        space_pressed = True
    if not keys[pygame.K_SPACE]:
        space_pressed = False

    if random.randint(1, 50) == 1:
        enemies.append(pygame.Rect(random.randint(0, 380), 0, 20, 20))

    move_bullets()
    move_enemies()
    
    if check_collision():
        game_over = True
    
    draw_game()

# Game over loop
done = False
while not done:
    game_over_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        # Restart the game
        player = pygame.Rect(200, 250, 20, 20)
        bullets, enemies = [], []
        score = 0
        game_over = False
        while not game_over:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: player.x -= speed
            if keys[pygame.K_RIGHT]: player.x += speed

            if keys[pygame.K_SPACE] and not space_pressed:
                bullets.append(pygame.Rect(player.x + 8, player.y, 4, 10))
                space_pressed = True
            if not keys[pygame.K_SPACE]:
                space_pressed = False

            if random.randint(1, 50) == 1:
                enemies.append(pygame.Rect(random.randint(0, 380), 0, 20, 20))

            move_bullets()
            move_enemies()
            
            if check_collision():
                game_over = True
            
            draw_game()
    if keys[pygame.K_q]:
        done = True

pygame.quit()
"""
