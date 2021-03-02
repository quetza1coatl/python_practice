import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()
        # Each new alien appears in the upper right corner of the screen with indent.
        self.rect.x = self.screen.get_rect().right - 2 * self.rect.width
        self.rect.y = self.rect.height
        # Save the exact vertical position of the alien - this position is more important.
        self.y = float(self.rect.y)
        self.settings = ai_game.settings

    def update(self):
        self.y += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True
