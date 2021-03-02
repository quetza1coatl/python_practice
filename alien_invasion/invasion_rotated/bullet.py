import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # create a bullet rect at the 0,0 point and immediately change this coordinates
        # we do so because our bullet is not created from image (we have no bullet surface at this moment)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.ship_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)