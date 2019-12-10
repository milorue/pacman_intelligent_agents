from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom, HumanPacman, PacmanGreedy
from pacman.ghost_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *
import math
import csv
import itertools

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

def generate_ghosts(pacman_in, board_in, num_ghosts=4):
    game_board = deepcopy(board_in)
    locations = [ghost, ghost2, ghost3, ghost4]
    directions = [ghostDir, ghostDir1, ghostDir2, ghostDir3]
    ghost_agent_types = ['GhostAStar', 'GhostBetter', 'GhostPinky','GhostAStarWithScatter']
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
        game_pacman = deepcopy(generate_pacman(game_board))
        game_ghosts = deepcopy(generate_ghosts(game_pacman, game_board))
        game = PacmanGame(game_board, game_pacman, game_ghosts, frame_rate=10)
        try:
            start = datetime.now()
            game.game_setup()
        except SystemExit:
            data_round = extract_game_data(game, start)
            data_all.append(data_round)
            print(i + 1, ":", data_round)
    print(len(data_all))
    export_data(data_all)

def extract_game_data(game_in, start):
    data_round = {}
    time_length = datetime.now() - start
    data_round['score'] = int(game_in.state['score'])
    data_round['length'] = str(time_length)
    data_round['length_seconds'] = time_length.total_seconds()
    data_round['frame_rate'] = int(game_in.frame_rate)
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

def collect_structured_data(num_simulations):
    pacman_position = vector(-40, -80)
    pacman_direction = vector(0, -5)
    ghost_locations = [deepcopy(ghost), deepcopy(ghost2), deepcopy(ghost3), deepcopy(ghost4)]
    ghost_directions = [deepcopy(ghostDir), deepcopy(ghostDir1), deepcopy(ghostDir2), deepcopy(ghostDir3)]
    game_counter = 0
    for sim_num in range(num_simulations):
        data_all = []
        print("dataset size before:", len(data_all))
        game_board = deepcopy(board)

        # creates pacman possibilities
        pacman_type_1 = PacmanBetterRandom(deepcopy(pacman_position), deepcopy(pacman_direction), game_board)
        pacman_type_2 = PacmanGreedy(deepcopy(pacman_position), deepcopy(pacman_direction), game_board)
        
        ghost_possibilities = [
            GhostBetter(vector(0,0), vector(0,0), game_board, pacman_type_1),
            GhostAStar(vector(0,0), vector(0,0), game_board, pacman_type_1),
            GhostAStarWithScatter(vector(0,0), vector(0,0), game_board, pacman_type_1),
            GhostPinky(vector(0,0), vector(0,0), game_board, pacman_type_1)
        ]

        # calculates all possible ghost type scenarios for pacman 1
        possibilities_size = len(ghost_possibilities)
        ghost_tuples = list(itertools.product(range(possibilities_size), repeat=4))
        ghost_lists = []
        for tuple in ghost_tuples:
            ghost_lists.append([])
            tuple_list = list(tuple)
            for i in range(len(tuple_list)):
                # modifies ghost
                game_ghost = deepcopy(ghost_possibilities[tuple_list[i]])
                game_ghost.x = ghost_locations[i].x
                game_ghost.y = ghost_locations[i].y
                game_ghost.direction = ghost_directions[i]
                ghost_lists[-1].append(game_ghost)

        # simulation for each generated ghost scenario
        for ghost_scenario in ghost_lists:
            # resets game board
            game_board_item = deepcopy(game_board)

            # resets some ghost properties (necessary for game mechanics)
            for ghost_item in ghost_scenario:
                try:
                    ghost_item.board = game_board_item
                    ghost_item.pacmanPos = pacman_type_1
                except:
                    pass

            # plays game with pacman agent 1
            pacman_game_1 = PacmanGame(game_board_item, deepcopy(pacman_type_1), deepcopy(ghost_scenario), frame_rate=10)
            try:
                start = datetime.now()
                pacman_game_1.game_setup()
            except SystemExit:
                game_counter = game_counter + 1
                data_round = extract_game_data(pacman_game_1, start)
                data_all.append(data_round)
                print("Game",game_counter,"Trial Set", str(sim_num + 1) + ":", datetime.now(),"\n",data_round)

            # resets game board
            game_board_item = deepcopy(game_board)
            # resets ghost properties (necessary for game mechanics)
            for ghost_item in ghost_scenario:
                try:
                    ghost_item.board = game_board_item
                    ghost_item.pacmanPos = pacman_type_2
                except:
                    pass

            # plays game with pacman agent 2
            pacman_game_2 = PacmanGame(game_board_item, deepcopy(pacman_type_2), deepcopy(ghost_scenario), frame_rate=10)
            try:
                start = datetime.now()
                pacman_game_2.game_setup()
            except SystemExit:
                game_counter = game_counter + 1
                data_round = extract_game_data(pacman_game_2, start)
                data_all.append(data_round)
                print("Game", game_counter, "Trial Set", str(sim_num + 1) + ":", datetime.now(), "\n", data_round)
            file_label = str(sim_num + 1) + "-" + 'data' + datetime.now().strftime("%Y%m%d%H%M%S") + ".csv"
        game_counter = 0
        print("dataset size after:", len(data_all))
        export_data(data_all, file_label=file_label)

def main():
    collect_random_data(10)
    collect_structured_data(1)

main()
