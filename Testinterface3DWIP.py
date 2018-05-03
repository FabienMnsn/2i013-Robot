#imports

from interface.interface3DWIP import *

from basiques.cube import *
from basiques.mur import *
from basiques.balise import *

from robot_sim.robot2 import *
from robot_sim.vuerobot import VueRobot as vueR
from robot_sim.vuecube import VueCube as vueC
from robot_sim.vuebalise import VueBalise as vueB

#code

main = Window(1000, 400, "Arena", resizable=True)

b = Balise(160,0,-80,80)
#print(b.safficher())

r = Creation_Robot(0,0,-1,1)
#print(r.getDimension())
print(r.safficher())

c = Cube(-120,0,-50,40,60,40)
#print(c.safficher())

s = Sol(0,0,0,4000,4000)
#print(s.safficher())


main.eye = (0,10,200)
main.lookat = (0,40,0)

main.addVueRobot(r)
main.addVueSol(s)
main.addVueBalise(b)
main.addVueCube(c)
main.addVueCube(Cube(0,0,0,20,20,20))


#for i in range(0, 30):
    
    #r.set_motor_dps(1,-50)
    #r.set_motor_dps(2,50)
    #main.addVueRobot(r)
    #main.on_draw()
    #print(r.safficher())
    

pyglet.app.run()
