import pygame


class Ship:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # load picture. Method 'load' returns Surface object!
        self.image = pygame.image.load('../images/ship_rotated.bmp')
        self.rect = self.image.get_rect()
        # New ship is created at the middle-bottom position of the screen
        self.rect.midleft = self.screen_rect.midleft
        # flag for moving in the  -> and <- directions
        self.moving_up = False
        self.moving_down = False
        # Rect uses int only, but we need float for more accurate calculations
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
