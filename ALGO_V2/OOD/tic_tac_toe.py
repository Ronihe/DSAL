# 1. clear the ambuguity
# board height and width
# player can move around

# 2. core object:


# 3. realtionship btw

class Game:
    def __init__(self):

    def new(self):
        def up(self):
            pass

        def down(self):
            pass

        def left(self):

        def right(self):


class Board:
    def __init__(self):
        self.width = 3
        self.height = 4
        self.board = self.draw()

    def draw(self):
        return [[[0, 0] for i in range(self.width)] for j in range(self.height)]


class Player:







########
from pprint import pprint


class Game:
    def __init__(self):
        # board
        # player
        self.board = Board(8, 8)
        self.player = Player()

    def move(self, direction):
        move_map = {
            "up": (1, 0),
            "down": (-1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        position = self.board.move_token(player, move_map[direction]):
        if position:
            # update player position
            pass


class Board:
    def __init__(self, height=4, width=4):
        self.size = (height, width)
        self.board = self.build_board(self.size)

    def build_board(self, height_width):
        board = []
        for r in range(height_width[0]):
            row = []
            for w in range(height_width[1]):
                row.append(None)

            board.append(row)

        return board

    def print_board(self):
        pprint(self.board)

    def move_token(self, token, move_distance):
        if self._validate_move(token, move_distance):
            # move
            return True

        return False

    def _validate_move(self, token, move_distance):
        y, x = self.size

        x += move_distance[1]
        y += move_distance[0]

        if x < 0 or y < 0:
            return False
        if x >= self.size[1] or y >= self.size[0]:
            return False

        return True


class Token:
    def __init__(self, name):
        self.name = name


class Player(Token):
    def __init__(self):
        super().__init__('Player')
        self.position = (0, 0)
        self.print_player()

    def print_player(self):
        print(self.position)


g = Game()
from pprint import pprint


class Game:
    def __init__(self):
        # board
        # player
        self.board = Board(8, 8)
        self.player = Player()

    def move(self, direction):
        move_map = {
            "up": (1, 0),
            "down": (-1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        position = self.board.move_token(player, move_map[direction]):
        if position:
            # update player position
            pass


class Board:
    def __init__(self, height=4, width=4):
        self.size = (height, width)
        self.board = self.build_board(self.size)

    def build_board(self, height_width):
        board = []
        for r in range(height_width[0]):
            row = []
            for w in range(height_width[1]):
                row.append(None)

            board.append(row)

        return board

    def print_board(self):
        pprint(self.board)

    def move_token(self, token, move_distance):
        if self._validate_move(token, move_distance):
            # move
            return True

        return False

    def _validate_move(self, token, move_distance):
        y, x = self.size

        x += move_distance[1]
        y += move_distance[0]

        if x < 0 or y < 0:
            return False
        if x >= self.size[1] or y >= self.size[0]:
            return False

        return True


class Token:
    def __init__(self, name):
        self.name = name


class Player(Token):
    def __init__(self):
        super().__init__('Player')
        self.position = (0, 0)
        self.print_player()

    def print_player(self):
        print(self.position)


g = Game()
