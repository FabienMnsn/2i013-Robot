import time
from pyglet.gl import *

from interface3D.window import Model, Window
from composants.cube import Cube
from composants.mur import Mur
from composants.sol import Sol
from composants.arene import Arene

from robots.robot import Robot as rien
from robots.rconverter import RConverter as Robot

#from strategie.strat70 import Strat70 as Strat
#from strategie.stratCarre70 import StratCarre70 as Strat
from strategie.stratRotD90 import StratRotD90 as Strat

LXA,LYA,LZA=10000,10000,3000 #En mm
POS=(LXA/2,LYA/2,1)
DIR=90
V=360

r=Robot(POS,DIR,V)

#s=Strat(r)
#r.setStrat(s)

a=Arene(LXA,LYA,LZA)
a.generationA()
a.addRobot(r)
print(a.toString())

window = Window(height=1000,width=1200,caption="[Robot 2I013] - 3D View",resizable=True)
window.camera.position=(0,0,0)

glClearColor(0.5,0.7,1,1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)

window.model.setArene(a)
#for c in a.liste_cube:
#    if isinstance(c, Mur):
#        window.model.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),color=(1,1,1))
#    elif isinstance(c, Sol):
#        window.model.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),color=(192/255,192/255,192/255))
#    elif isinstance(c, Cube):
#        window.model.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),texture_file="interface3D/img/cube_side.png")
    
#if a.robot != None:
#    window.model.addRobot((a.robot.getPos()),(a.robot.DIMENSIONS))

pyglet.app.run()

#while not r.strat.stop():
    #r.runStrat()
    #print(r.toString())
#r.setStrat(None)
#print("Strat stopped")
