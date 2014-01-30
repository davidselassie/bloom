import copy

import bloom_vector
import bloom_bullet

class bloomBarrage:
	def __init__(self):
		self.pattern = []
		
	def fire(self):
		return copy.deepcopy(self.pattern)
	
	def addBullet(self, pattern):
		self.pattern.append(copy.deepcopy(pattern))