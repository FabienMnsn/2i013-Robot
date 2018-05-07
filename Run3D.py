import time
from pyglet.gl import *

from interface3D.window import Window
from composants.cube import Cube
from composants.mur import Mur
from composants.sol import Sol
from composants.arene import Arene

from robots.robot import Robot as rien
from robots.rconverter import RConverter as Robot

from strategie.simulation import Simulation
from strategie.strat70 import Strat70 as Strat
#from strategie.stratCarre70 import StratCarre70 as Strat
#from strategie.stratRotD90 import StratRotD90 as Strat

LXA,LYA,LZA=10000,10000,3000 #En mm
POS=(LXA/2,LYA/2,10)
DIR=0
V=0

r=Robot(POS,DIR,V)

a=Arene(LXA,LYA,LZA)
a.generationA()
a.addRobot(r)
print(a.toString())

simul=Simulation(None,a)

window = Window(height=1000,width=1200,caption="[Robot 2I013] - 3D View",resizable=True )
window.camera.position=(0,0,0) 
window.set_simul(simul)
glClearColor(0.5,0.7,1,1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)

window.model.setArene(a)
pyglet.app.run()
