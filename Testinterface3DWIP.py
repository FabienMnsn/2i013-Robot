#imports

from interface.interface3DWIP import *
from robot_sim.robot2 import *
from basiques.mur import *
#code


newwindow = Window(800, 800, "Arena", resizable=False)

#newwindow.addbalise(0, 50, -100, 25, "f")  #pour les mur de face en z
#newwindow.addcube(0, 0, 0, 1000, 2, 1000, 3) #sol

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
