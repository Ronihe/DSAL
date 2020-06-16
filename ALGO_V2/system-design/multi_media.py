import sys
from enum import Enum
from collections import namedtuple
from typing import List, Optional


class Player(Enum):
    player1 = 'O'
    player2 = 'X'


Point = namedtuple('Point', ('x', 'y'))


class Board():
    cells: List[List[Optional[str]]] = []

    #
    def __init__(self):
        self.cells = [[None] * 3 for i in range(3)]

    def render(self):
        """
        prints out the current game state to the console
        """

        for i in range(3):
            print('   ', ''.join([f' [{self.cells[i][j] or " "}] '
                                  for j in range(3)]))
        print('')

    def play(self, player: Player, point: Point):
        """
        returns True if the game has ended (current player has won).
        """

        if not self.validate_play(point):
            raise Exception("not valid move.")

        self.cells[point.x - 1][point.y - 1] = player.value
        self.render()
        return False

    def validate_play(self, point: Point):

        if self.cells[point.x - 1][point.y - 1]:
            return False
        if point.x < 1 or point.x > 3:
            return False
        if point.y < 1 or point.y > 3:
            return False

        return True

    def is_winner(self, player: Player):
        # horizontal
        for row in self.cells:
            return all([cell == player for cell in row]):

            # vertical
            for col in range(self.cells):
                [self.cells[][col]]

            # diagnal
            pass

    class Game:
        board: Board

        def __init__(self):
            self.board = Board()

        def run_plays(self, plays: List[Point]):
            """
            runs a set of plays non-interactively

            If a move cannot be made, the game will
            terminate with an error message
            """

            turn = 0
            for play in plays:
                active_player = list(Player)[turn % 2]
                if self.board.play(active_player, play):
                    print(f"Player {active_player} won!!!")
                    return
                turn += 1

            # Only two games should be ran at a time

    # CodeInterview will truncate the output

    # print("Game 1: Bad Move")
    # game = Game()
    # game.run_plays([
    #   Point(2, 2),
    #   Point(2, 1),

    # ])

    print("\n\nGame 2: No Winner")
    game = Game()
    game.run_plays([
        Point(2, 2),
        Point(1, 2),
        Point(1, 1),
        Point(3, 3),
        Point(1, 3),
        Point(2, 1),
        Point(2, 3),
        Point(3, 1),
        Point(3, 2)
    ])

    # print("\n\nGame 3: Column Check")
    # game = Game()
    # game.run_plays([
    #   Point(2, 2),
    #   Point(2, 1),
    #   Point(1, 2),
    #   Point(2, 3),
    #   Point(3, 2),
    # ])

    # print("\n\nGame 4: Row Check")
    # game = Game()
    # game.run_plays([
    #   Point(2, 2),
    #   Point(1, 2),
    #   Point(1, 1),
    #   Point(3, 3),
    #   Point(2, 3),
    #   Point(1, 3),
    #   Point(2, 1)
    # ])

    # print("\n\nGame 5: Diagonal LR")
    # game = Game()
    # game.run_plays([
    #   Point(2, 2),
    #   Point(1, 2),
    #   Point(1, 1),
    #   Point(3, 2),
    #   Point(3, 3),
    # ])

    # print("\n\nGame 6: Diagonal RL")
    # game = Game()
    # game.run_plays([
    #   Point(2, 2),
    #   Point(1, 2),
    #   Point(1, 3),
    #   Point(3, 2),
    #   Point(3, 1),
    # ])

