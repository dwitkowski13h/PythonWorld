from .Plant import Plant


class Grass(Plant):

	def __init__(self, plant=None, position=None, world=None):
		super(Grass, self).__init__(plant, position, world)

	def clone(self):
		return Grass(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 0
		self.liveLength = 7
		self.powerToReproduce = 3
		self.sign = 'G'
