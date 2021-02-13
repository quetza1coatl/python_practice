import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Each new alien appears in the upper left corner of the screen with indent.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Save the exact horizontal position of the alien - this position is more important.
        self.x = float(self.rect.x)
