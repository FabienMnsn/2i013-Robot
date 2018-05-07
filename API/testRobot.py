#import strat70
#import stratRotD90
#import stratCarre70
import robot2I013
import time, os
import simulation
import stratImage

robot=robot2I013.Robot2I013()

"""
i=0
while i < 3:
    with open("imagecouleur"+str(i)+".jpg",'w') as fic:
        img=robot.get_image()
        img.save("imagecouleur"+str(i)+".jpg")
        #fic.write(img)
    time.sleep(3)
    i=i+1"""
    
#strat=strat70.Strat70(robot)
#strat=stratCarre70.StratCarre70(robot)
#strat=stratRotD90.StratRotD90(robot)

strat=stratImage.StratImage(robot)

simul=simulation.Simulation(strat)
simul.run()
