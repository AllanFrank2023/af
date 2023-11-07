#plade = __import__('board')
#mons = __import__('Monster')
import pygame
import sys
import random


class Spillelogik:
    def __init__(self, screen, image):
        self.screen = screen
        self.monster = Monster(self.screen, image, max_steps)
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
            self.clock.tick(60)  # Limit the frame rate to 60 frames per second

def main():
    pygame.init()
    screen_width = 1600
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Monster Moving")

    original_image = pygame.image.load("monster.png")
    desired_width = 85
    desired_height = 55
    resized_image = pygame.transform.scale(original_image, (desired_width, desired_height))
    pygame.image.save(resized_image, "monster3.png")
    monster_image = pygame.image.load("monster3.png")

    game = Spillelogik(screen, monster_image)
    game.run()

if __name__ == "__main__":
    main()
