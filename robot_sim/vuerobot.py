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
        
        """
        # faces
        # f1 arriere
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

        # f2 dessous
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

        # f3 avant
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

        # f4 dessus
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

        # f5 cote droit
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

        # f6 cote gauche
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
        """
        # faces
        # f1 arriere
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[3][0], self.robot.coords[3][1], self.robot.coords[3][2],
                    self.robot.coords[2][0], self.robot.coords[2][1], self.robot.coords[2][2],
                    self.robot.coords[6][0], self.robot.coords[6][1], self.robot.coords[6][2],
                    self.robot.coords[7][0], self.robot.coords[7][1], self.robot.coords[7][2])),
                       colorf1)

        # f2 dessous
        #print(type(robot))
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[0][0], self.robot.coords[0][1], self.robot.coords[0][2],
                    self.robot.coords[1][0], self.robot.coords[1][1], self.robot.coords[1][2],
                    self.robot.coords[2][0], self.robot.coords[2][1], self.robot.coords[2][2],
                    self.robot.coords[3][0], self.robot.coords[3][1], self.robot.coords[3][2])),
                       colorf2)

        # f3 avant
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[4][0], self.robot.coords[4][1], self.robot.coords[4][2],
                    self.robot.coords[5][0], self.robot.coords[5][1], self.robot.coords[5][2],
                    self.robot.coords[1][0], self.robot.coords[1][1], self.robot.coords[1][2],
                    self.robot.coords[0][0], self.robot.coords[0][1], self.robot.coords[0][2])),
                       colorf3)

        # f4 dessus
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[5][0], self.robot.coords[5][1], self.robot.coords[5][2],
                    self.robot.coords[4][0], self.robot.coords[4][1], self.robot.coords[4][2],
                    self.robot.coords[7][0], self.robot.coords[7][1], self.robot.coords[7][2],
                    self.robot.coords[6][0], self.robot.coords[6][1], self.robot.coords[6][2])),
                       colorf4)

        # f5 cote droit
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[1][0], self.robot.coords[1][1], self.robot.coords[1][2],
                    self.robot.coords[5][0], self.robot.coords[5][1], self.robot.coords[5][2],
                    self.robot.coords[6][0], self.robot.coords[6][1], self.robot.coords[6][2],
                    self.robot.coords[2][0], self.robot.coords[2][1], self.robot.coords[2][2])),
                       colorf5)

        # f6 cote gauche
        self.batch.add(4, GL_QUADS, None, (
            'v3f', (self.robot.coords[4][0], self.robot.coords[4][1], self.robot.coords[4][2],
                    self.robot.coords[0][0], self.robot.coords[0][1], self.robot.coords[0][2],
                    self.robot.coords[3][0], self.robot.coords[3][1], self.robot.coords[3][2],
                    self.robot.coords[7][0], self.robot.coords[7][1], self.robot.coords[7][2])),
                       colorf6)
    
