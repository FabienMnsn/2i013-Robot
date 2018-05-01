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

main = Window(800, 800, "Arena", resizable=False)

b = Creation_Balise()
#print(b.safficher())

r = Creation_Robot()
#print(r.getDimension())

c = Cube(40,70,-100,20,20,20)
#print(c.safficher())


#vb = vueB(b)
#vr = vueR(r)
#vc = vueC(c)
#print(vc.batch)

main.addVueBalise(b)
main.addVueRobot(r)

main.addVueCube(c)
main.addVueCube(Cube(100,60,150,50,50,50))

for i in range(0, 30):
    #r.set_motor_dps(2,-5)
    #print(r.safficher())
    main.addVueRobot(r)

pyglet.app.run()
