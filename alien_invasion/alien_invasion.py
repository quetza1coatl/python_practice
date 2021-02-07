import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        # init module
        pygame.init()
        # using external settings as local variable
        self.settings = Settings()

        # create a display surface, set it to a class variable
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            # get() returns all last events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # fill screen with specify color
            self.screen.fill(self.settings.bg_color)
            # overlay sheep image to main surface
            self.ship.blitme()
            # draw updated screen
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
