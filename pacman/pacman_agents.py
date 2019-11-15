from freegames import floor, vector
from random import choice, randint


class PacmanRandom:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.agent = vec
        self.moves = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10)
        ]

    def send_move_to_board(self):
        return self.direction

    def move(self, valid):
        if valid:
            self.agent.move(self.direction)
        else:
            self.choose_direction()

    def choose_direction(self):
        self.direction = choice(self.moves)






