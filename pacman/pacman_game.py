"""Code was pulled and modified from free-python-games written by Grant Jenks under an Apache License"""

from random import choice
from turtle import *
from freegames import floor, vector
from pacman.pacman_agents import PacmanRandom
from datetime import *
from pacman.pathing_functions import *

class PacmanGame:
    def __init__(self, board, pacman, ghosts):
        self.state = {'score': 0}
        self.board = board  # defines the board takes a array
        self.pacman = pacman  # defines location of pacman and initializes him
        self.ghosts = ghosts  # defines the locations and faces of ghosts

        self.pac_pos = self.pacman.pos
        self.ghost_positions = []

        for ghost in self.ghosts:
            self.ghost_positions.append(ghost.pos)

        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.aim = vector(0, -5)
        # self.going = self.pacman + self.aim

        self.powerTimer = 30
        self.ghostTimer = 0

    def build_board(self, x, y):  # replaces square function
        self.path.up()
        self.path.goto(x, y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)

        self.path.end_fill()

    def draw_world(self):  # replaces world function
        bgcolor('blue')  # background color
        self.path.color('black')  # path color

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
        return self.pacman

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
        if self.board.valid_move(self.pac_pos + direction):
            self.pac_pos.move(direction)  # our copy of the agent moves in the board
            newPos = self.board.determine_teleports(self.pac_pos)
            self.pac_pos = newPos
            self.pacman.update(self.pac_pos)  # we update the agent where the board let it go
            self.board.update_pacman(newPos)

        position = get_offset(self.pacman.pos)  # pacman's current position
        self.scoring(position)

        self.board.update_pacman(position)

        up()
        goto(self.pac_pos.x + 10, self.pac_pos.y + 10)
        dot(20, 'yellow')

    def move_ghosts(self):
        count = 0
        for ghost in self.ghosts:
            count += 1
            direction = ghost.move()
            new_pos = vector(ghost.pos.x + direction.x, ghost.pos.y + direction.y)
            if self.board.valid_move(ghost.pos + direction):
                ghost.pos = new_pos
                newPos = self.board.determine_teleports(ghost.pos)
                ghost.pos = newPos
                ghost.update(ghost.pos)

            if count == 1:
                up()
                goto(ghost.pos.x + 10, ghost.pos.y + 10) # draws pinky
                dot(20, 'pink')
            elif count == 2:
                up()
                goto(ghost.pos.x + 10, ghost.pos.y + 10)
                dot(20, 'orange')
            elif count == 3:
                up()
                goto(ghost.pos.x + 10, ghost.pos.y + 10)
                dot(20, 'light blue')
            else:
                up()
                goto(ghost.pos.x + 10, ghost.pos.y + 10)
                dot(20, 'red')

        self.board.update_ghosts(self.ghosts)

        for ghost in self.ghosts:
            self.ghost_positions.append(ghost.pos)

    def run_game(self):
        self.end = datetime.now()
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
            if abs(self.pac_pos - ghost.pos) < 20 or self.state.get('score') == 160:
                self.kill_pacman(self.pac_pos, ghost.pos)
                self.path.clear() # clears the path maker
                self.writer.clear() # clears the score from the window
                raise SystemExit # causes the program to "terminate" (temporary fix so the simulation automatically closes the display and allows the program to continue)
                return

        ontimer(self.run_game, 1)  # loops make_moves at 80fps
        # while not self.is_finish:
        #     self.run_game()

    def game_setup(self):
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        self.writer.goto(160, 160)
        self.writer.color('white')
        self.writer.write(self.state['score'])
        listen()
        # input setup (remove when AI)
        # onkey(lambda: self.move(5, 0), 'Right')
        # onkey(lambda: self.move(-5, 0), 'Left')
        # onkey(lambda: self.move(0, 5), 'Up')
        # onkey(lambda: self.move(0, -5), 'Down')
        self.draw_world()
        self.run_game()
        done()