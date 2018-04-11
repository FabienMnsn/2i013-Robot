from robot_gopy.robot2I013 import *
from time import strftime
from datetime import datetime

#code
robot = Robot2I013()
img = robot.get_image()
date = str(datetime.now())
img.save(date+".jpg")

"""
class strategieCamera:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False

    def update(self):
        self.robot.get_image()
        self.stop = True """
        
