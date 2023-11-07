import pygame
#import sys
import random


class Board:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, monster):
        self.screen.fill((0, 0, 0))
        self.screen.blit(monster.image, (monster.rect.x, monster.rect.y))
        pygame.display.update()

#class board:
#    def __init__(self, root):
#        self.root = root
#        root.title("DnD Spillebane")
        
        # Initialize Pygame
#        pygame.init()

        # Screen dimensions
#        screen_width = 1600
#        screen_height = 1000

        # Create the screen
#        screen = pygame.display.set_mode((screen_width, screen_height))
#        pygame.display.set_caption("Monster Moving")

        # Load the original image
#        original_image = pygame.image.load("monster.png")

        # Define the desired width and height for the resized image
#        desired_width = 85
#        desired_height = 55

# Resize the image
#resized_image = pygame.transform.scale(original_image, (desired_width, desired_height))
#pygame.image.save(resized_image, "monster3.png")

# Load the monster image
#monster_image = pygame.image.load("monster3.png")
#monster_rect = monster_image.get_rect()

# Monster starting position
#monster_x = random.randint(0, screen_width - monster_rect.width)
#monster_y = random.randint(0, screen_height - monster_rect.height)

# Set the maximum number of steps for each direction
#max_steps = 1  # Adjust this value as needed

# Initialize step counters
#left_steps = 0
#right_steps = 0
#up_steps = 0
#down_steps = 0

# Create a clock to control the frame rate
#clock = pygame.time.Clock()

# Main game loop
#while True:
 #   for event in pygame.event.get():
 #       if event.type == pygame.QUIT:
 #           pygame.quit()
 #           sys.exit()

    # Randomly select a direction
 #   direction = random.choice(['left', 'right', 'up', 'down'])

    # Update the monster's position based on the selected direction and step count
 #   if direction == 'left' and left_steps < max_steps:
 #       monster_x -= 85  # Move left
 #       left_steps += 1
 #   elif direction == 'right' and right_steps < max_steps:
 #       monster_x += 85  # Move right
 #       right_steps += 1
 #   elif direction == 'up' and up_steps < max_steps:
 #       monster_y -= 85  # Move up
 #       up_steps += 1
 #   elif direction == 'down' and down_steps < max_steps:
 #       monster_y += 85  # Move down
 #       down_steps += 1

    # Reset step counters when the maximum number of steps is reached
 #   if left_steps == max_steps:
 #       left_steps = 0
 #   if right_steps == max_steps:
 #       right_steps = 0
 #   if up_steps == max_steps:
 #       up_steps = 0
 #   if down_steps == max_steps:
 #       down_steps = 0

    # Ensure the monster stays within the screen boundaries
 #   monster_x = max(0, min(screen_width - monster_rect.width, monster_x))
 #   monster_y = max(0, min(screen_height - monster_rect.height, monster_y))

    #screen.fill(white)
 #       screen.fill((0, 0, 0))
 #       screen.blit(monster_image, (monster_x, monster_y))
 #       pygame.display.update()

    #clock.tick(2)  # Limit the frame rate per second
