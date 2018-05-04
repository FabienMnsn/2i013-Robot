#imports

from interface.interface3DWIP import *

from basiques.cube import *
from basiques.mur import *
from basiques.balise import *
from basiques.sol import *

from robot_sim.robot2 import *

#code

main = Window(1000, 400, "Arena", resizable=True)


b = Balise(160,0,-80,50)

r = Creation_Robot(0,0,0,1)
print(r.safficher())

c = Cube(40,0,-50,50,50,50)

s = Sol(0,0,0,4000,4000)

m = Mur(0,0,-150,3000,200,20)

main.eye = (0,80,400)
main.lookat = (0,0,0)
main.up = (0,0,-1)

main.addVueMur(m)
main.addVueRobot(r)
main.addVueSol(s)
main.addVueBalise(b)
main.addVueCube(c)


#for i in range(0, 30):
    
r.set_motor_dps(3,50)
#r.set_motor_dps(2,50)
#main.addVueRobot(r)
#main.on_draw()
print(r.safficher())
    

pyglet.app.run()
