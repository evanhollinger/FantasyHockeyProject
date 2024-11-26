from league import create_league
from player import add_players

if __name__ == '__main__':
    print("Hello world - Day 0 (11/19/2024)")

    # ESPN API key to pull league data and store in url
    league_url = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/fhl/seasons/2025/segments/0/leagues/1157174311?view=modular&view=mNav&view=mMatchupScore&view=mScoreboard&view=mStatus&view=mSettings&view=mTeam&view=mPendingTransactions"
    league = create_league(league_url)

    # ESPN API key to pull player data from each team
    roster_url = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/fhl/seasons/2025/segments/0/leagues/1157174311?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav"
    add_players(league, roster_url)
    league.display_teams()

