#imports

from robot2I013 import *
from simulation import *
from strategie import *

#script de test de la simulation

#création d'un robot
robot1 = Robot2I013()
#création d'une stratégie tout droit
stratDroit = strategieToutDroit70(robot1)
#création d'une simulation tout droit
simu1 = Simulation(stratDroit)

#création d'une stratégie carré
stratCarre = strategieCarre(robot1)
#creation d'une simulation pour le carré
simu2 = Simulation(stratCarre)

#lancement de la strategie (ou plutot la boucle de la simu) tout droit
print("**Début de la stratégie de déplacement tout droit**")
simu1.run()
print("**Fin de la stratégie**")

#lancement de la strategie Carre
print("**Début de la stratégie Carré**")
simu2.run()
print("**Fin de la stratégie Carré**")
