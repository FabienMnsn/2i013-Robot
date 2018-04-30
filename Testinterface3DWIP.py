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

c = Creation_Cube()
#print(c.safficher())


vb = vueB(b)
vr = vueR(r)
vc = vueC(c)
#print(vc.batch)

main.addVueBalise(vb)
main.addVueRobot(vr)
main.addVueCube(vc)

pyglet.app.run()
"""
mur = Creation_Mur()
balise = Balise(0, 0, -50, 25, "f")
newwindow.addbalise(balise)
robot1 = Creation_Robot()
newwindow.addcube(mur)
newwindow.addrobot(robot1)

print(type(newwindow.balise))
print(type(newwindow.obj_robot))

#for i in range(0,20):
    #robot1.set_motor_dps(2,1)
    #newwindow.on_draw()
    #print(robot1.safficher())
    #
#pyglet.clock.schedule_interval(10,newwindow.frame_rate)
pyglet.app.run()
"""
