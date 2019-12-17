# Project: Pacman (and Ghost) AI

## Description
This project implemented different Artificial Intelligence approaches for the ghosts to kill pacman and for pacman to score more points and stay alive longer.

## PEAS
- **Performance Measures:** Final game score, total survival time

- **Environment:** Board, pellets, power pellets

- **Actuators (Pacman):** At any time: Legal move (Up, Down, Left, Right)

- **Actuators (Ghost):** At junction: Legal move (Up, Down, Left, Right)

- **Sensors:** Board, location of pellets, location of all agents (ghosts, pacman)

## Agent Definition
- **PacmanHuman:** Human controlled agent for validation Ghost agent validation.

- **PacmanRandom:** Random agent, used for bulk data collection.

- **GhostRandom:** Random simple reflex agent.

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
- **Milo:** (Fun ghost implementations including "Follow the Leader")

- **Justin:** (Pacman A-Star Search | Data Collection Methods)

- **Gabe:** (Clean up interface | Monte Carlo Implementation)

## Results

The following graphs were created after collecting data from multiple simulations of Pacman with varying ghost AI types and pacman AI types.

![description](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/count-capture_type.png)

![description](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_score-capture_type.png)

![description](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_score-pacman_type.png)

![description](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_time-capture_type.png)

![description](https://github.com/ElvinLord12/pacman_intelligent_agents/blob/master/mean_time-pacman_type.png)

## Original Code Source
https://github.com/grantjenks/free-python-games/blob/master/freegames/pacman.py
