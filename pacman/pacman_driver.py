from pacman.ghost_agents import *
from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *
import math
import csv
import itertools

position = vector(-40, -80)
direction = vector(0, -5)

ghost = vector(-180, 160)
ghost2 = vector(-180, -160)
ghost3 = vector(100, 160)
ghost4 = vector(100, -160)
ghostDir = vector(5, 0)
ghostDir1 = vector(0, 5)
ghostDir2 = vector(0, -5)
ghostDir3 = vector(-5, 0)

ghostList = [ghost, ghost2, ghost3, ghost4]

board = PacmanBoard(deepcopy(tiles), deepcopy(position), deepcopy(ghostList))

pacman = PacmanRandom(position, direction, board)
pacmanBetter = PacmanBetterRandom(position, direction, board)
human = HumanPacman(position, direction, board)
pacmanGreedy = PacmanGreedy(position, direction, board)
pacmanSmart = SmartPacman(position, direction, board, ghostList)
pacmanSimple = SimpleSmartPacman(position, direction, board, ghostList)

blinky = GhostAStar(ghost, ghostDir, board, pacmanBetter)
pinky = GhostAStarWithScatter(ghost2, ghostDir1, board, pacmanBetter)
inky = GhostPinky(ghost3, ghostDir2, board, pacmanBetter)
clide = GhostBetter(ghost4, ghostDir3, board, pacmanBetter)

ghostFollow1 = GhostRandomFollow(ghost, ghostDir, board, pacmanBetter)
ghostFollow2 = GhostRandomFollow(ghost2, ghostDir1, board, pacmanBetter)
ghostFollow3 = GhostRandomFollow(ghost3, ghostDir2, board, pacmanBetter)
ghostFollow4 = GhostRandomFollow(ghost4, ghostDir3, board, pacmanBetter)

bae = GhostRandom(ghost, ghostDir, board)
bae1 = GhostRandom(ghost2, ghostDir1, board)
bae2 = GhostRandom(ghost3, ghostDir2, board)
bae3 = GhostRandom(ghost4, ghostDir3, board)

ghostz = [blinky, pinky, inky, clide]
badGhosts = [bae, bae1, bae2, bae3]
trails = [ghostFollow1, ghostFollow2, ghostFollow3, ghostFollow4]


def generate_pacman(board_in):
    pacman_types = ['PacmanBetterRandom', 'PacmanGreedy', 'SmartPacman']
    pacman_agent_type = choice(pacman_types)
    if pacman_agent_type == 'PacmanBetterRandom':
        pacman_agent = PacmanBetterRandom(position, direction, board_in)
    elif pacman_agent_type == 'SmartPacman':
        pacman_agent = SmartPacman(position, direction, board_in, [])
    else:
        pacman_agent = PacmanGreedy(position, direction, board_in)
    return pacman_agent

def generate_ghosts(pacman_in, board_in, num_ghosts=4):
    game_board = deepcopy(board_in)
    locations = [ghost, ghost2, ghost3, ghost4]
    directions = [ghostDir, ghostDir1, ghostDir2, ghostDir3]
    ghost_agent_types = ['GhostAStar', 'GhostBetter', 'GhostPinky', 'GhostAStarWithScatter']
    ghost_agents = []
    for num in range(num_ghosts):
        place = locations[num % len(locations)]
        ghost_dir = choice(directions)
        ghost_type = choice(ghost_agent_types)
        if ghost_type == 'GhostAStar':
            game_ghost = GhostAStar(place, ghost_dir, game_board, pacman_in)
        elif ghost_type == 'GhostPinky':
            game_ghost = GhostPinky(place, ghost_dir, game_board, pacman_in)
        elif ghost_type == 'GhostAStarWithScatter':
            game_ghost = GhostAStarWithScatter(place, ghost_dir, game_board, pacman_in)
        else:
            game_ghost = GhostBetter(place, ghost_dir, game_board, pacman_in)
        ghost_agents.append(game_ghost)
    return ghost_agents

