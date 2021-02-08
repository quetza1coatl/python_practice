import pygame


class Ship:
    def __init__(self, ai_game):
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

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
