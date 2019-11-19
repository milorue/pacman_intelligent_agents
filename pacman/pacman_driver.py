from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom
from pacman.ghost_agents import GhostRandom
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard

position = vector(-40, -80)
direction = vector(0, -5)

board = PacmanBoard(deepcopy(tiles))

pacman = PacmanRandom(position, direction, board)
pacmanBetter = PacmanBetterRandom(position, direction, board)


ghost = vector(-180, 160)
ghostDir = vector(10, 0)

ghosty = GhostRandom(ghost, ghostDir, deepcopy(tiles))
ghostz = [ghosty]

game = PacmanGame(board, deepcopy(pacmanBetter), deepcopy(ghostz))
game.game_setup()

