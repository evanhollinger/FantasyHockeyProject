import pandas as pd


class Team:
    def __init__(self, name, id, players=None):
        """
        Initializes a Team object.
        :param name: Name of the team.
        :param players: List of players on the team. Defaults to an empty list.
        """
        self.name = name
        self.id = id
        self.players = []

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def add_player(self, player):
        """Add a player to the team."""
        self.players.append(player)

    def __str__(self):
        # Join the player names (not the Player objects)
        players_str = ", ".join([str(player) for player in self.players]) if self.players else "No players"
        return f"Team: {self.name} (ID: {self.id}), Players: {players_str}"
