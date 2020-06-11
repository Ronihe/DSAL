# define the generic game state.

class GameState:
    """
    does not implement useful functionalities, but starting the base class for implementing the state for other games.
    """

    def __init__(self):
        pass

    def make_move(self, player, move):
        pass

    def legal_move(self, player, move):
        pass

    def game_over(self):
        pass

    def outcome(self):
        pass

    def serlize(self):
        pass

    def __str__(self):
        return '<generic game="", state="">'
