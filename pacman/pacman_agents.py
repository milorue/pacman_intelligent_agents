from freegames import floor, vector
from random import choice, randint


class PacmanRandom:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y
        self.moves = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10)
        ]

    def move(self, valid):
        if valid:
            return True
        else:
            self.choose_direction()

    def choose_direction(self):
        self.direction = choice(self.moves)

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y


class PacmanBetterRandom:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y
        self.moves = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10)
        ]

    def move(self, valid):
        if valid:
            return True
        else:
            self.choose_move()


    # def choose_move(self):
    #
    #
    # def all_valid(self, position):
    #     for i in self.moves:




