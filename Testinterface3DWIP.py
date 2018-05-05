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


a = Arene(800,80,800,[],[]) # en changeant les 3 premeires valeur on modifie la taille de l'arene
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

main.eye = (0,300,700)
main.lookat = (0,100,0)
main.up = (0,0,-1)

main.addVueArene(a)
main.addVueRobot(r)
main.addVueBalise(b)

#for i in range(0, 30):
    
#r.set_motor_dps(3,50)
#r.set_motor_dps(2,50)
#main.addVueRobot(r)
#main.on_draw()
#print(r.safficher())
    

pyglet.app.run()
