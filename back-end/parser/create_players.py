from Player import Player
from Game import Game
import pandas as pd

regular_season_scores = [("GAME 1 - vs. LAL", 107, 92),
                         ("GAME 2 - vs. MIA", 107, 103),
                         ("GAME 3 - vs. ORL", 109, 99),
                         ("GAME 4 - vs. BOS", 100, 122),
                         ("GAME 5 - vs. MEM", 108, 99),
                         ("GAME 6 - vs. MIL", 114, 106),
                         ]


def create_players(data_path):
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


if __name__ == "__main__":
    # For testing
    path = "/Users/shivambhatoolaul/Documents/GitHub/guess-the-raptors-score/back-end/data/for-testing.xlsx"
    ps = create_players(path)

    for p in ps:
        print(p)
        print("")
        for game in p.games:
            print(game)
