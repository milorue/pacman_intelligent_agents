import collections
import heapq

import numpy as np
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


class GhostAStar:
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

        branch = a_star(self.board, obj, self.board.get_pacman())
        try:
            self.direction = branch[1]-branch[0]
        except:
            return self.direction
        return self.direction

    def update(self, new_location):
        self.x = new_location.x
        self.y = new_location.y

    def get_position(self):
        return self.board.make_vec(self.x, self.y)


class AStarNode:
    def __init__(self, parent, position, distance_from_start, goal):
        self.parent = parent
        self.position = position
        self.distance_from_start = distance_from_start
        self.cost = sum(np.absolute(np.subtract(goal, position))) + distance_from_start

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __ne__(self, other):
        return self.cost != other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __repr__(self):
        string = "Position: " + str(self.position) + "\n"
        string += "distance_from_start: " + str(self.distance_from_start) + "\n"
        string += "Cost: " + str(self.cost) + "\n"
        return string


def a_star(board, start_point, pacman):
    """
    :param start_point: Where you want the path to start
    :param a_map: a map to analyze, not change
    :return: a list of positions (x, y) that are the suggested path from current position to a goal
    """

    # initialize current position, root, and list of visited positions
    visited_positions = set()
    visited_positions.add(start_point)
    heap = []
    node = AStarNode(None, start_point, 0, pacman)
    heapq.heappush(heap, node)
    while node.position != pacman and heap:

        node = heapq.heappop(heap)
        visited_positions.add(node.position)
        for move in board.moves_from(node.position):
            position = node.position + move
            if position not in visited_positions:
                heapq.heappush(heap, AStarNode(node, position, node.distance_from_start + 1, pacman))

    branch = collections.deque([])

    while node is not None:
        branch.append(node.position)
        node = node.parent

    branch.reverse()

    return branch
