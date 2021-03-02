import pygame
import sys

from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        # init module
        pygame.init()
        # using external settings as local variable
        self.settings = Settings()

        # create a display surface, set it to a class variable
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        # get() returns all last events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _update_screen(self):
        # fill screen with specify color
        self.screen.fill(self.settings.bg_color)
        # overlay sheep image to main surface
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # draw updated screen
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        print(f'Screen size x:{self.screen.get_rect().width} y: {self.screen.get_rect().height}')
        print(f'Alien init location x:{alien.rect.x} y:{alien.rect.y}')
        ship_width = self.ship.rect.width
        available_space_x = self.settings.screen_width - (3 * alien_width) - ship_width
        number_columns = available_space_x // (2 * alien_width)
        print(f'available space x : {available_space_x}')
        print(f'number columns: {number_columns}')

        available_space_y = self.settings.screen_height - alien_height
        number_aliens_y = available_space_y // (2 * alien_height)
        print(f'available space y : {available_space_y}')
        print(f'number aliens y : {number_aliens_y}')

        for columns in range(number_columns):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, columns)

    def _create_alien(self, alien_number, column):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = self.screen.get_rect().right - 2 * alien.rect.width * column - 2 * alien.rect.width
        alien.y = alien.rect.height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        print(f'alien x: {alien.rect.x} y: {alien.rect.y}')
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        # check collisions. Returns map with collided objects.
        # True, True - means delete collided objects from both sprite groups
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
