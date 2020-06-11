import os
import pprint


class Board:
    def __init__(self, size):
        self.cells = [["" for c in range(size)] for r in range(size)]

    def display(self):
        pprint.pprint(self.cells, width=25)

    def update_cell(self, row, col, player):
        print(self.cells[row - 1][col - 1])
        if not self.cells[row - 1][col - 1]:
            self.cells[row - 1][col - 1] = player
        else:
            print("taken already")

        print(self.is_winner(player))

    def is_winner(self, player):
        for row in self.cells:
            print("horizontal", all([cell == player for cell in row]))
            if all([cell == player for cell in row]):
                return f'{player} won'

        for col in range(len(self.cells[0])):
            print([row[col] == player for row in self.cells])
            if all([row[col] == player for row in self.cells]):
                return f'{player} won'
        print([self.cells[row][col] == player for row in range(len(self.cells)) for col in range(len(self.cells)) if
            row == col])
        if all([self.cells[row][col] == player for row in range(len(self.cells)) for col in range(len(self.cells)) if
            row == col]):
            return f'{player} won'

        if all([self.cells[row][col] == player for row in range(len(self.cells)) for col in range(len(self.cells)) if
            row + col == len(self.cells)]):
            return f'{player} won'

        return False

    def is_tie(self):
        return all([c for row in self.cells for c in row ])



b = Board(3)


def print_header():
    print("welcome to play tic tac toe")


def refresh():
    # todo belong to game class
    # os.system("clear")
    # print_header()
    # show the board
    b.display()


while True:
    refresh()
    # get x input
    x_row = int(input("\nX, please choose row number with in the size"))
    x_col = int(input("\nX, please choose col wihtin the size"))
    b.update_cell(x_row, x_col, "X")

    refresh()
    # get x input
    o_row = int(input("\nO, please choose row number with in the size"))
    o_col = int(input("\nO, please choose col number wihtin the size"))
    b.update_cell(o_row, o_col, "O")
