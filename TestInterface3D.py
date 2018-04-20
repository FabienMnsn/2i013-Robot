#imports

from robot_sim.Interface3D import *

#code

newwindow = Window(800, 800, "Arena", resizable=False)
#newwindow.addcube(-200, 200, 200, 20, 400, 400, 1)  # pour un mur de cote l epaisseur sera en l
#newwindow.addcube(200, 200, 200, 20, 400, 400, 1)
#newwindow.addcube(200, 200, 600, 20, 400, 400, 1)
newwindow.addcube(0, 25, 0, 50, 50, 50, 2) #robot?
newwindow.addcube(0, 0, 0, 1000, 2, 1000, 3) #sol
newwindow.addbalise(0, 50, -100, 25, "f")  #pour les mur de face en z
#newwindow.addbalise(0, 0, 0, 100, "c")

pyglet.clock.schedule_interval(newwindow.update, newwindow.frame_rate)
pyglet.app.run()
