class Team:
    def __init__(self, name, players=None):
        """
        Initializes a Team object.
        :param name: Name of the team.
        :param players: List of players on the team. Defaults to an empty list.
        """
        self.name = name
        self.players = players if players else []

    def get_name(self):
        return self.name

    def add_player(self, player):
        """Add a player to the team."""
        self.players.append(player)

    def __str__(self):
        """Returns a string representation of the team."""
        players_str = ", ".join(self.players) if self.players else "No players"
        return f"Team: {self.name}, Roster: {players_str}"
