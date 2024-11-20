import requests


def add_players(league, roster_url):
    # Fetch roster data from the URL
    r = requests.get(roster_url)
    data = r.json()

    # Iterate through teams in the data
    for team_data in data['teams']:
        team_id = team_data['id']
        team_name = team_data['name']

        # Find the corresponding team in the league by ID
        team = next((t for t in league.teams if t.id == team_id), None)
        if team is None:
            print(f"Team with ID {team_id} not found in league.")
            continue

        # Add players to the team
        for entry in team_data['roster']['entries']:
            player_name = entry['playerPoolEntry']['player']['fullName']
            player = Player(player_name)  # Create a Player object
            team.add_player(player)  # Add the player to the team


class Player:
    def __init__(self, name, position = None, stats=None):
        """
        Initializes a Player object.
        :param name: Name of the player.
        :param position: Position of the player (e.g., 'Forward', 'Defense', 'Goalie').
        :param stats: Dictionary of stats for the player. Defaults to an empty dictionary.
        """
        self.name = name
        self.position = position if position else []
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
        return f"Name: {self.name}, Position: {self.position}, Stats: {self.stats}"
