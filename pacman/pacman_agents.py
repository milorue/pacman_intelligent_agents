from freegames import floor, vector
from random import choice, randint
from turtle import *
import time

import collections
import heapq
import numpy as np
from queue import PriorityQueue


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


class PacmanGreedy:
    def __init__(self, vec, direction, board):
        self.board = board
        self.direction = direction
        self.x = vec.x
        self.y = vec.y

        self.goal = choice(self.board.valid_locations())

        self.valid_moves_count = 0

    def move(self):
        obj = self.board.make_vec(self.x, self.y)

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
        for move in board.pacman_moves(node.position):
            position = node.position + move
            if position not in visited_positions:
                heapq.heappush(heap, AStarNode(node, position, node.distance_from_start + 1, pacman))

    branch = collections.deque([])

    while node is not None:
        branch.append(node.position)
        node = node.parent

    branch.reverse()

    return branch
