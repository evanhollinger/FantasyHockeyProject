import requests
import pandas as pd

from team import Team


def create_league(league_url):
    # example link - https://fantasy.espn.com/hockey/league?leagueId=1157174311

    # Store url data - Store data in JSON format - From JSON get all members
    r = requests.get(league_url)
    data = r.json()
    members = data["teams"]
    settings = data["settings"]
    league_name = settings["name"]

    new_league = League(league_name)

    # Loop through all members (for team names / abrevs)
    for member in members:
        name = member['name']
        team_id = member['id']
        temp = Team(name, team_id)
        new_league.add_team(temp)

    return new_league


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

        pd.set_option('display.max_colwidth', None)
        df = pd.DataFrame(self.get_teams())  # Create main DataFrame for the league

        # Display the league DataFrame
        print(df)

    def __str__(self):
        """Returns a string representation of the league."""
        return f"League: {self.name}, Number of teams: {len(self.teams)}"

