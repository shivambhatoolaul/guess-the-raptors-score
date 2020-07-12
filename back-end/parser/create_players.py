from Player import Player
import pandas as pd


def create_players(data_path):
    """
    Create players in the game, from the provided data_path.
    """

    database = pd.read_excel(data_path)

    print(database)


if __name__ == "__main__":
    # For testing
    data_path = '/Users/shivambhatoolaul/Documents/GitHub/guess-the-raptors-score/"back-end"/data/for-testing.xlsx'
    create_players(data_path)