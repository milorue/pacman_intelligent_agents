from random import choice
from turtle import *
from freegames import floor, vector
from pacman_board import PacmanBoard
from pacman_agents import PacmanRandom
from ghost_agents import GhostRandom
from copy import deepcopy
from board_raw import *
from datetime import *

position = vector(-40, -80)
direction = vector(0, -5)
pacman = PacmanRandom(position, direction)

ghost = vector(-180,160)
ghostDir = vector(10, 0)

ghosty = GhostRandom(ghost, ghostDir, deepcopy(tiles))
ghostz = [ghosty]

game = PacmanBoard(deepcopy(tiles), deepcopy(pacman), deepcopy(ghostz))
game.game_setup()

