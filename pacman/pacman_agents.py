from freegames import floor, vector
from pacman.pathing_functions import *


class AbstractPacman:
    def __init__(self, board, location):
        self.board = board
        self.pos = location
        self.direction = choice(board.moves_from(location))
        self.moves = [  # speed
            vector(10, 0),  # right
            vector(-10, 0),  # left
            vector(0, 10),  # up
            vector(0, -10)  # down
        ]

    def move(self):
        pass

    def update(self, new_location):
        self.pos = new_location


class PacmanRandom(AbstractPacman):
    def move(self):
        self.direction = choice(self.board.pacman_moves(self.pos))
        return self.direction

class SmartPacman(AbstractPacman):
    def __init__(self, board, location):
        super().__init__(board, location)

        self.count = 0
        #put the other shit you need here

    def move(self):


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
        # print(moves)
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

    def get_position(self):
        return self.board.make_vec(self.x, self.y)

    def update_ghosts(self, ghosts):
        pass


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

    def get_position(self):
        return self.board.make_vec(self.x, self.y)

    def update_ghosts(self, ghosts):
        pass


class PacmanGreedy:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y

        self.goal = choice(self.board.valid_locations())

        self.valid_moves_count = 0
        self.count = 0


    def move(self):
        obj = self.board.make_vec(self.x, self.y)
        if self.count == 0:
            self.goal = choice(self.board.valid_locations())

        self.count += 1

        if obj == self.goal:
            self.goal = choice(self.board.valid_locations())

        else:
            branch = a_star(self.board, obj, self.goal)
            try:
                self.direction = branch[1] - branch[0]
            except:
                return self.direction
            return self.direction

        return self.direction

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y

    def update_ghosts(self, ghosts):
        pass


class OldSmartPacman:
    def __init__(self, vec, direction, board, ghosts):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y
        self.ghosts = ghosts

        self.goal = choice(self.board.valid_locations())

        self.count = 0

        self.timer = 0

        self.proposed_location = board.make_vec(self.x, self.y)

        self.minDist = 30


    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y

    def update_ghosts(self, ghosts):
        self.ghosts = ghosts

    def distances_from_ghosts(self, position):
        distances = []
        for ghost in self.ghosts:
            x_disp = abs(int(position.x - ghost.x))
            y_disp = abs(int(position.y - ghost.y))
            disp = int((x_disp + y_disp) / 20)
            distances.append(disp)

        return distances


class SimpleSmartPacman:
    def __init__(self, vec, direction, board, ghosts):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y
        self.ghosts = ghosts

        self.goal = choice(self.board.valid_locations())

        self.count = 0

        self.timer = 0

    def move(self):
        obj = self.board.make_vec(self.x, self.y)
        moves = self.board.pacman_moves(obj)

        dist = self.distances_from_ghosts(obj)

        small = min(dist)

        for move in moves:
            new_location = obj + move
            distances = self.distances_from_ghosts(new_location)
            smallest = min(distances)
            if smallest < small:
                pass
            if smallest >= small:
                return move
            else:
                pass
        return choice(move)

    def update_ghosts(self, ghosts):
        self.ghosts = ghosts

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y

    def distances_from_ghosts(self, position):
        distances = []
        for ghost in self.ghosts:
            x_disp = abs(int(position.x - ghost.x))
            y_disp = abs(int(position.y - ghost.y))
            disp = int((x_disp + y_disp) / 20)
            distances.append(disp)

        return distances