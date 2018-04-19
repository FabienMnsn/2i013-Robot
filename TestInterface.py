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
    #print(robot1.safficher())
    #robot1.servo_rotate(45)
    interface.rafraichir(robot1)
    robot1.set_motor_dps(3,-10)
    robot1.get_distance()
    #print("dist. moy. =",robot1.get_distance(),"(mm)")
    #sleep(1)
    
