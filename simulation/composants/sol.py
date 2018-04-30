from composants.cube import Cube

class Sol(Cube):

    def __init__(self, x, y, z, lx, ly, lz=1):
        Cube.__init__(self, x, y, z, lx, ly, lz)

    def toString(self):
        return "Sol: Pos [{0},{1},{2}], Dim [{3},{4},{5}]\n".format(self.x, self.y, self.z, self.lx, self.ly, self.lz)

def Creation_Sol(arene):
    x = 1
    y = 1
    z = 0

    lx = arene.lx-1
    ly = arene.ly-1

    return Sol(x, y, z, lx, ly)

