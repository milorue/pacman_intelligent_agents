from pacman.ghost_agents import *
from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard
from datetime import *

position = vector(-40, -80)  # pacman position
direction = vector(0, -5)  # pacman direction

ghost = vector(-180, 160)  # ghost positions
ghost2 = vector(-180, -160)
ghost3 = vector(100, 160)
ghost4 = vector(100, -160)

ghostDir = vector(5, 0)  # ghost directions
ghostDir1 = vector(0, 5)
ghostDir2 = vector(0, -5)
ghostDir3 = vector(-5, 0)

ghostList = [ghost, ghost2, ghost3, ghost4]  # list of ghost positions

board = PacmanBoard(deepcopy(tiles), deepcopy(position), deepcopy(ghostList))

pacmanRandom = PacmanRandom(position, direction, board)
pacmanBetter = PacmanBetterRandom(position, direction, board)
human = HumanPacman(position, direction, board)
pacmanGreedy = PacmanGreedy(position, direction, board)
pacmanSmart = SmartPacman(position, direction, board, ghostList)

pacman = human  # set this to change pacman (change to human for demo)

blinky = GhostAStar(ghost, ghostDir, board, pacman)
pinky = GhostAStar(ghost2, ghostDir1, board, pacman)
inky = GhostAStar(ghost3, ghostDir2, board, pacman)
clide = GhostAStar(ghost4, ghostDir3, board, pacman)

stinky = GhostAStar(ghost, ghostDir, board, pacman)
rinky = GhostBetter(ghost2, ghostDir1, board, pacman)
tinker = GhostPinky(ghost3, ghostDir2, board, pacman)
green_uggs = GhostBetter(ghost4, ghostDir3, board, pacman)

dumbo = GhostBetter(ghost, ghostDir, board, pacman)
dumbky = GhostBetter(ghost2, ghostDir1, board, pacman)
dumbit = GhostBetter(ghost3, ghostDir2, board, pacman)
dumby = GhostBetter(ghost4, ghostDir3, board, pacman)

help = GhostBS(ghost, ghostDir, board, pacman)
me = GhostBS(ghost2, ghostDir1, board, pacman)
out = GhostBS(ghost3, ghostDir2, board, pacman)
please = GhostBS(ghost4, ghostDir3, board, pacman)

gogo = GhostPinky(ghost, ghostDir, board, pacman)
dodo = GhostAStar(ghost2, ghostDir1, board, pacman)
bobo = GhostAStar(ghost3, ghostDir2, board, pacman)
toto = GhostFollowLeader(ghost4, ghostDir3, board, pacman, ghostList)

ghostsAllRandom = [dumbo, dumbky, dumbit, dumby]
ghostsAllSmart = [blinky, pinky, inky, clide]
ghostsHalfRandom = [stinky, rinky, tinker, green_uggs]
ghostsOddity = [bobo, dodo, gogo, toto]
ghostsHELP = [help, me, out, please]

fullList = [ghostsAllRandom, ghostsHalfRandom, ghostsOddity, ghostsAllSmart, ghostsHELP]


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def randomize_ghosts(ghost_list):  # takes a list of lists of ghosts and returns one
    out = choice(ghost_list)
    print(namestr(out, globals()))
    return out


for i in range(5):
    ghostz = fullList[i]
    print(namestr(ghostz, globals()))
    game = PacmanGame(deepcopy(board), deepcopy(pacman), deepcopy(ghostz))
    try:
        start = datetime.now()
        game.game_setup()
    except SystemExit:
        data_round = game.state['score']
        print(i + 1, ":", data_round)
