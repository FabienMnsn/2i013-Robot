#imports

import pyglet
from pyglet.gl import *
from robot_sim.robot2 import *

#code

class VueRobot:
    def __init__(self, robot_att):

        self.robot = robot_att
        position = self.robot.getPosition() + self.robot.getDimension()
        dimension = (position[3], position[4], position[5])
        
        self.batch = pyglet.graphics.Batch()
        
        #print("pos:", position,"dim:",dimension)
        
        colorf1 = ('c3f', (1., 1., 1.,) * 4)
        colorf2 = ('c3f', (0.95, 0.95, 0.95,) * 4)
        colorf3 = ('c3f', (0.90, 0.90, 0.90,) * 4)
        colorf4 = ('c3f', (0.85, 0.85, 0.85,) * 4)
        colorf5 = ('c3f', (0.80, 0.80, 0.80,) * 4)
        colorf6 = ('c3f', (0.75, 0.75, 0.75,) * 4)
        # faces
        # f1
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (position[0] + dimension[0]/2,
                    position[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] + dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] + dimension[2]/2)),
                       colorf1)

        # f2
        #print(type(robot))
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (position[0] + dimension[0]/2,
                    position[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1],
                    position[2] - dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1],
                    position[2] - dimension[2]/2)),
                       colorf2)

        # f3
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (position[0] + dimension[0]/2,
                    position[1],
                    position[2] - dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1],
                    position[2] - dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] - dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] - dimension[2]/2)),
                       colorf3)

        # f4
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (position[0] + dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] - dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] - dimension[2]/2)),
                       colorf4)

        # f5
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (position[0] + dimension[0]/2,
                    position[1],
                    position[2] - dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1],
                    position[2] + dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] + dimension[2]/2,
                    position[0] + dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] - dimension[2]/2)),
                       colorf5)

        # f6
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (position[0] - dimension[0]/2,
                    position[1],
                    position[2] - dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] + dimension[2]/2,
                    position[0] - dimension[0]/2,
                    position[1] + dimension[1],
                    position[2] - dimension[2]/2)),
                       colorf6)
    
