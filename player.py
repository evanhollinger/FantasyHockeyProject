import requests
import requests

def add_players(league, roster_url):
    # Fetch roster data from the URL
    response = requests.get(roster_url)
    data = response.json()

    # Position mapping based on defaultPositionId
    position_map = {
        1: "Center",
        2: "Left Wing",
        3: "Right Wing",
        4: "Defense",
        5: "Goalie"
    }

    # Updated stat mapping with descriptive labels
    stat_map = {
        '13': "Goals",
        '14': "Assists",
        '15': "Plus/Minus",
        '16': "Points",
        '17': "PIM",       # Penalty Minutes
        '18': "PPG",       # Power Play Goals
        '19': "PPA",       # Power Play Assists
        '27': "TOI/G"      # Time on Ice per Game
    }

    # Function to convert seconds to mm:ss format
    def convert_to_time_format(seconds):
        # Round the seconds to the nearest whole number
        seconds = round(seconds)
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    # Iterate through teams in the data
    for team_data in data['teams']:
        team_id = team_data['id']
        team_name = team_data['name']

        # Find the corresponding team in the league by ID
        team = next((t for t in league.teams if t.id == team_id), None)
        if not team:
            print(f"Team with ID {team_id} not found in league.")
            continue

        # Add players to the team
        for entry in team_data['roster']['entries']:
            player = entry['playerPoolEntry']['player']
            player_name = player['fullName']
            position_id = player['defaultPositionId']
            position = position_map.get(position_id, "Unknown")

            # Find the player stats for the specific player ID
            player_stat = next((e['stats'] for e in player['stats'] if e['id'] == '002025'), {})

            # Map the stats based on stat_map (using the stat map for descriptive labels)
            mapped_stats = {}

            # Loop over the stat_map and convert the values
            for key in stat_map:
                stat_name = stat_map[key]
                stat_value = player_stat.get(key, 0)

                # If the stat is 'TOI/G', convert it from seconds to mm:ss format
                if key == '27':
                    mapped_stats[stat_name] = convert_to_time_format(stat_value)
                else:
                    mapped_stats[stat_name] = stat_value

            # Create a Player object with the position and mapped stats
            new_player = Player(name=player_name, position=position, stats=mapped_stats)

            # Add the player to the team
            team.add_player(new_player)

class Player:
    def __init__(self, name, position=None, stats=None):
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
