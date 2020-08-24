def _get_outcome(raptors_score, other_score):
    """
    Private method to get outcome of the game (i.e. W or L).
    """
    if raptors_score > other_score:
        return "W"
    else:
        return "L"


def _get_starting_score(guessed_outcome, actual_outcome):
    """
    Private method to get starting score from guessed outcome of the game.
    """
    if actual_outcome == guessed_outcome:
        return 100
    else:
        return 75


class Game:
    """
    A class to keep track of a game's guessed score and actual score.
    === Public Attributes ===
    headline: The name of this game (for ex. Game 1 - TOR vs. LAL).
    guess: The score that someone guessed for this game.
    actual: The actual score for this game.
    score: How much should the guess score (i.e. points for guess when compared to actual).
    """

    headline: str
    guess: dict
    actual: dict
    score: int

    def __init__(self,
                 headline,
                 guess_TOR, guess_OTHER,
                 actual_TOR, actual_OTHER
                 ):
        """
        Initialize this game's headline, the <self. guess>
        and <self.actual> if available.
        """
        self.headline = headline
        self.guess = {"TOR": guess_TOR, "OTHER": guess_OTHER, "outcome": _get_outcome(guess_TOR, guess_OTHER)}
        self.actual = {"TOR": actual_TOR, "OTHER": actual_OTHER, "outcome": _get_outcome(actual_TOR, actual_OTHER)}
        self.score = self.get_score()

    def get_score(self):
        """
        Get the score that the player should get for their guess.
        Scoring system at: https://shivambhatoolaul.github.io/guess-the-raptors-score/submit.html
        """
        guess = self.guess
        actual = self.actual

        # no actual available yet
        if actual["TOR"] is None or actual["OTHER"] is None:
            return 0

        # error
        if guess["TOR"] is None or guess["OTHER"] is None:
            return -1

        # perfect guess
        elif actual["TOR"] == guess["TOR"] and actual["OTHER"] == guess["OTHER"]:
            return 150

        else:
            starting_score = _get_starting_score(guess["outcome"], actual["outcome"])
            penalty = abs(guess["TOR"] - actual["TOR"]) + abs(guess["OTHER"] - actual["OTHER"])
            return starting_score - penalty

    def add_bonus_to_score(self, bonus_points):
        """
        Add a bonus to the score of the game.
        """
        self.score += bonus_points

    def __repr__(self):
        """
        str representation of game in console...
        """
        guess = self.guess
        actual = self.actual
        headline = self.headline + " \n"
        guess_message = "GUESS: TOR " + str(guess["TOR"]) + " - " + str(guess["OTHER"]) + " OTHER \n"
        actual_message = "ACTUAL: TOR " + str(actual["TOR"]) + " - " + str(actual["OTHER"]) + " OTHER \n"
        points = "POINTS: " + str(self.score) + " \n"

        return headline + guess_message + actual_message + points
