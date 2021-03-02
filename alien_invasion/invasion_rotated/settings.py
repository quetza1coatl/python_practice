class Settings:
    def __init__(self):
        # general
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship
        self.ship_speed = 0.7
        # bullet
        self.bullet_speed = 1.3
        self.bullet_width = 12
        self.bullet_height = 3
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5
        # aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 for right direction, -1 for left direction. We can simply use multiplying to change 'x' coordinate with +/-
        self.fleet_direction = 1
