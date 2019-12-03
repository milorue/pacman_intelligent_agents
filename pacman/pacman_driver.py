from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom, HumanPacman
from pacman.ghost_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *
from turtle import Terminator

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

blinky = GhostAStar(ghost, ghostDir, board, pacman)
pinky = GhostBetter(ghost2, ghostDir1, board, pacman)
inky = GhostBetter(ghost3, ghostDir2, board, pacman)
clide = GhostBetter(ghost4, ghostDir3, board, pacman)

bae = GhostRandom(ghost, ghostDir, board)
bae1 = GhostRandom(ghost2, ghostDir1, board)
bae2 = GhostRandom(ghost3, ghostDir2, board)
bae3 = GhostRandom(ghost4, ghostDir3, board)


ghostz = [blinky, pinky, inky, clide]
badGhosts = [bae, bae1, bae2, bae3]

def collect_data(num_simulations):
    data_all = []
    for i in range(num_simulations):
        data_round = {}
        start = datetime.now()
        game = PacmanGame(board, deepcopy(pacmanBetter), deepcopy(ghostz))
        try:
            game.game_setup()
        except SystemExit:
            data_round['score'] = game.state['score']
            data_round['length'] = str(datetime.now() - start)
            data_all.append(data_round)
        print(data_round)
    print("Simulations:", len(data_all))

def main():
    collect_data(100)

main()
