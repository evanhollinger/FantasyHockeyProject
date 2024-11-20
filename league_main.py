class Team:
    def __init__(self, name, players=None):
        """
        Initializes a Team object.
        :param name: Name of the team.
        :param players: List of players on the team. Defaults to an empty list.
        """
        self.name = name
        self.players = players if players else []

    def add_player(self, player):
        """Add a player to the team."""
        self.players.append(player)

    def __str__(self):
        """Returns a string representation of the team."""
        players_str = ", ".join(self.players) if self.players else "No players"
        return f"Team: {self.name}, Players: {players_str}"


class League:
    def __init__(self, name):
        """
        Initializes a League object.
        :param name: Name of the league.
        """
        self.name = name
        self.teams = []

    def add_team(self, team):
        """Add a team to the league."""
        self.teams.append(team)

    def get_teams(self):
        """Returns a list of all teams in the league."""
        return self.teams

    def display_teams(self):
        """Displays information about all the teams in the league."""
        if not self.teams:
            print("No teams in the league yet.")
        for team in self.teams:
            print(team)

    def __str__(self):
        """Returns a string representation of the league."""
        return f"League: {self.name}, Number of teams: {len(self.teams)}"