def export_data(data_dict, file_label=str('data' + datetime.now().strftime("%Y%m%d%H%M%S") + ".csv")):
    csv_file_label = file_label
    csv_columns = data_dict[0].keys()

    with open(csv_file_label, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in data_dict:
            writer.writerow(data)

def collect_random_data(num_simulations):
    data_all = []
    for i in range(num_simulations):
        data_round = {}
        game_board = deepcopy(board)

        # game_pacman = deepcopy(generate_pacman(game_board))
        game_pacman = deepcopy(pacmanSmart)
        game_ghosts = deepcopy(trails)
      
        game = PacmanGame(game_board, game_pacman, game_ghosts)
        try:
            start = datetime.now()
            game.game_setup()
        except SystemExit:
            data_round = extract_game_data(game, start)
            data_all.append(data_round)
            print(i + 1, ":", data_round)
    print(len(data_all))
    export_data(data_all)

def collect_data(num_simulations, num_iterations):
    for h in range(num_iterations):
        data_all = []
        for i in range(num_simulations):

            data_round = {}
            game_board = deepcopy(board)

            pacman1 = PacmanBetterRandom(position, direction, game_board)

            game_ghosts_general = generate_ghosts(pacman1, game_board)

            game_ghosts1 = deepcopy(game_ghosts_general)
            for ghost in game_ghosts1:
                ghost.pacmanPos = pacman1
            game1 = PacmanGame(deepcopy(game_board), pacman1, game_ghosts1)
            try:
                start = datetime.now()
                game1.game_setup()
            except SystemExit:
                data_round = extract_game_data(game1, start)
                data_all.append(data_round)
                print(i + 1, "-", datetime.now(), ":", data_round)

            pacman2 = PacmanGreedy(position, direction, game_board)
            game_ghosts2 = deepcopy(game_ghosts_general)
            for ghost in game_ghosts2:
                ghost.pacmanPos = pacman2
            game2 = PacmanGame(deepcopy(game_board), pacman2, game_ghosts2)
            try:
                start = datetime.now()
                game2.game_setup()
            except SystemExit:
                data_round = extract_game_data(game2, start)
                data_all.append(data_round)
                print(i + 1, "-", datetime.now(), ":", data_round)

            game_ghosts3 = deepcopy(game_ghosts_general)
            pacman3 = SmartPacman(position, direction, board, game_ghosts3)
            for ghost in game_ghosts3:
                ghost.pacmanPos = pacman3
            game3 = PacmanGame(deepcopy(game_board), pacman3, game_ghosts3)
            try:
                start = datetime.now()
                game3.game_setup()
            except SystemExit:
                data_round = extract_game_data(game3, start)
                data_all.append(data_round)
                print(i + 1, "-", datetime.now(), ":", data_round)

        export_data(data_all)


def extract_game_data(game_in, start):
    data_round = {}
    time_length = datetime.now() - start
    data_round['score'] = int(game_in.state['score'])
    data_round['length'] = str(time_length)
    data_round['length_seconds'] = time_length.total_seconds()
    data_round['pacman_pos_x'] = int(game_in.pacman.x)
    data_round['pacman_pos_y'] = int(game_in.pacman.y)
    data_round['pacman_type'] = str(game_in.pacman.__class__.__name__)
    for ghost_item in game_in.ghosts:
        index = str(game_in.ghosts.index(ghost_item) + 1)
        label = "ghost" + index + "_pos_x"
        data_round[label] = int(ghost_item.x)
        label = "ghost" + index + "_pos_y"
        data_round[label] = int(ghost_item.y)
        label = "ghost" + index + "_euc_disp"
        data_round[label] = float(
            math.sqrt(((game_in.pacman.x - ghost_item.x) / 20.0) ** 2 + (
                        (game_in.pacman.y - ghost_item.y) / 20.0) ** 2))
        label = "ghost" + index + "_x_tile_disp"
        data_round[label] = int((game_in.pacman.x - ghost_item.x) / 20)
        label = "ghost" + index + "_y_tile_disp"
        data_round[label] = int((game_in.pacman.y - ghost_item.y) / 20)
        label = "ghost" + index + "_type"
        data_round[label] = str(ghost_item.__class__.__name__)
    return data_round

def main():
    # collect_random_data(10)
    collect_data(100, 5)

main()
