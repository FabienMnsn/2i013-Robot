#imports

from interface.interface3DWIP import *

from basiques.cube import *
from basiques.mur import *
from basiques.balise import *
from basiques.sol import *
from basiques.arene import *

from robot_sim.robot2 import *

#code

main = Window(720, 480, "Arena", resizable=True)

#setup environnement (arene et ses composants)
a = Arene(800,80,800,[],[]) # en changeant les 3 premieres valeurs on modifie la taille de l'arene
a.safficher()
a.generateur_arene()
a.safficher()

b = Balise(160,0,-80,50)

r = Creation_Robot(0,0,0,1)
print(r.safficher())

c0 = Cube(40,0,-100,80,80,80)
c1 = Cube(200,0,250,150,150,150)
a.ajouter_cube(c0)
a.ajouter_cube(c1)

main.addVueArene(a)
main.addVueRobot(r)
main.addVueBalise(b)

#setup position camera
main.eye = (0,300,700)
main.lookat = (0,100,0)
main.up = (0,0,-1)
    

pyglet.app.run()
