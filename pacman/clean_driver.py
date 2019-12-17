from pacman.ghost_agents import *
from pacman.pacman_game import PacmanGame
from pacman.pacman_agents import *
from copy import deepcopy
from pacman.board_raw import *
from pacman.pacman_board import PacmanBoard

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

pacman = pacmanSmart  # set this to change pacman (change to human for demo)

blinky = GhostAStar(ghost, ghostDir, board, pacman)
pinky = GhostAStar(ghost2, ghostDir1, board, pacman)
inky = GhostAStar(ghost3, ghostDir2, board, pacman)
clide = GhostAStar(ghost4, ghostDir3, board, pacman)

stinky = GhostAStarWithScatter(ghost, ghostDir, board, pacman)
rinky = GhostRandomFollow(ghost2, ghostDir1, board, pacman)
tinker = GhostPinky(ghost3, ghostDir2, board, pacman)
green_uggs = GhostFollowLeader(ghost4, ghostDir3, board, pacman, ghostList)

dumbo = GhostBetter(ghost, ghostDir, board, pacman)
dumbky = GhostBetter(ghost2, ghostDir1, board, pacman)
dumbit = GhostBetter(ghost3, ghostDir2, board, pacman)
dumby = GhostBetter(ghost4, ghostDir3, board, pacman)

gogo = GhostPinky(ghost, ghostDir, board, pacman)
dodo = GhostRandomFollow(ghost2, ghostDir1, board, pacman)
bobo = GhostAStar(ghost3, ghostDir2, board, pacman)
toto = GhostFollowLeader(ghost4, ghostDir3, board, pacman, ghostList)

ghostsDumb = [dumbo, dumbky, dumbit, dumby]
ghostsUnfair = [blinky, pinky, inky, clide]
ghostsWeird = [stinky, rinky, tinker, green_uggs]
ghostsOddity = [bobo, dodo, gogo, toto]

fullList = [ghostsUnfair, ghostsWeird, ghostsDumb, ghostsOddity]


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def randomize_ghosts(ghost_list):  # takes a list of lists of ghosts and returns one
    out = choice(ghost_list)
    print(namestr(out, globals()))
    return out


for i in range(10):
    ghostz = randomize_ghosts(fullList)
    game = PacmanGame(deepcopy(board), deepcopy(pacman), deepcopy(ghostz))
    try:
        game.game_setup()
    except SystemExit:
        print("exited")
