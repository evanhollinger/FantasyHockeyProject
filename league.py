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
        """Displays each team and their players in a Tkinter GUI with enhanced styling."""
        pd.set_option('display.max_colwidth', None)
        teams = self.get_teams()  # Assuming `self.get_teams()` returns a list of `Team` objects

        # Create the main Tkinter window
        root = tk.Tk()
        root.title("ESPN Fantasy Hockey League Database")

        # Set the window size
        root.geometry("800x600")

        # Create a style object to customize the appearance of widgets
        style = ttk.Style()

        # Configure the theme to a more modern look
        style.theme_use("clam")

        # Configure Treeview styles
        style.configure("Treeview",
                        font=("Arial", 10),  # Set font for Treeview
                        rowheight=25,  # Set row height
                        foreground="black",  # Text color
                        background="#f4f4f4",  # Light background
                        fieldbackground="#e0e0e0")  # Field background color for cells

        style.configure("Treeview.Heading",
                        font=("Arial", 12, "bold"),  # Make column headers bold
                        foreground="darkblue",  # Column header text color
                        background="#d3d3d3")  # Column header background color

        # Add a frame for the Treeview widget
        frame = ttk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the Treeview widget with hierarchical rows
        tree = ttk.Treeview(frame, columns=('Player Name', 'Position'), show='tree headings')
        tree.pack(fill=tk.BOTH, expand=True)

        # Set up the main column for the team and player headings
        tree.heading('#0', text="Team / Players", anchor=tk.W)
        tree.column('#0', width=250, stretch=tk.NO)

        # Define additional columns for player details
        tree.heading('Player Name', text="Player Name", anchor=tk.W)
        tree.heading('Position', text="Position", anchor=tk.W)
        tree.column('Player Name', width=150, stretch=tk.YES)
        tree.column('Position', width=100, stretch=tk.YES)

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

                tree.insert(team_id, tk.END, text='', values=(player_name, player_position))

        # Add a scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add borders to the frame
        frame.config(borderwidth=2, relief="solid")

        # Start the Tkinter event loop
        root.mainloop()

    def __str__(self):
        """Returns a string representation of the league."""
        return f"League: {self.name}, Number of teams: {len(self.teams)}"

