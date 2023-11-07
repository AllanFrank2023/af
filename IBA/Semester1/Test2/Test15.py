import pygame
import sys
import random

class Monster:
    def __init__(self, screen, image, max_steps=80):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, self.screen.get_height() - self.rect.height)
        self.max_steps = max_steps
        self.step_counters = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
    # Randomly select a direction
    # Update the monster's position based on the selected direction and step count
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

class Board:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, monster):
        self.screen.fill((0, 0, 0))
        self.screen.blit(monster.image, (monster.rect.x, monster.rect.y))
        pygame.display.update()

class GameLogic:
    def __init__(self, screen, image):
        self.screen = screen
        self.monster = Monster(self.screen, image)
        self.board = Board(self.screen)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.monster.move()
            if all(step_counter == self.monster.max_steps for step_counter in self.monster.step_counters.values()):
                self.monster.reset_step_counters()

            self.board.draw(self.monster)
            self.clock.tick(2)  # Limit the frame rate to 60 frames per second

def main():
    # Initialize Pygame
    pygame.init()
    # Screen dimensions
    screen_width = 1600
    screen_height = 1000
    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Monster Moving")
    # Load the original image / resize png and save it/load png
    original_image = pygame.image.load("monster.png")
    desired_width = 85
    desired_height = 55
    resized_image = pygame.transform.scale(original_image, (desired_width, desired_height))
    pygame.image.save(resized_image, "monster3.png")
    monster_image = pygame.image.load("monster3.png")
    # Monster starting position
    monster_x = random.randint(0, screen_width)
    monster_y = random.randint(0, screen_height)
    # Ensure the monster stays within the screen boundaries
    monster_x = max(0, min(screen_width - desired_width, monster_x))
    monster_y = max(0, min(screen_height - desired_height, monster_y))


    game = GameLogic(screen, monster_image)
    game.run()

if __name__ == "__main__":
    main()
