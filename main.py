# Draw Lines in Pygame / No Functions

# Pygame game template
import pygame
import sys
import config  # Import the config module
import random
import shapes  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    shapes_list = []   # List to hold shapes
 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 
        
        # Generate a random number to represent the various shapes
        shape_type = random.randrange(3)

        # Create a new shape and add it to the list
        if shape_type == 0:
            # Circle: (type, color, position, radius)
            new_shape = {
                'type': 'circle',
                'color': (random.randrange(225), random.randrange(225), random.randrange(225)),
                'position': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
                'radius': random.randrange(50)
            }
        elif shape_type == 1:
            # Rectangle: (type, color, position, width, height)
            new_shape = {
                'type': 'rectangle',
                'color': (random.randrange(225), random.randrange(225), random.randrange(225)),
                'position': (random.randrange(config.WINDOW_WIDTH - 100), random.randrange(config.WINDOW_HEIGHT - 100)),
                'width': random.randrange(100),
                'height': random.randrange(100)
            }
        elif shape_type == 2:
            new_shape = {
                'type': 'line',
                'color': (random.randrange(225), random.randrange(225), random.randrange(225)),
                'start_pos': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
                'end_pos': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
                'width': random.randrange(10)
            }

        # Add the new shape to the list
        shapes_list.append(new_shape)

        # Draw all shapes from the list using the appropriate fuction from the shapes module
        for shape in shapes_list:
            if shape['type'] == 'circle':
                shapes.draw_circle(screen, shape)
            elif shape['type'] == 'rectangle':
                shapes.draw_rect(screen, shape)
            elif shape['type'] == 'line':
                shapes.draw_line(screen, shape)

        font = pygame.font.SysFont("Ariel", 120)
        text = font.render("It's me Matt", True, (random.randrange(225), random.randrange(225), random.randrange(225)))
        screen.blit(text, [250, 250])
        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































