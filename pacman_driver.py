from random import choice
from turtle import *
from freegames import floor, vector
from pacman_board import PacmanBoard
from pacman_agents import PacmanRandom
from copy import deepcopy
from board_raw import *
from datetime import *

position = vector(-40, -80)
direction = vector(0, -5)
pacman = PacmanRandom(position, direction)

game = PacmanBoard(deepcopy(tiles), deepcopy(pacman), deepcopy(ghosts))
game.game_setup()

