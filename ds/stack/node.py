class Node:

	def __init__(self, data_):
		self.data = data_
		self.next = None

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		__repr__ = __str__