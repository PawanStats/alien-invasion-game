import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self.get_high_score()

    def get_high_score(self):
        """Gets high score from file, if it exists."""
        try:
            with open('highscore.json') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
            
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

