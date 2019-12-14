from pacman.ghost_agents import *
from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard

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

blinky = GhostAStar(ghost, ghostDir, board, pacmanBetter)
pinky = GhostBetter(ghost2, ghostDir1, board, pacmanBetter)
inky = GhostBetter(ghost3, ghostDir2, board, pacmanBetter)
clide = GhostBetter(ghost4, ghostDir3, board, pacmanBetter)

ghostz = [blinky, pinky, inky, clide]

game = PacmanGame(deepcopy(board), deepcopy(pacmanSmart), deepcopy(ghostz))

game.game_setup()
