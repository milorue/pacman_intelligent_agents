from freegames import floor, vector
from random import choice


class GhostRandom:
    def __init__(self, agent, direction, board):
        self.board = board
        self.direction = direction
        self.agent = agent
        self.moves = [
            vector(10, 0),  # right
            vector(-10, 0),  # left
            vector(0, 10),  # up
            vector(0, -10)  # down
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

    def determine_board_pos(self, point):  # static method for check_move
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        board_pos = int(x + y * 20)
        return board_pos