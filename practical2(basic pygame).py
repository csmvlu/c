import pygame  # Import the Pygame library for game development
from math import pi  # Import pi from the math library for arc calculations

pygame.init()  # Initialize all Pygame modules

# Set the size of the game window
size = [400, 300]
screen = pygame.display.set_mode(size)  # Create the display surface (the game window)

# Set the window title
pygame.display.set_caption("Geometry Drawing")

done = False  # A flag to indicate whether the game loop should continue running
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

# Main game loop
while not done:
    clock.tick(10)  # Limit the frame rate to 10 frames per second
    
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user clicked the window close button
            done = True  # If so, set 'done' to True to exit the game loop

    screen.fill((0, 0, 0))  # Fill the screen with a black color (background)

    # Draw a green line with thickness 5 from coordinates (0, 0) to (50, 30)
    pygame.draw.line(screen, (0, 255, 0), [0, 0], [50, 30], 5)

    # Draw connected lines (no fill) forming a polyline with thickness 5
    pygame.draw.lines(screen, (0, 0, 0), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

    # Draw a black rectangle with thickness 2 (hollow rectangle)
    pygame.draw.rect(screen, (0, 0, 0), [75, 10, 50, 20], 2)

    # Draw a filled black rectangle
    pygame.draw.rect(screen, (0, 0, 0), [150, 10, 50, 20])

    # Draw a red hollow ellipse with thickness 2
    pygame.draw.ellipse(screen, (255, 0, 0), [225, 10, 50, 20], 2)

    # Draw a filled red ellipse
    pygame.draw.ellipse(screen, (255, 0, 0), [300, 10, 50, 20])

    # Draw a black triangle with thickness 5 by connecting the given points
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 100], [0, 200], [200, 200]], 5)

    # Draw a filled blue circle with radius 40 at position (60, 250)
    pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)

    # Draw an arc (a portion of a circle) with a start angle of 0 and end angle of pi/2 radians
    pygame.draw.arc(screen, (0, 0, 0), [210, 75, 150, 125], 0, pi / 2, 2)

    pygame.display.flip()  # Update the full display to show the new drawings

pygame.quit()  # Quit Pygame and close the window




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