from freegames import floor, vector
from random import choice, randint
from turtle import *
import time


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
            self.choose_move()

    def choose_move(self):
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

        self.valid_moves_count = 0

    def move(self):
        position = self.board.make_vec(self.x, self.y)
        if self.board.valid_move(position + self.direction) and self.valid_moves_count < 3:
            # time.sleep(5)
            self.choose_move()
            return self.direction
        else:
            self.choose_move()
            return self.direction


    def choose_move(self):
        moves = self.all_valid(vector(self.x, self.y))
        print(moves)
        self.direction = choice(moves)


    def all_valid(self, position):
        valid_moves = []
        for i in self.moves:
            if self.board.valid_move(position + i):
                valid_moves.append(i)
        self.valid_moves_count = len(valid_moves)

        return valid_moves

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y


class HumanPacman:
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

        self.valid_moves_count = 0

    def move(self):
        onkey(lambda: self.choose_move(10, 0), 'Right')
        onkey(lambda: self.choose_move(-10, 0), 'Left')
        onkey(lambda: self.choose_move(0, 10), 'Up')
        onkey(lambda: self.choose_move(0, -10), 'Down')

        return self.direction

    def choose_move(self, x, y):
        move = vector(x,y)
        position = self.board.make_vec(self.x, self.y)
        if self.board.valid_move(position + move):
            self.direction = move
        else:
            pass


    def all_valid(self, position):
        valid_moves = []
        for i in self.moves:
            if self.board.valid_move(position + i):
                valid_moves.append(i)
        self.valid_moves_count = len(valid_moves)

        return valid_moves

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y
