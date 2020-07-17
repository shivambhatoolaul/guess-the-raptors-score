from create_players import create_players
from game_table_to_html import game_table_to_html
from Player import Player
from typing import List
import pandas as pd
import sys


class GameTables:
    """
    A class for everything related to data-tables on the Guess the Raptors' Score web-page.
    === Public Attributes ===
    players: The players in the game.
    """

    players = List[Player]

    def __init__(self, database_path):
        """
        Initialize players from <database_path>.
        """
        # error checking
        try:
            self.players = create_players(database_path)
        except:
            print("ERROR: Database is not formatted correctly to create players in game.")
            self.players = []
            sys.exit(1)

    def get_leaderboard_table(self):
        """
        Get the main leaderboard table (i.e.) the list of players
        """
        players = self.players

        # error checking
        if len(players) <= 0:
            print("ERROR: No players in database.")
            return

        else:
            leaderboard_table = []
            for player in players:
                player_game_info = ['<a href="https://www.instagram.com/{0}/">'.format(player.username) + '@' + player.username + '</a>',
                                    player.points]
                leaderboard_table.append(player_game_info)

            leaderboard_table_df = pd.DataFrame(leaderboard_table, columns=["PLAYER", "SCORE"])
            # format link
            return leaderboard_table_df

    def get_game_table(self, game_number):
        """
        Get the score for a game.
        """
        players = self.players

        # error checking
        if len(players) <= 0:
            print("ERROR: No players in database.")
            return

        elif len(players[0].games) < game_number:
            print("ERROR: No real game scores available for this game yet...")
            return

        else:
            game_table = []
            for player in players:
                game = player.games[game_number-1]  # zero indexing
                player_game_info = ['<a href="https://www.instagram.com/{0}/">'.format(player.username) + '@' + player.username + '</a>',
                                    game.score]
                game_table.append(player_game_info)

            game_table_df = pd.DataFrame(game_table, columns=["PLAYER", "SCORE"])
            # format link
            return game_table_df


if __name__ == "__main__":
    # For testing
    path = "/Users/shivambhatoolaul/Documents/GitHub/guess-the-raptors-score/back-end/data/guesses.xlsx"
    guess_the_raptors_score = GameTables(path)

    #gt1 = guess_the_raptors_score.get_game_table(game_number=1)

    html = game_table_to_html(guess_the_raptors_score.get_leaderboard_table(), "LEADERBOARD")

    print(html)



























