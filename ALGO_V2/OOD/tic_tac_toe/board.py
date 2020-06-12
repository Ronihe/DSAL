import os
import pprint


class Game:
    def __init__(self, board, player1, player2):
        if player1.avatar == player2.avatar:
            raise NameError("two players can not have the same avatars")
        self._board = board
        self._players = (player1, player2)
        self.moves = 0

    def greet(self):
        print(f'welcome to tic tac toe! player {self._players[0].avator} and player {self._players[1].avator}')

    def play(self):
        flag = True
        while flag:
            self._board.display()

            turn = self.moves % 2
            curr_player = self._players[turn]
            self.make_move(curr_player)
            if self.check_win(curr_player) or self.check_tie():
                self.game_over(curr_player)
                break

    def make_move(self, player):
        row, col = self.ask_for_move(player)
        self._board.update_cell(row, col, player.avatar)
        self.moves += 1

    def ask_for_move(self, player):
        row = int(input(f"\n {player.avatar}, please choose row number with in the size"))
        col = int(input(f"\n {player.avatar}, please choose col number within the size"))
        if not self._board.validate(row, col):
            print("not valid move, please try again")
            self.ask_for_move(player)
        return row, col

    def check_win(self, player):
        return self._board.is_winner(player)

    def check_tie(self):
        return self.moves >= self._board.size ** 2

    def game_over(self, player):
        print(f'thanks for playing, {player.avatar} won!')


class Player:
    def __init__(self, avatar):
        self.avatar = avatar


class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [["" for c in range(size)] for r in range(size)]

    def display(self):
        pprint.pprint(self.cells, width=25)

    def update_cell(self, row, col, player):
        if not self.cells[row - 1][col - 1]:
            self.cells[row - 1][col - 1] = player
        else:
            print("taken already")

        print(self.is_winner(player))

    def validate(self, row, col):
        if (row < 0 or row >= self.size) or (col < 0 or col >= self.size):
            return False
        if self.cells[row][col]:
            return False

        return True

    def is_winner(self, player):
        for row in self.cells:
            if all([cell == player for cell in row]):
                return f'{player} won'

        for col in range(len(self.cells[0])):
            if all([row[col] == player for row in self.cells]):
                return f'{player} won'

        if all([self.cells[row][col] == player for row in range(len(self.cells)) for col in range(len(self.cells)) if
                row == col]):
            return f'{player} won'

        if all([self.cells[row][col] == player for row in range(len(self.cells)) for col in range(len(self.cells)) if
                row + col == len(self.cells)]):
            return f'{player} won'

        return False


board = Board(3)
player1 = Player("X")
player2 = Player("O")
game = Game(board, player1, player2)
game.play()
