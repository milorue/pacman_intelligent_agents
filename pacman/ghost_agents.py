from freegames import floor, vector
from random import choice


class GhostRandom:
    def __init__(self, agent, direction, board):
        self.board = board
        print(board)
        self.direction = direction
        self.agent = agent
        self.moves = [
            vector(10, 0),  # right
            vector(-10, 0),  # left
            vector(0, 10),  # up
            vector(0, -10)  # down
        ]

    def choose_move(self):
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

    def check_move_on_board(self, move):
        move_located = self.determine_board_pos(move)

        if self.board[move_located] == 0:
            return False

        move_located = self.determine_board_pos(move + 19)

        if self.board[move_located] == 0:
            return False

        return move.x % 20 == 0 or move.y % 20 == 0