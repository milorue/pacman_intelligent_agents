from freegames import floor, vector
from random import choice


class GhostRandom:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y
        self.moves = [  # speed
            vector(7.5, 0),  # right
            vector(-7.5, 0),  # left
            vector(0, 7.5),  # up
            vector(0, -7.5)  # down
        ]

        self.valid_moves_count = 0

    def move(self):
        position = self.board.make_vec(self.x, self.y)
        self.choose_move()
        return self.direction


    def choose_move(self):
        moves = self.all_valid(self.board.make_vec(self.x, self.y))
        self.direction = choice(moves)

    def determine_board_pos(self, point):  # static method for check_move
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        board_pos = int(x + y * 20)
        return board_pos

    def all_valid(self, position):
        valid_moves = []  # resets on each position
        for i in self.moves:
            if self.board.valid_move(position + i):
                valid_moves.append(i)
        self.valid_moves_count = len(valid_moves)

        return valid_moves

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y
