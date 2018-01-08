from node import Node

# queues are first in first out

class LinkedQueue:

	def __init__(self):
		self.front = None
		self.end = None

	def push(self, data):
		n = Node(data)

		if self.front is None:
			self.front = n
			self.end = n

		else:
			self.end.next = n
			self.end = n

	def remove(self):
		tmp = self.front

		self.front = self.front.next
		return tmp

	def peek(self):
		return self.front

	def empty(sefl):
		return self.front is None

	def show(self):
		tmp = self.front

		while tmp:
			print tmp
			tmp = tmp.next

q = LinkedQueue()

for i in range(10):
	q.push(i)

# print q.peek()
q.show()

print q.remove()
print q.peek()
print "---"

q.show()