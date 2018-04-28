#imports

from interface.interface3DWIP import *
from robot_sim.robot2 import *
from basiques.mur import *
#code


newwindow = Window(800, 800, "Arena", resizable=False)

#newwindow.addbalise(0, 50, -100, 25, "f")  #pour les mur de face en z
#newwindow.addcube(0, 0, 0, 1000, 2, 1000, 3) #sol

mur = Creation_Mur()
robot = Creation_Robot()
newwindow.addcube(mur)
newwindow.addcube(robot)
        
#pyglet.clock.schedule_interval(10,newwindow.frame_rate)
pyglet.app.run()
