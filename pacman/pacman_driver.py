from pacman.pacman_board import PacmanBoard
from pacman.pacman_agents import PacmanRandom
from pacman.ghost_agents import GhostRandom
from copy import deepcopy
from pacman.board_raw import *

position = vector(-40, -80)
direction = vector(0, -5)
pacman = PacmanRandom(position, direction)

ghost = vector(-180,160)
ghostDir = vector(10, 0)

ghosty = GhostRandom(ghost, ghostDir, deepcopy(tiles))
ghostz = [ghosty]

game = PacmanBoard(deepcopy(tiles), deepcopy(pacman), deepcopy(ghostz))
game.game_setup()

