from create_players import create_players
from Player import Player
from Game import Game

import pandas as pd


class GameTables:
    """
    A class for everything related to data-tables on the Guess the Raptors' Score web-page.
    === Public Attributes ===
    players: The players in the game.
    """

    players = list[Player]

    def __init__(self, database_path):
        """
        Initialize players from <database_path>.
        """
        self.players = []

    def get_leaderboard_table(self):
        """
        Get the main leaderboard table (i.e.) the list of players
        """
        pass

    def get_game_table(self, game_number):
        pass































