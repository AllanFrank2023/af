import pygame
import sys
import random

class Monster:
    def __init__(self, screen, image, max_steps=30):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, self.screen.get_height() - self.rect.height)
        self.max_steps = max_steps
        self.step_counters = {'left': 0, 'right': 0, 'up': 0, 'down': 0}

    def move(self):
        direction = random.choice(['left', 'right', 'up', 'down'])
        if self.step_counters[direction] < self.max_steps:
            if direction == 'left':
                self.rect.x -= 75
            elif direction == 'right':
                self.rect.x += 75
            elif direction == 'up':
                self.rect.y -= 75
            elif direction == 'down':
                self.rect.y += 75
            self.step_counters[direction] += 1

    def reset_step_counters(self):
        for direction in self.step_counters:
            self.step_counters[direction] = 0








#import pygame
#import sys
#import random

#class monster:
#    def __init__(self, Name, Health, Defence, Strength)

#        self.Name = Name 

#        self.Health = Health 

#        self.Defence = Defence 

#        self.strenth = Strenth 
# Load the original image
#original_image = pygame.image.load("monster.png")

# Define the desired width and height for the resized image
#desired_width = 85
#desired_height = 55

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
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
 #           sys.exit()

    # Randomly select a direction
#    direction = random.choice(['left', 'right', 'up', 'down'])

    # Update the monster's position based on the selected direction and step count
#    if direction == 'left' and left_steps < max_steps:
#        monster_x -= 85  # Move left
#        left_steps += 1
#    elif direction == 'right' and right_steps < max_steps:
#        monster_x += 85  # Move right
#        right_steps += 1
#    elif direction == 'up' and up_steps < max_steps:
#        monster_y -= 85  # Move up
#        up_steps += 1
#    elif direction == 'down' and down_steps < max_steps:
#        monster_y += 85  # Move down
#        down_steps += 1

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
  #  monster_x = max(0, min(screen_width - monster_rect.width, monster_x))
  #  monster_y = max(0, min(screen_height - monster_rect.height, monster_y))

    #screen.fill(white)
    #screen.fill((0, 0, 0))
    #screen.blit(monster_image, (monster_x, monster_y))
    #pygame.display.update()

   # clock.tick(2)  # Limit the frame rate per second
