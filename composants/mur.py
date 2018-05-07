from composants.cube import Cube
import random

class Mur(Cube):

    def __init__(self, x, y, z, lx, ly, lz):
        Cube.__init__(self, x, y, z, lx, ly, lz)

    def toString(self):
        return "Mur: Pos [{0},{1},{2}], Dim [{3},{4},{5}]\n".format(self.x, self.y, self.z, self.lx, self.ly, self.lz)
