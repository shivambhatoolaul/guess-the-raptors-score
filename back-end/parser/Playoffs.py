from create_players import create_players_for_regular_season
from game_table_to_html import game_table_to_html
from Player import Player
from Game import Game
from typing import List
from GameTable import GameTables
import pandas as pd
import sys


playoff_scores = [{"ROUND": 1, "vs": "BKN", "FINAL GAME": 4, "SCORE": (150, 122)}]

playoff_bonus_from_reg_season = {'mr_santorelli': 5,
                                 'yovng.m': 4,
                                 '_eyad_m': 6,
                                 '_liam148': 5,
                                 'gavin.uruci': 0,
                                 'atomlaboss': 7,
                                 'daniel_apush': 3,
                                 '416ahmed': 2,
                                 'omf_sacha': 7,
                                 'chef.lamotte': 2,
                                 'stafahussain': 0,
                                 'aaron.uruci': 1,
                                 'emmanuelrichmond_': 6,
                                 'tdeenoo': 3,
                                 'jake_1804': 4,
                                 '_416_zak': 1
                                 }


def create_players_for_playoff_round(round_number, data_path):
    """
    Create players for a round of the playoffs.
    """
    database = pd.read_excel(data_path)

    players = []

    for index, row in database.iterrows():

        player = Player(row["What's your Instagram username?"])
        data = playoff_scores[round_number-1]
        vs = data["vs"]
        score = data["SCORE"]

        current_headline = "TOR vs. " + str(vs) + " - ROUND " + str(round_number) + " OF PLAYOFFS."
        guessed_tor_score = row["TOR"]
        guessed_other_score = row[vs]
        real_tor_score = score[0]
        real_other_score = score[1]

        current_game = PlayoffRound(current_headline,
                                    guessed_tor_score, guessed_other_score,
                                    real_tor_score, real_other_score)

        # add bonus from regular season
        bonus_points = 0
        bonus_points += playoff_bonus_from_reg_season[player.username]
        guessed_last_game = row["How many games do you think this series is going to go up to?"]
        current_game.update_elimination_game_guess(guessed_last_game)  # needed for HTML table...
        real_last_game = int(data["FINAL GAME"])

        if guessed_last_game == real_last_game:
            bonus_points += 10

        current_game.add_bonus_to_score(bonus_points)

        player.add_game(current_game)

        players.append(player)

    return players


class PlayoffRound(Game):
    """
    To keep track of a round in the playoffs.
    """
    def __init__(self, headline,
                 guess_TOR, guess_OTHER,
                 actual_TOR, actual_OTHER
                 ):
        """
        Initialize this round's headline, the <self. guess>
        and <self.actual> if available.
        """
        super().__init__(headline, guess_TOR, guess_OTHER, actual_TOR, actual_OTHER)
        self.guessed_elimination_game_number = 7

    def update_elimination_game_guess(self, guess):
        """
        Update when this player guessed the elimination game for this playoff round would be.
        """
        self.guessed_elimination_game_number = guess


class PlayoffTables(GameTables):
    """
    A class for a playoff table in the Guess the Raptors' Game.
    === Public Attributes ===
    players: The players in the game.
    round_number: what round of the playoffs this is.
    """

    def __init__(self, round_number, database_path):
        # super().__init__(database_path)  # super uses create_players_for_regular_season...
        try:
            self.round_number = round_number
            # check if we have data for this round before creating players for this round.
            if round_number > len(playoff_scores):
                print("ERROR: We don't have data up to this playoff round yet.")
                self.players = []
                sys.exit(1)

            self.players = create_players_for_playoff_round(round_number, database_path)

        except:
            print("ERROR: Database is not formatted correctly to create players in game.")
            self.players = []
            sys.exit(1)

    def get_round_table(self):
        """
        Get the table for this round of the playoffs.
        """

        players = self.players

        # error checking
        if len(players) <= 0:
            print("ERROR: No players in database.")
            return

        elif len(players[0].games) != 1:
            print("ERROR: This player only has data from the regular season for now.")
            return

        else:
            game_table = []
            for player in players:
                game = player.games[0]
                guess = "GAME " + str(game.guessed_elimination_game_number) + ": " + str(game.guess["TOR"]) + "-" + str(game.guess["OTHER"])
                player_game_info = ['<a href="https://www.instagram.com/{0}/">'.format(player.username) +
                                    '@' + player.username + '</a>',
                                    guess,
                                    game.score]
                game_table.append(player_game_info)

            game_table_df = pd.DataFrame(game_table, columns=["PLAYER", "GUESS", "SCORE"])
            game_table_df.sort_values("SCORE", ascending=False, ignore_index=True, inplace=True)

            # format link
            return game_table_df


if __name__ == "__main__":
    path = "/Users/shivambhatoolaul/Documents/GitHub/guess-the-raptors-score/back-end/data/guess_playoffs_round_1.xlsx"

    guess_the_raptors_score_round_1 = PlayoffTables(round_number=1, database_path=path).get_round_table()

    print(game_table_to_html(guess_the_raptors_score_round_1, "ROUND 1 - vs. BKN"))

