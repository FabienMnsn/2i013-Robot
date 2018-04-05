from robot2I013 import *

#code

class strategieCamera:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False

    def update(self):
        self.robot.get_image()
        self.stop
        
