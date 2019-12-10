from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom, HumanPacman
from pacman.ghost_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *
import math

position = vector(-40, -80)
direction = vector(0, -5)

board = PacmanBoard(deepcopy(tiles), position)

pacman = PacmanRandom(position, direction, board)
pacmanBetter = PacmanBetterRandom(position, direction, board)
human = HumanPacman(position, direction, board)


ghost = vector(-180, 160)
ghost2 = vector(-180, -160)
ghost3 = vector(100, 160)
ghost4 = vector(100, -160)
ghostDir = vector(5, 0)
ghostDir1 = vector(0, 5)
ghostDir2 = vector(0, -5)
ghostDir3 = vector(-5, 0)

blinky = GhostAStar(ghost, ghostDir, board, pacmanBetter)
pinky = GhostBetter(ghost2, ghostDir1, board, pacmanBetter)
inky = GhostBetter(ghost3, ghostDir2, board, pacmanBetter)
clide = GhostBetter(ghost4, ghostDir3, board, pacmanBetter)

bae = GhostRandom(ghost, ghostDir, board)
bae1 = GhostRandom(ghost2, ghostDir1, board)
bae2 = GhostRandom(ghost3, ghostDir2, board)
bae3 = GhostRandom(ghost4, ghostDir3, board)


ghostz = [blinky, pinky, inky, clide]
badGhosts = [bae, bae1, bae2, bae3]

def generate_ghosts(pacman_in):
    game_board = deepcopy(board)
    locations = [ghost, ghost2, ghost3, ghost4]
    directions = [ghostDir, ghostDir1, ghostDir2, ghostDir3]
    ghost_agent_types = ['GhostAStar', 'GhostBetter']
    ghost_agents = []
    for place in locations:
        ghost_dir = choice(directions)
        ghost_type = choice(ghost_agent_types)
        if ghost_type == 'GhostAStar':
            game_ghost = GhostAStar(place, ghost_dir, game_board, pacman_in)
        else:
            game_ghost = GhostBetter(place, ghost_dir, game_board, pacman_in)
        ghost_agents.append(game_ghost)
    return ghost_agents

def collect_data(num_simulations):
    data_all = []
    for i in range(num_simulations):
        data_round = {}
        start = datetime.now()
        game = PacmanGame(deepcopy(board), deepcopy(pacmanBetter), deepcopy(generate_ghosts(pacmanBetter)))
        try:
            game.game_setup()
        except SystemExit:
            data_round['score'] = game.state['score']
            data_round['length'] = str(datetime.now() - start)
            data_round['pacman_pos'] = vector(game.pacman.x, game.pacman.y)
            data_round['pacman_type'] = game.pacman.__class__.__name__
            for ghost in game.ghosts:
                index = str(game.ghosts.index(ghost) + 1)
                label = "ghost" + index + "_pos"
                data_round[label] = vector(ghost.x, ghost.y)
                label = "ghost" + index + "_dist"
                data_round[label] = math.sqrt(((game.pacman.x - ghost.x) / 20.0)**2 + ((game.pacman.y - ghost.y) / 20.0)**2)
                label = "ghost" + index + "_type"
                data_round[label] = ghost.__class__.__name__
            data_all.append(data_round)
            print(data_all[-1])
    print(len(data_all))

def main():
    collect_data(100)

main()
