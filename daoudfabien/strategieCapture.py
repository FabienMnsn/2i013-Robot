from robot2I013 import *

#code
robot = Robot2I013()
img = robot.get_image()
img.save("/users/Etu3/3670293/L2/S2/2I013/Projet/Robot7M/daoudfabien/Images/Image.jpg")

"""
class strategieCamera:
    def __init__(self, robot):
        self.robot = robot
        self.stop = False

    def update(self):
        self.robot.get_image()
        self.stop = True """
        
