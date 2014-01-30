import math

class bloomVector:
	def __init__(self, value1, value2):
		self.values = [value1, value2]
		
	def __getitem__(self, index):
		return self.values[index]
		
	def __setitem__(self, index, operand):
		self.values[index] = operand
		
		return self.values[index]
		
	def __add__(self, operand):
		return bloomVector(self.values[0] + operand[0], self.values[1] + operand[1])

	def __iadd__(self, operand):
		self.values[0] += operand[0]
		self.values[1] += operand[1]
		
		return self
		
	def __sub__(self, operand):
		return self.__add__(operand.__neg__)

	def __isub__(self, operand):
		return self.__iadd__(operand.__neg__)
		
	def __mul__(self, operand):
		return bloomVector(self.values[0] * operand, self.values[1] * operand)
		
	def __div__(self, operand):
		return self.__mul__(1.0 / operand)
		
	def __neg__(self):
		return bloomVector(-self.values[0], -self.values[1])
		
	def __str__(self):
		return "<" + self.values.__str__()[1:-1] + ">"
		
	def tuple(self):
		return (self.values[0], self.values[1])
		
	def distance(self, operand):
		return math.sqrt((self.values[0] - operand[0]) ** 2 + (self.values[1] - operand[1]) ** 2)
		
	def fastDistance(self, operand):
		return abs(self.values[0] - operand[0]) + abs(self.values[1] - operand[1])
		
	def zero(self):
		self.values = [0.0, 0.0]
		
	def unit(self):
		magnitude = self.fastDistance((0.0, 0.0))
		return bloomVector(self.values[0] / magnitude, self.values[1] / magnitude)