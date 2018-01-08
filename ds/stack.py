# stack implementation with list...kind of cheating
# stack supports 4 basic operations and is Last In First Out
class Stack:

	def __init__(self):
		self.top = None
		self.stack = []

	def add(self, data):
		self.stack.append(data)

	def remove(self):
		return self.stack.pop()

	def empty(self):
		return len(self.stack) == 0

	def peek(self):
		if not len(self.stack):
			raise ValueError("stack is empty")

		return self.stack[-1]

	def show(self):
		for i in reversed(self.stack):
			print i

s = Stack()

print s.empty()

for i in range(10):
	s.add(i)

for i in range(5):
	s.remove()