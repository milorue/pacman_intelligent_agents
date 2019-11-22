# Project: Pacman Agents
Intelligent Agents that play Pacman

## PEAS
- **Performance Measures:** Final game score, total survival time

- **Environment:** Board, pellets, power pellets

- **Actuators (Pacman):** At any time: Legal move (Up, Down, Left, Right)

- **Actuators (Ghost):** At junction: Legal move (Up, Down, Left, Right)

- **Sensors:** Board, location of pellets, location of all agents

## Agent Definition
- **PacmanHuman:** Human controlled agent for validation Ghost agent validation.

- **PacmanRandom:** Random agent, used for bulk data collection.

- **GhostRandom:** Random simple reflex agent.

- **GhostGBFS:** Takes the move that moves them closest to Pacman at his current location.

- **GhostMCTS:** Uses Monte Carlo tree search to choose a move when at a junction.

- **GhostSA:** Uses Simulated Annealing to learn what actions will be most likely to capture Pacman.

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

## Agent Interface

## Simulation Interface

## Advanced AI
- **Multi-Agent Cooperative**
- **MonteC Carlo Search**

## Unit Testing Framework
