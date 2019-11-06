from random import choice
from turtle import *
from freegames import floor, vector


class pacman_board:
    def __init__(self, board, pacman, ghosts):
        self.board = board  # defines the board takes a array
        self.pacman = pacman  # defines location of pacman and initializes him
        self.ghosts = ghosts  # defines the locations and faces of ghosts

        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.aim = vector(0, -5)

    def build_board(self, x, y):
        self.path.up()
        self.path.goto(x,y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)

        self.path.end_fill()

    def get_offset(self, point):
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index  # returns the offset within the board (for UI purposes)



