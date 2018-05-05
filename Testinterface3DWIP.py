#imports

from interface.interface3DWIP import *

from basiques.cube import *
from basiques.mur import *
from basiques.balise import *
from basiques.sol import *
from basiques.arene import *

from robot_sim.robot2 import *

from strategies.simulation import *
from strategies.strategieToutDroit70 import *

#code

main = Window(720, 480, "Arena", resizable=True)

#setup environnement (arene et ses composants)
a = Arene(800,80,800,[],[]) # en changeant les 3 premieres valeurs on modifie la taille de l'arene
a.safficher()
a.generateur_arene()

b = Balise(160,0,-80,50)

r = Creation_Robot(0,0,-0.4,1)

c0 = Cube(40,0,-100,80,80,80)
c1 = Cube(200,0,250,150,150,150)
a.ajouter_cube(c0)
a.ajouter_cube(c1)

#setup de strategie et simulation
strat70 = strategieToutDroit70(r)
simulation = Simulation(strat70)

# setup des vue 3D
main.addVueArene(a)
main.addVueRobot(r)
main.addVueBalise(b)
main.addSim(simulation)

#setup position camera
main.eye = (0,300,700)
main.lookat = (0,100,0)
main.up = (0,0,-1)

#RUN GENERAL
pyglet.app.run()
