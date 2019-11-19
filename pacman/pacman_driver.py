from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import PacmanRandom, PacmanBetterRandom, HumanPacman
from pacman.ghost_agents import GhostRandom, GhostBetter
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard

position = vector(-40, -80)
direction = vector(0, -5)

board = PacmanBoard(deepcopy(tiles))

pacman = PacmanRandom(position, direction, board)
pacmanBetter = PacmanBetterRandom(position, direction, board)
human = HumanPacman(position, direction, board)


ghost = vector(-180,160)
ghost2 = vector(-180, -160)
ghost3 = vector(100, 160)
ghost4 = vector(100, -160)
ghostDir = vector(5, 0)
ghostDir1 = vector(0, 5)
ghostDir2 = vector(0, -5)
ghostDir3 = vector(-5, 0)

blinky = GhostBetter(ghost, ghostDir, board, pacman)
pinky = GhostBetter(ghost2, ghostDir1, board, pacman)
inky = GhostBetter(ghost3, ghostDir2, board, pacman)
clide = GhostBetter(ghost4, ghostDir3, board, pacman)


ghostz = [blinky, pinky, inky, clide]

game = PacmanGame(board, deepcopy(human), deepcopy(ghostz))
game.game_setup()

