import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        file = 'high_score.txt'
        if os.stat(file).st_size == 0:
            self.high_score = 0 
        else:
            with open(file) as file_object:
                contents = file_object.read()
            self.high_score = int(contents)
        self.level = 1

        # Start Alien Invasion in a inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0