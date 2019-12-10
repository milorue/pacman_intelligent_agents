from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom, HumanPacman, PacmanGreedy
from pacman.ghost_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *
from turtle import Terminator as Terminator
import math
import csv

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

def generate_pacman(board_in):
    pacman_types = ['PacmanBetterRandom', 'PacmanGreedy']
    pacman_agent_type = choice(pacman_types)
    if pacman_agent_type == 'PacmanBetterRandom':
        pacman_agent = PacmanBetterRandom(position, direction, board_in)
    else:
        pacman_agent = PacmanGreedy(position, direction, board_in)
    return pacman_agent

def generate_ghosts(pacman_in, board_in):
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

def export_data(data_dict):
    csv_file_label = 'data' + datetime.now().strftime("%Y%M%d%H%M%S") + ".csv"
    csv_columns = data_dict[0].keys()

    with open(csv_file_label, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in data_dict:
            writer.writerow(data)

def collect_data(num_simulations):
    data_all = []
    for i in range(num_simulations):
        data_round = {}
        start = datetime.now()
        game_board = deepcopy(board)
        game_pacman = deepcopy(generate_pacman(game_board))
        game_ghosts = deepcopy(generate_ghosts(game_pacman, game_board))
        game = PacmanGame(game_board, game_pacman, game_ghosts, frame_rate=1)
        try:
            game.game_setup()
        except SystemExit:
            data_round['score'] = int(game.state['score'])
            data_round['length'] = str(datetime.now() - start)
            data_round['frame_rate'] = int(game.frame_rate)
            data_round['pacman_pos_x'] = int(game.pacman.x)
            data_round['pacman_pos_y'] = int(game.pacman.y)
            data_round['pacman_type'] = str(game.pacman.__class__.__name__)
            for ghost in game.ghosts:
                index = str(game.ghosts.index(ghost) + 1)
                label = "ghost" + index + "_pos_x"
                data_round[label] = int(ghost.x)
                label = "ghost" + index + "_pos_y"
                data_round[label] = int(ghost.y)
                label = "ghost" + index + "_euc_disp"
                data_round[label] = float(math.sqrt(((game.pacman.x - ghost.x) / 20.0)**2 + ((game.pacman.y - ghost.y) / 20.0)**2))
                label = "ghost" + index + "_x_tile_disp"
                data_round[label] = int((game.pacman.x - ghost.x) / 20)
                label = "ghost" + index + "_y_tile_disp"
                data_round[label] = int((game.pacman.y - ghost.y) / 20)
                label = "ghost" + index + "_type"
                data_round[label] = str(ghost.__class__.__name__)
            data_all.append(data_round)
            print("Trial", str(i + 1) + ":", data_all[-1])
        except Terminator:
            raise SystemError
    print(len(data_all))
    export_data(data_all)

def main():
    collect_data(10)

main()
