import pygame


class Ship:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # load picture. Method 'load' returns Surface object!
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # New ship is created at the middle-bottom position of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # flag for moving in the  -> and <- directions
        self.moving_right = False
        self.moving_left = False
        # Rect uses int only, but we need float for more accurate calculations
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
