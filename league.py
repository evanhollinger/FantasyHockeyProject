import requests
import pandas as pd
import tkinter as tk
from tkinter import ttk
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
        """Displays each team and their players in a Tkinter GUI with a dark theme."""
        pd.set_option('display.max_colwidth', None)
        teams = self.get_teams()  # Assuming `self.get_teams()` returns a list of `Team` objects

        # Extract all unique stat keys from player stats
        all_stats = set()
        for team in teams:
            for player in team.players:
                all_stats.update(player.stats.keys())

        # Create the main Tkinter window
        root = tk.Tk()
        root.title("ESPN Fantasy Hockey League Database")

        # Set the window size
        root.geometry("1920x1080")

        # Dark theme color variables
        DARK_BG = "#2e2e2e"
        TREEVIEW_BG = "#3b3b3b"
        TREEVIEW_FG = "#e0e0e0"
        TREEVIEW_HEADER_BG = "#4a4a4a"
        TREEVIEW_HEADER_FG = "#ffffff"
        SCROLLBAR_BG = "#5a5a5a"

        # Configure the main window with a dark background
        root.configure(bg=DARK_BG)

        # Create a style object to customize widget appearance
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        font=("Arial", 10),
                        rowheight=25,
                        foreground=TREEVIEW_FG,
                        background=TREEVIEW_BG,
                        fieldbackground=TREEVIEW_BG)
        style.configure("Treeview.Heading",
                        font=("Arial", 12, "bold"),
                        foreground=TREEVIEW_HEADER_FG,
                        background=TREEVIEW_HEADER_BG)

        # Create a frame to hold the Treeview widget
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Define all Treeview columns: Player Name, Position, and dynamically created stat columns
        columns = ['Player Name', 'Position'] + list(all_stats)

        # Create the Treeview widget
        tree = ttk.Treeview(frame, columns=columns, show='tree headings')
        tree.pack(fill=tk.BOTH, expand=True)

        # Set up the main column for the team and player headings
        tree.heading('#0', text="Team / Players", anchor=tk.W)
        tree.column('#0', width=200, stretch=tk.NO)

        # Define the additional columns and headings dynamically
        for column in columns:
            tree.heading(column, text=column, anchor=tk.W)
            tree.column(column, width=100, stretch=tk.NO)

        # Populate the Treeview with teams and their players
        for team in teams:
            team_name = team.name  # Assuming the `Team` class has a 'name' attribute
            team_players = team.players  # Assuming the `Team` class has a 'players' attribute

            # Add a team as a parent row
            team_id = tree.insert('', tk.END, text=team_name, open=True)

            # Add each player under the team
            for player in team_players:
                player_name = player.name  # Assuming Player class has a 'name' attribute
                player_position = player.position  # Assuming Player class has a 'position' attribute
                player_stats = player.stats  # Assuming Player class has a 'stats' dictionary

                # Fill the row data dynamically, ensuring all columns align with their keys
                row_data = [player_name, player_position] + [player_stats.get(stat, "") for stat in all_stats]

                # Insert the player row under the team
                tree.insert(team_id, tk.END, text='', values=row_data)

        # # Add borders to the frame
        # frame.config(borderwidth=2, relief="solid")

        # Start the Tkinter event loop
        root.mainloop()

    def __str__(self):
        """Returns a string representation of the league."""
        return f"League: {self.name}, Number of teams: {len(self.teams)}"
