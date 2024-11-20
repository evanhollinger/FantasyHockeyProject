class Player:
    def __init__(self, name, position, stats=None):
        """
        Initializes a Player object.
        :param name: Name of the player.
        :param position: Position of the player (e.g., 'Forward', 'Defense', 'Goalie').
        :param stats: Dictionary of stats for the player. Defaults to an empty dictionary.
        """
        self.name = name
        self.position = position
        self.stats = stats if stats else {}

    def get_name(self):
        """Return the name of the player."""
        return self.name

    def get_position(self):
        """Return the position of the player."""
        return self.position

    def get_stats(self):
        """Return the stats of the player."""
        return self.stats

    def add_stat(self, stat_name, stat_value):
        """Add or update a stat for the player."""
        self.stats[stat_name] = stat_value

    def __str__(self):
        """Returns a string representation of the player."""
        stats_str = ", ".join(f"{stat}: {value}" for stat, value in self.stats.items()) if self.stats else "No stats"
        return f"Player: {self.name}, Position: {self.position}, Stats: {stats_str}"
