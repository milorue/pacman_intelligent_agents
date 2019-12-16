import collections
import heapq
from random import choice


class AStarNode:
    def __init__(self, parent, position, distance_from_start, goal):
        self.parent = parent
        self.position = position
        self.distance_from_start = distance_from_start
        diff = goal - position
        dist = abs(diff[0]) + abs(diff[1])
        self.cost = dist + distance_from_start

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


def a_star(board, start_point, end_point):
    """
    :param board: the pacman board which is being searched on
    :param start_point: Where you want the path to start
    :param end_point: a map to analyze, not change
    :return: a list of positions (x, y) that are the suggested path from current position to a goal
    """

    # initialize current position, root, and list of visited positions
    visited_positions = set()
    visited_positions.add(start_point)
    heap = []
    node = AStarNode(None, start_point, 0, end_point)
    heapq.heappush(heap, node)
    while node.position != end_point and heap:

        node = heapq.heappop(heap)
        visited_positions.add(node.position)
        for move in board.moves_from(node.position):
            position = node.position + move
            if position not in visited_positions:
                heapq.heappush(heap, AStarNode(node, position, node.distance_from_start + 10, end_point))

    branch = collections.deque([])

    while node is not None:
        branch.append(node.position)
        node = node.parent

    branch.reverse()

    return branch


def forward_proj(board, pos, dir, dist):
    print("pos:", pos)
    print("dir:", dir)
    print("dist:", dist)
    while dist > 0:
        moves = board.moves_from(pos)
        if dir not in moves:
            dir = choice(moves)
        pos += dir
        dist -= abs(dir[0]) + abs(dir[1])
    return pos


def proj_move(board, ghost_pos, ghost_dir, pac_pos, pac_dir):

    """
    get ghost position
    get ghost direction
    get pacman position
    get manhattan distance between
    get projected pacman position
    get a* branch between ghost location and projected pacman
    return initial direction of branch
    :return:
    """

    diff = ghost_pos - pac_pos
    distance = abs(diff[0]) + abs(diff[1])
    move = board.moves_from(ghost_pos)[0]
    speed = (abs(move[0]) + abs(move[1])) / 10
    pac_proj = forward_proj(board, pac_pos, pac_dir, round(distance * speed))
    branch = a_star(board, ghost_pos, pac_proj)

    try:
        ghost_dir = branch[1] - branch[0]
    except IndexError:
        pass
    return ghost_dir
