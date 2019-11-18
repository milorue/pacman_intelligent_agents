"""Code was pulled and modified from free-python-games written by Grant Jenks under an Apache License"""

from random import choice
from turtle import *
from freegames import floor, vector
from pacman.pacman_agents import PacmanRandom


class PacmanGame:
    def __init__(self, board, pacman, ghosts):
        self.state = {'score': 0}
        self.board = board  # defines the board takes a array
        self.pacman = pacman  # defines location of pacman and initializes him
        self.ghosts = ghosts  # defines the locations and faces of ghosts

        self.pacman_object = vector(self.pacman.x, self.pacman.y)
        self.ghosts_objecst = []

        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.aim = vector(0, -5)
        # self.going = self.pacman + self.aim

    def build_board(self, x, y):  # replaces square function
        self.path.up()
        self.path.goto(x,y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)

        self.path.end_fill()

    def draw_world(self):  # replaces world function
        bgcolor('black')  # background color
        self.path.color('blue')  # path color

        for index in range(len(self.board.tiles)):  # loops through board array to draw
            tile = self.board.tiles[index]

            if tile > 0:  # builds walls
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.build_board(x, y)

                if tile == 1:  # builds paths
                    self.path.up()
                    self.path.goto(x + 10, y + 10)
                    self.path.dot(2, 'white')  # creates pellets

    def get_pacman(self):
        return self.pacman.agent

    def get_ghost(self, ghost_num):
        return self.ghosts[ghost_num]

    def move(self, x, y):  # any change in movement direction is handled here
        if self.board.valid_move(self.pacman.agent + vector(x, y)):
            self.aim.x = x
            self.aim.y = y

    def scoring(self, position):  # pellet collection function
        if self.board.tiles[position] == 1:
            self.board.tiles[position] = 2
            self.state['score'] += 1
            x = (position % 20) * 20 - 200
            y = 180 - (position // 20) * 20
            self.build_board(x, y)

    def kill_pacman(self, pacman, point):
        if abs(pacman - point) < 20:
            return  # exit case
        else:
            pass

    def move_pacman(self):

        direction = self.pacman.move() # get agents direction it intends to go
        if self.board.valid_move(self.pacman_object + direction):
            self.pacman_object.move(direction)  # our copy of the agent moves in the board
            self.pacman.update(self.pacman_object)  # we update the agent where the board let it go

        position = self.board.get_offset(self.pacman_object)  # pacman's current position
        self.scoring(position)

        up()
        goto(self.pacman_object.x + 10, self.pacman_object.y + 10)
        dot(20, 'yellow')

    def move_ghosts(self):
        for ghost in self.ghosts:
            direction = ghost.send_move_to_board()
            ghost.move(self.board.valid_move(ghost.agent + direction))  # validates the move

            up()
            goto(ghost.agent.x + 10, ghost.agent.y + 10)
            dot(20, 'red')

    def run_game(self):
        self.writer.undo()
        self.writer.write(self.state['score'])

        clear()

        # valid moves array

        options = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10),
        ]

        movement = choice(options)

        self.move_pacman()
        self.move_ghosts()

        update()  # updates the board

        for ghost in self.ghosts:  # kill pacman function
            if abs(self.pacman_object - ghost.agent) < 20:
                return

        ontimer(self.run_game, 100)  # loops make_moves at 80fps

    def game_setup(self):
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        self.writer.goto(160, 160)
        self.writer.color('white')
        self.writer.write(self.state['score'])
        listen()
        # input setup (remove when AI)
        onkey(lambda: self.move(5, 0), 'Right')
        onkey(lambda: self.move(-5, 0), 'Left')
        onkey(lambda: self.move(0, 5), 'Up')
        onkey(lambda: self.move(0, -5), 'Down')
        self.draw_world()
        self.run_game()
        done()
