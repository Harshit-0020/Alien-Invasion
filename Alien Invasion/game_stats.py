class GameStats:
    """Tracks statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialise statistics."""
        # High score should never  be reset.
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()
        # Start the game in an active state.
        self.game_active = False

    # noinspection PyAttributeOutsideInit
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.game_level = 1
