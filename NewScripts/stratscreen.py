#strategie visant a enregistrer l image de la camera du robot

class stratscreen():
    def __init__(self, robot):
        self.stop = False
        self.robi = robot

    def update(self):
        im = self.robi.rgo.get_image()
        im.save("test.jpg")
        self.stop = True