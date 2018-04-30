import stratCarre70

class Simulation():

	def __init__(self,strategie):
		self.strategie = strategie

	def run(self):
		cpt=0
		while not self.strategie.stop():
			self.strategie.update()
			cpt+=1
		print("Stoping")
