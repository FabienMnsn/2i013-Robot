import stratTriangle
import robot2I013
import time, os
import simulationTriangle

robot=robot2I013.Robot2I013()

strat=stratTriangle.StratTriangle(robot)

simul=simulationTriangle.SimulationTriangle(strat)
simul.run()
