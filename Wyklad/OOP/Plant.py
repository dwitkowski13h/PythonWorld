from Organism import Organism
import random

class Plant(Organism):

	def __init__(self, plant=None, position=None):
		super(Plant, self).__init__(plant, position)

	def move(self):
		pass