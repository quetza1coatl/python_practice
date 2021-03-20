from game_complexity import GameComplexity


class Settings:
    def __init__(self):
        # general
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship
        self.ship_limit = 3
        # bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        # aliens
        self.fleet_drop_speed = 10
        # button complexity - vertical_shift_factor map. Keys: 0 - for easy, 2 for hard
        self.button_vertical_shift_factor_map = {GameComplexity.easy.complexity_factor: -1,
                                                 GameComplexity.normal.complexity_factor: 0,
                                                 GameComplexity.hard.complexity_factor: 1}
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.alien_points = 50

        self.initialize_dynamic_settings(GameComplexity.normal.complexity_factor)

    def initialize_dynamic_settings(self, game_complexity):
        """Initialize settings that change throughout the game."""
        # easy
        if game_complexity == GameComplexity.easy.complexity_factor:
            self.bullets_allowed = 5
            self.ship_speed = 2
            self.bullet_speed = 4.0
            self.alien_speed = 0.5
        # hard
        elif game_complexity == GameComplexity.hard.complexity_factor:
            self.bullets_allowed = 3
            self.ship_speed = 1.2
            self.bullet_speed = 3.0
            self.alien_speed = 1.3
        # normal for other
        else:
            self.bullets_allowed = 4
            self.ship_speed = 1.6
            self.bullet_speed = 3.0
            self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
