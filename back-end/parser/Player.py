from Game import Game


class Player:
    """
    A class for a player in the GameTables.
    === Public Attributes ===
    username: The name of the player.
    ig_link: This player's Instagram link.
    games: The guesses that the player made for the Raptor's games.
    points: The total points that the player has for their <score_guesses>
    """
    username: str
    ig_link = str
    games: list
    points: int

    def __init__(self, username):
        """
        Initialize this player w/ <name>, an empty dict of guesses for the games,
        and 0 points.
        """
        self.username = username.strip('@')
        self.ig_link = "https://www.instagram.com/" + username + "/"
        self.games = []
        self.points = 0

    def add_game(self, game):
        """
        Add a <game>'s guessed score (+ actual score for this game)
        to this player's <self.score_guesses>.
        """
        self.games.append(game)
        self.update_points()

    def update_points(self):
        """
        From <self.score_guesses>, update the total number of points this player should have.
        """
        total = 0
        for game in self.games:
            total += game.score
        self.points = total

    def __repr__(self):
        """
        str representation of Player in console...
        """
        return self.username + ": " + str(self.points) + " TOTAL POINTS."
