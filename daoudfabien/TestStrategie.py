#imports

from robot2I013 import *
from simulation import *
from strategieToutDroit70 import *
from strategieCarre import *

#script de test de la simulation

#creation d un robot
robot1 = Robot2I013()
#creation d une strategie tout droit
stratDroit = strategieToutDroit70(robot1)
#creation d une simulation tout droit
simu1 = Simulation(stratDroit)

"""
#creation d une strategie carre
stratCarre = strategieCarre(robot1)
#creation d une simulation pour le carre
simu2 = Simulation(stratCarre)
"""

#lancement de la strategie (ou plutot la boucle de la simu) tout droit
print("**Debut de la strategie de deplacement tout droit**")
simu1.run()
print("**Fin de la strategie**")


"""
#lancement de la strategie Carre
print("**Debut de la strategie Carre**")
simu2.run()
print("**Fin de la strategie Carre**")
"""
