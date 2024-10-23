import pygame, time, random
pygame.init()
white, black, red, green = (255, 255, 255), (0, 0, 0), (213, 50, 80), (0, 255, 0)
width, height = 600, 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
snake_block, snake_speed = 10, 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over, game_close = False, False
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0
    snake_List, length_of_snake = [], 1
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: game_over, game_close = True, False
                    if event.key == pygame.K_c: gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT: x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP: y1_change, x1_change = -snake_block, 0
                elif event.key == pygame.K_DOWN: y1_change, x1_change = snake_block, 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0: game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake: del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head: game_close = True
        for segment in snake_List:
            pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()



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
This setup is the foundation for building more complex games using Pygame.'''


#WARNING (this is same code as above use this on your own risk)
#This code is for the one *jiske gand me chull hai or hero banna hai*.

'''
import pygame, time, random
pygame.init()

# Define colors
white, black, red, green = (255, 255, 255), (0, 0, 0), (213, 50, 80), (0, 255, 0)

# Set display width and height
width, height = 600, 400
dis = pygame.display.set_mode((width, height))

# Set game title
pygame.display.set_caption('Snake Game')

# Snake properties
snake_block, snake_speed = 10, 15

# Set clock and fonts
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def show_score(score):
    value = score_font.render(f"Your Score: {score}", True, white)
    dis.blit(value, [0, 0])

# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over, game_close = False, False
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0
    snake_List, length_of_snake = [], 1
    score = 0  # Initialize score

    # Randomly place the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            show_score(score)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: game_over, game_close = True, False
                    if event.key == pygame.K_c: gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT: x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP: y1_change, x1_change = -snake_block, 0
                elif event.key == pygame.K_DOWN: y1_change, x1_change = snake_block, 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0: game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Draw the food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Update the snake
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        # Check for collisions with the body
        for x in snake_List[:-1]:
            if x == snake_Head: game_close = True

        # Draw the snake
        for segment in snake_List:
            pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])

        # Display score
        show_score(score)
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 10  # Increase score

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
'''


