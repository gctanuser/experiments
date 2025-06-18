

class Tree:
	def __init__(self):
		self.G = None
	
	def compute(self, n : int, n2 : int) -> int:
		return n * n2


sampleTree = Tree()

print(sampleTree.compute(1,2))
