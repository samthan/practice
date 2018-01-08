from array import *

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


class ArrayStack:

	def __init__(self):
		self.arr = [None] * 5
		self.capacity = 5
		self.size = 0
		self.top = self.arr[self.size]

	def add(self, data):
		if self.size == self.capacity:
			# print "expanding"
			self.capacity *= 2
			resize = [None] * self.capacity

			for i in range(self.size):
				resize[i] = self.arr[i]

			resize[self.size] = data

			self.size += 1
			self.arr = resize
		else:
			# print "within capacity"
			self.arr[self.size] = data
			self.size += 1

		self.top = self.arr[self.size - 1]

	def remove(self):
		self.arr[self.size - 1] = None
		self.size -= 1
		self.top = self.arr[self.size - 1]

	def empty(self):

		return self.size == 0

	def peek(self):
		return self.top

	def show(self):
		for i in reversed(self.arr):
			if i is not None:
				print i


a = ArrayStack()
for i in range(6):
	a.add(i)

# print a.peek()
a.show()
print "-------"
a.remove()
print a.peek()
a.show()
# s = Stack()

for i in range(5):
	a.remove()

print a.peek()
print a.empty()

# print s.empty()

# for i in range(10):
# 	s.add(i)

# for i in range(5):
# 	s.remove()