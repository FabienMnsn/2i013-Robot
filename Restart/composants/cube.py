import random

class Cube():

    def __init__(self, x, y, z, lx, ly, lz):
        self.x = x
        self.y = y
        self.z = z
        self.lx = lx
        self.ly = ly
        self.lz = lz
     
    def toString(self):
        return "Cube: Pos [{0},{1},{2}], Dim [{3},{4},{5}]\n".format(self.x, self.y, self.z, self.lx, self.ly, self.lz)

    def getPos(self):
        return self.x, self.y, self.z

def Creation_Cube(arene):
    x = random.randint(0,arene.lx)
    y = random.randint(0,arene.ly)
    z = random.randint(0,arene.lz)
    
    lx = random.randint(50,70)
    ly = random.randint(50,70)
    lz = random.randint(50,70)
    
    return Cube(x, y, z, lx, ly, lz)
