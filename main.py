from league import create_league

if __name__ == '__main__':
    print("Hello world - Day 0 (11/19/2024)")

    # ESPN API key to pull league data and store in url
    url = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/fhl/seasons/2025/segments/0/leagues/1157174311?view=modular&view=mNav&view=mMatchupScore&view=mScoreboard&view=mStatus&view=mSettings&view=mTeam&view=mPendingTransactions"
    league = create_league(url)
    league.display_teams()

    print("Goodbye world - Day 0 end")

