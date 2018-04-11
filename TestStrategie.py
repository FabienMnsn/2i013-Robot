#imports

from robot_gopy.robot2I013 import *
from strategies.simulation import *
from strategies.strategieToutDroit70 import *
from strategies.strategieRot90 import *
#from strategieCarre import *
#from robot2 import *

#script de test de la simulation

#creation d un robot

robot1 = Robot2I013()
#robot1 = Creation_Robot()

#creation d une strategie tout droit
#stratDroit = strategieToutDroit70(robot1)
strat90 = strategieRot90(robot1)
#creation d une simulation tout droit
#simu1 = Simulation(stratDroit)
simu1 = Simulation(strat90)


#lancement de la strategie (ou plutot la boucle de la simu) tout droit
print("**Debut de la strategie de deplacement tout droit**")
simu1.run()
print("**Fin de la strategie**")

