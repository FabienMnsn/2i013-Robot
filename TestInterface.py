#imports

from time import sleep
from interface.interface import *
from robot_sim.robot2 import *

#code

#_____creation dun robot_____
robot1 = Creation_Robot()

#_____creation dune interface_____
interface = Interface()

#_____boucle de test de mise a jour de l'interface_____
for i in range(0, 5):
    
    robot1.servo_rotate(45)
    robot1.setPosition((250+10*1, 250+10*i, 10))
    interface.rafraichir(robot1)
