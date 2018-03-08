#-*- coding: utf-8 -*-

import pyglet
from interface.featuresGL import *
from structures.robot import *
from basiques.cube import *
from structures.arene import *
from save.saveJson import *
from save.csvToJson import *
import random

# script deplacement robot
if __name__ == "__main__":
    mode = raw_input("Veuillez rentrer le mode d'affichage:")
    # creation arene + robot
    arena = Creation_Arene()
    sol = Creation_Sol(arena)
    iRobot = Creation_Robot(arena)

    # affichage
    # dans le terminal
    if mode == "-t":
        arena.afficher()

    #dans une fenetre
    if mode =="-3D":
        aWindow = Window(500,500,"new world")

        pyglet.app.run()

    # deplacement robot
