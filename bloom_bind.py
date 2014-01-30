class bloomBind:
	def __init__(self, key, name, wait):
		self.key = key
		self.value = 0
		self.name = name
		self.wait = wait
		
	def __str__(self):
		return "BIND: " + self.name + " -> " + self.key.__str__() + " (" + self.value.__str__() + ")"