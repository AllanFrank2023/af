import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1600
screen_height = 1000

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monster Moving")

# Load the original image
original_image = pygame.image.load("monster.png")

# Define the desired width and height for the resized image
desired_width = 85
desired_height = 55

# Resize the image
resized_image = pygame.transform.scale(original_image, (desired_width, desired_height))

# Save the resized_image as a PNG image
pygame.image.save(resized_image, "monster3.png")

# Load the monster image
monster_image = pygame.image.load("monster3.png")
monster_rect = monster_image.get_rect()

# Monster starting position
monster_x = 400
monster_y = 300

# Monster speed
monster_speed = 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

     # Get a list of keys
    keys = pygame.key.get_pressed()

    # Move the monster based on the random direction
    direction = random.choice(['left', 'right', 'up', 'down'])  # Choose a random direction
    
    if direction == 'left':
        monster_x -= monster_speed
    elif direction == 'right':
        monster_x += monster_speed
    elif direction == 'up':
        monster_y -= monster_speed
    elif direction == 'down':
        monster_y += monster_speed

    # Ensure the monster stays within the screen boundaries
    monster_x = max(0, min(screen_width - monster_rect.width, monster_x))
    monster_y = max(0, min(screen_height - monster_rect.height, monster_y))

    # Redraw the screen
    screen.fill((0, 0, 0))  # Clear the screen with a black background
    screen.blit(monster_image, (monster_x, monster_y))

    # Update the display
    pygame.display.update()

