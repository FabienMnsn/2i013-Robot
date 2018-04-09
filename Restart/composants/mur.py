from composants.cube import Cube
import random

class Mur(Cube):

    def __init__(self, x, y, z, lx, ly, lz):
        Cube.__init__(self, x, y, z, lx, ly, lz)

    def toString(self):
        return "Mur: Pos [{0},{1},{2}], Dim [{3},{4},{5}]\n".format(self.x, self.y, self.z, self.lx, self.ly, self.lz)
			
def Creation_Mur(arene):

    x = random.randint(0, arene.lx)
    y = random.randint(0, arene.ly)
    z = 1

    lx = random.randint(10, 1000)
    ly = random.randint(10,1000)
    lz = arene.lz-1
    
    return Mur(x, y, z, lx, ly, lz)
