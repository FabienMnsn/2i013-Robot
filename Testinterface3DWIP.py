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


a = Arene(1500,200,1500,[],[]) # en changeant les 3 premeires valeur on modifie la taille de l'arene
a.safficher()
a.generateur_arene()
a.safficher()

b = Balise(160,0,-80,50)

r = Creation_Robot(0,0,0,1)
print(r.safficher())

#c = Cube(40,0,-50,50,50,50)

#s = Sol(0,0,0,4000,4000)

#m = Mur(-150,0,0,30,200,20)

main.eye = (0,400,800)
main.lookat = (0,0,0)
main.up = (0,0,-1)

main.addVueArene(a)
#main.addVueMur(m)
main.addVueRobot(r)
#main.addVueSol(s)
#main.addVueBalise(b)
#main.addVueCube(c)


#for i in range(0, 30):
    
#r.set_motor_dps(3,50)
#r.set_motor_dps(2,50)
#main.addVueRobot(r)
#main.on_draw()
#print(r.safficher())
    

pyglet.app.run()
