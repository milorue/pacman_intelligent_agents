# Project: Pacman (and Ghost) AI
Milo Rue, Gabe Pesco, Justin Moczynski

## Description
This project implemented different Artificial Intelligence approaches for the ghosts to kill pacman and for pacman to score more points and stay alive longer.

## PEAS
- **Performance Measures:** Final game score, total survival time

- **Environment:** Board, pellets

- **Actuators (Pacman):** At any time: Legal move (Up, Down, Left, Right)

- **Actuators (Ghost):** At junction: Legal move (Up, Down, Left, Right)

- **Sensors:** Board, location of pellets, location of all agents (ghosts, pacman)

## Agent Definition
- **PacmanHuman:** Human controlled agent for validation Ghost agent validation

- **PacmanBetterRandom:** Agent who randomly selects moves on the board at junctions (places where at least two directions are possible in addition to the current direction), used for a baseline for data collection

- **PacmanGreedy:** Agent whose objective is to score the most it can, disregarding where the ghosts are located on the board

- **SmartPacman:** Agent whose objective is to score the most it can, considering where the ghosts are located on the board

- **GhostBetter:** Agent who randomly selects moves on the board at junctions (places where at least two directions are possible in addition to the current direction), used for a baseline for data collection

- **GhostAStar:** Agent whose objective is to kill pacman using A-Star search technique

- **GhostAStarWithScatter:** Agent whose objective is to kill pacman using A-Star search technique with randomly delays

- **GhostPinky:** Agent whose objective is to kill pacman using A-Star search technique after waiting at the start of the game
<!-- - **GhostGBFS:** Takes the move that moves them closest to Pacman at his current location. -->

- **PacmanMC:** Uses Monte Carlo tree search to choose a move when at a junction. (work in progress)

<!-- - **GhostSA:** Uses Simulated Annealing to learn what actions will be most likely to capture Pacman. -->

## Work Distribution

### (ending 11/12/19)
- **Milo:** (Interface and Environment

- **Justin:** (Random behavior and Data collection)

- **Gabe:** (Ghost AI)

### (ending 11/19/19)
- **Milo:** (Bug & Game Rules | Random Pacman & Ghost Behavior)

- **Justin:** (Data Collection & Performance Measures)

- **Gabe:** (Ghost Definitions)

### (ending 12/03/19)
- **Milo:** (Power Pellet Implementations, Simple Greedy)

- **Justin:** (Game Reset & Restart, Data Collect)

- **Gabe:** (Ghost Definitions | Monte Carlo Search)

### (ending 12/10/19)
- **Milo:** (Fun ghost implementations including "Follow the Leader")

- **Justin:** (Data Collection Methods, Performance Measures | Pacman A-Star Search)

- **Gabe:** (Revised A Star Search | Clean up interface)

### (ending 12/17/19)
- **Milo:** (progress on Fun ghost implementations including "Follow the Leader")

- **Justin:** (Pacman A-Star Search | Data Collection Methods)

- **Gabe:** (Clean up interface | progress on Monte Carlo Implementation)

## Results

The following graphs were created after collecting data from multiple simulations of Pacman with varying ghost AI types and pacman AI types.

This graph displays the number of games each ghost AI agent captured pacman in the dataset.

![](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/count-capture_type.png)

Notice the GhostAStar agent captures the pacman the most times for each of the different Pacman AI implementations.

These graphs display the average score of Pacman when it is captured by each type of ghost from the games in the dataset.

![](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_score-capture_type.png)
![](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_score-pacman_type.png)

Notice the SmartPacman agent scores the highest on average for each of the different Ghost AI implementations. In addition, notice the second-best performing agent with regards to maximizing score is the PacmanGreedy agent. The PacmanBetterRandom is the worst agent with regards to maximizing score.

These graphs display the average time Pacman stays alive before it is captured by each type of ghost from the games in the dataset.

![](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_time-capture_type.png)
![](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_time-pacman_type.png)

Notice the SmartPacman agent stays alive the longest on average for each of the different Ghost AI implementations. In addition, notice the second-best performing agent with regards to maximizing playing time is the PacmanBetterRandom agent. The PacmanGreedy is the worst agent with regards to maximizing playing time.

## Research Sources
original code source: https://github.com/grantjenks/free-python-games/blob/master/freegames/pacman.py

Monte Carlo research source: https://towardsdatascience.com/monte-carlo-tree-search-158a917a8baa
