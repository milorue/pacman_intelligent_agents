from freegames import floor, vector
from random import choice
from pacman.pathing_functions import *


class AbstractGhost:
    def __init__(self, board, location):
        self.board = board
        self.pos = location
        self.direction = choice(board.moves_from(location))
        self.moves = [  # speed
            vector(5, 0),  # right
            vector(-5, 0),  # left
            vector(0, 5),  # up
            vector(0, -5)  # down
        ]

    def move(self):
        pass

    def update(self, new_location):
        self.pos = new_location


class GhostBetter(AbstractGhost):
    def move(self):
        if self.board.valid_move(self.pos + self.direction):
            pass
        else:
            self.direction = choice(self.board.moves_from(self.pos))
        return self.direction


class GhostPinky(AbstractGhost):
    def __init__(self, board, location):
        super().__init__(board, location)
        self.timer = 30

    def move(self):

        while self.timer >= 0:
            self.timer -= 1
            return vector(0, -10)

        valid = self.board.moves_from(self.pos)

        if len(valid) >= 3 or self.pos in self.board.get_decision_points():
            branch = a_star(self.board, self.pos, self.board.pacman + self.pos * 3)
            try:
                self.direction = branch[1] - branch[0]
            except IndexError:
                return self.direction
            return self.direction
        else:
            return self.direction

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y

    def get_position(self):
        return self.board.make_vec(self.x, self.y)


class GhostAStarWithScatter:
    def __init__(self, vec, direction, board, pacman):
        self.board = board
        self.direction = direction
        self.pacmanPos = pacman
        self.x = vec.x
        self.y = vec.y
        self.timer = 0

        self.waitTimer = 60

        self.valid_moves_count = 0

    def update_pacman(self, pacman, pacmanDir):
        self.pacmanPos = pacman
        self.pacmanDir = pacmanDir

    def move(self):
        self.timer += 1
        obj = self.board.make_vec(self.x, self.y)

        while self.waitTimer >= 0:
            self.waitTimer -= 1
            return vector(0, 10)

        if self.timer >= 5:
            homebases = [
                vector(-180, 160),
                vector(-180, -160),
                vector(100, 160),
                vector(100, -160)
            ]

            if self.timer == 10:
                self.timer = 0

            valid = self.board.moves_from(obj)
            invalid = self.board.invalid_moves_from(obj)
            if len(valid) >= 3 or obj in self.board.get_decision_points():
                branch = a_star(self.board, obj, choice(homebases))
                try:
                    self.direction = branch[1] - branch[0]

                except:
                    return self.direction
                return self.direction

            else:
                return self.direction

        else:
            valid = self.board.moves_from(obj)
            invalid = self.board.invalid_moves_from(obj)
            if len(valid) >= 3:
                branch = a_star(self.board, obj, self.pacmanPos)
                try:
                    self.direction = branch[1] - branch[0]
                except:
                    return self.direction
                return self.direction

            elif len(invalid) >= 2 and len(valid) >= 2:
                branch = a_star(self.board, obj, self.pacmanPos)
                try:
                    self.direction = branch[1] - branch[0]
                except:
                    return self.direction
                return self.direction
            else:
                return self.direction

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y

    def get_position(self):
        return self.board.make_vec(self.x, self.y)


class GhostAStar(AbstractGhost):
    def move(self):
        branch = a_star(self.board, self.pos, self.board.pacman.pos)
        try:
            self.direction = branch[1] - branch[0]
        except IndexError:
            pass
        return self.direction


class GhostProjAStar(AbstractGhost):
    '''
    Gives a non-deterministic location for where an entity will be after a specific distance.
    '''

    def move(self):
        pac_pos = self.board.pacman.pos
        pac_dir = self.board.pacman.direction
        diff = self.pos - pac_pos
        distance = abs(diff[0]) + abs(diff[1])
        pac_proj = forward_proj(self.board, pac_pos, pac_dir, round(distance / 2))
        branch = a_star(self.board, self.pos, pac_proj)

        try:
            self.direction = branch[1] - branch[0]
        except IndexError:
            pass
        return self.direction


class GhostRandom:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y
        self.moves = [  # speed
            vector(10, 0),  # right
            vector(-10, 0),  # left
            vector(0, 10),  # up
            vector(0, -10)  # down
        ]

        self.valid_moves_count = 0

    def move(self):
        position = self.board.make_vec(self.x, self.y)
        self.choose_move()
        return self.direction

    def choose_move(self):
        moves = self.all_valid(self.board.make_vec(self.x, self.y))
        self.direction = choice(moves)

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
