from robots.robot import Robot as rien
from robots.rconverter import RConverter as Robot
from composants.cube import *
from composants.mur import *
from composants.sol import *
from composants.arene import *

#from strategie.strat70 import Strat70 as Strat
#from strategie.stratCarre70 import StratCarre70 as Strat
#from strategie.stratRotD90 import StratRotD90 as Strat
LXA,LYA,LZA=10000,10000,30000 #En mm

POS=(LXA/2,LYA/2,1)
DIR=90
V=360

r=Robot(POS,DIR,V)
print(r.toString())

a=Arene(LXA,LYA,LZA)
a.generationA()
a.addRobot(r)
print(a.toString())

r.move()

print(a.toString())
