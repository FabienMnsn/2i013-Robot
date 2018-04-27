#imports

from robot_sim.Interface3D import *
from robot_sim.robot2 import *

#code
robot = Creation_Robot()

newwindow = Window(800, 800, "Arena", resizable=False)
#newwindow.addcube(-200, 200, 200, 20, 400, 400, 1)  # pour un mur de cote l epaisseur sera en l
#newwindow.addcube(200, 200, 200, 20, 400, 400, 1)
#newwindow.addcube(200, 200, 600, 20, 400, 400, 1)

#newwindow.addcube(0, 25, 0, 50, 50, 50, 2) #robot?
newwindow.addcube(robot.position[0], robot.position[1]+35, robot.position[2], robot.dimension[0], robot.dimension[1], robot.dimension[2], 2)#robot avec les parametre du robot2

newwindow.addcube(0, 0, 0, 1000, 2, 1000, 3) #sol
newwindow.addbalise(0, 50, -100, 25, "f")  #pour les mur de face en z
#newwindow.addbalise(0, 0, 0, 100, "c")
i = 0
while(i < 10):
        
	i += 1
pyglet.clock.schedule_interval(newwindow.update, newwindow.frame_rate)
pyglet.app.run()
