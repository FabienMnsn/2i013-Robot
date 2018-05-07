import stratImage

class SimulationImage():

    def __init__(self,strategie):
        self.strategie = strategie

    def run(self):
        self.strategie.nouvelle_image()
        while not self.strategie.stop():
            self.strategie.update()
		print("Stoping")
