# noinspection PyAttributeOutsideInit
class Settings:
    """A class to store all the settings in Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3
        # Bullet settings.
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 3.0

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # noinspection PyAttributeOutsideInit
    def initialize_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represent right, -1 represents left.
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.score_scale * self.alien_points)
