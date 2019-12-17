from pacman.ghost_agents import *
from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard

pac_pos = vector(-40, -80)
ghost1_pos = vector(-180, 160)
ghost2_pos = vector(-180, -160)
ghost3_pos = vector(100, 160)
ghost4_pos = vector(100, -160)
board = PacmanBoard(deepcopy(tiles))

pacman = PacmanRandom(board, pac_pos)
blinky = GhostAStar(board, ghost1_pos)
pinky = GhostAStar(board, ghost2_pos)
inky = GhostAStar(board, ghost3_pos)
clide = GhostAStar(board, ghost4_pos)
ghosts = [blinky, pinky, inky, clide]

board.define_pacman(pacman)
board.define_ghosts(ghosts)

game = PacmanGame(deepcopy(board), deepcopy(pacman), deepcopy(ghosts))

game.game_setup()
