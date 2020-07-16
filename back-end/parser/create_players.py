from Player import Player
from Game import Game
import pandas as pd

regular_season_scores = [("Game 1 - vs. LAL", 120, 100),
                         ("Game 2 - vs. MIA", 110, 102)
                         ]


def create_players(data_path, event):
    """
    Create players in the game, from the provided data_path.
    """

    database = pd.read_excel(data_path)

    columns = list(database.columns)
    players = []

    for index, row in database.iterrows():

        player = Player(row["IG_USERNAME"])

        TOR_score_index = 1
        OTHER_score_index = 2

        for i in range(len(regular_season_scores)):
            current_headline = regular_season_scores[i][0]
            guessed_TOR_score = row[columns[TOR_score_index]]
            guessed_OTHER_score = row[columns[OTHER_score_index]]
            real_TOR_score = regular_season_scores[i][1]
            real_OTHER_score = regular_season_scores[i][2]

            current_game = Game(current_headline,
                                guessed_TOR_score, guessed_OTHER_score,
                                real_TOR_score, real_OTHER_score)

            player.add_game(current_game)

            TOR_score_index += 2
            OTHER_score_index += 2

        players.append(player)

    return players


def add_event_for_players(players, new_data_path, event):
    """
    Add another event for players still playing.
    This is created as a prototype, in case the game continues after the 8 remaining regular season games.
    """
    pass


if __name__ == "__main__":
    # For testing
    path = "/Users/shivambhatoolaul/Documents/GitHub/guess-the-raptors-score/back-end/data/for-testing.xlsx"
    ps = create_players(path, "Regular Season/")

    for p in ps:
        print(p)
        print("")
        for game in p.games:
            print(game)