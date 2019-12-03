from freegames import floor, vector
from random import choice
from queue import PriorityQueue


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

    def determine_board_pos(self, point):  # static method for check_move
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        board_pos = int(x + y * 20)
        return board_pos

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

class GhostBlinky:  # unfinished dev
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
        pass

    def heuristic(self, a, b):
        x1 = a.x
        y1 = a.y
        x2 = b.x
        y2 = b.y
        return abs(x1 - x2) + abs(y1 - y2)

    def search(self, currPos, pacmanPos):
        start = (currPos.x, currPos.y)
        goal = (pacmanPos.x, pacmanPos.y)
        frontier = PriorityQueue()
        frontier.put((start, 0))
        came_from = {}
        cost = {}
        came_from[start] = None
        cost[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in self.board.moves_from(vector(current[0], current[1])):
                new_cost = cost[current] + 10
                priority = new_cost + self.heuristic(pacmanPos, next)
                frontier.put((next.x, next.y), priority)
                came_from[(next.x, next.y)] = current


class GhostBetter:
    def __init__(self, vec, direction, board, pacman):
        self.board = board
        self.direction = direction
        self.pacmanPos = pacman
        self.x = vec.x
        self.y = vec.y
        self.moves = [  # speed
            vector(5, 0),  # right
            vector(-5, 0),  # left
            vector(0, 5),  # up
            vector(0, -5)  # down
        ]

        self.valid_moves_count = 0

    def move(self):
        obj = self.board.make_vec(self.x, self.y)
        valid = self.all_valid(obj)

        if self.board.valid_move(obj + self.direction):
            if len(valid) >= 3:
                self.choose_move()
                return self.direction
            return self.direction

        self.choose_move()
        return self.direction


    def choose_move(self):
        moves = self.all_valid(self.board.make_vec(self.x, self.y))
        self.direction = choice(moves)

    def determine_board_pos(self, point):  # static method for check_move
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        board_pos = int(x + y * 20)
        return board_pos

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

    def get_position(self):
        return self.board.make_vec(self.x, self.y)