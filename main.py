from league_main import Team, League

import requests
import pandas as pd


if __name__ == '__main__':
    print("Hello world - Day 0 (11/19/2024)")

    # Example of using the classes:

    # Create a league
    fantasy_league = League("Fantasy Football League")

    # Create teams and add players
    team1 = Team("ET", ["Michkov", "Sanheim", "Fedotov"])
    team2 = Team("E2T", ["Brink", "Konecny"])

    # Add teams to the league
    fantasy_league.add_team(team1)
    fantasy_league.add_team(team2)

    # Display information about all teams in the league
    fantasy_league.display_teams()

    # Example of adding a new player to a team
    team1.add_player("McDavid")
    print("\nUpdated team details:")
    fantasy_league.display_teams()

