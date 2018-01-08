from node import Node

class LinkedList:

	def __init__(self):
		self.length = 0
		self.head = None

	# adds to end
	def add(self, data):
		n = Node(data)

		if self.head is None:
			self.head = n
			self.length += 1
			return

		tmp = self.head

		while tmp.next:
			tmp = tmp.next

		tmp.next = n

		self.length += 1

	# add to beginning
	def add_start(self, data):
		n = Node(data)

		n.next = self.head
		self.head = n
		self.length += 1

	# add at nth position
	def add_at(self, data, n):
		if n > self.length:
			raise ValueError("not long enough")

		if n == 0:
			self.add_start(data)
		elif n == self.length:
			self.add(data)
		else:
			node = Node(data)
			tmp = self.head
			for i in range(n - 1):
				tmp = tmp.next

			a = tmp.next

			tmp.next = node
			node.next = a

			self.length += 1

	# removes last item
	def remove(self):

		if self.length == 0:
			return
		elif self.length == 1:
			self.head = None
			return

		tmp = self.head.next
		prev = self.head

		while tmp.next:
			prev = tmp
			tmp = tmp.next

		prev.next = None
		self.length -= 1

	def remove_at(self, n):
		if n > self.length:
			raise ValueError("list not long enough")
		if n == self.length:
			self.remove()

		pre = self.head
		nex = self.head.next

		for i in range(n - 1 - 1):
			pre = nex
			nex = nex.next

		pre.next = nex.next
		self.length -= 1

	def reverse_copy(self):
		prev = self.head
		curr = self.head.next

		prev.next = None

		while curr:
			tmp = curr.next
			curr.next = prev
			prev = curr
			curr = tmp

		a = LinkedList()
		while prev:
			a.add(prev)
			prev = prev.next
		
		return a


	[1, 2, 3, 4, 5]
	def rec_helper(self, curr, nex):
		if nex is None:
			return

		split = nex.next

		nex.next = curr
		curr = nex 
		self.head = nex

		self.rec_helper(curr, split)

	def reverse_copy_r(self):
		if self.length == 0:
			return LinkedList()
		elif self.length == 1:
			return
		else:
			curr = self.head
			nex = self.head.next
			curr.next = None
			self.rec_helper(curr, nex)

	def size(self):
		return self.length

	def start(self):
		return self.head

	def show(self):
		tmp = self.head

		while tmp:
			print tmp
			tmp = tmp.next

l = LinkedList()

for i in range(5):
	l.add(i)

l.show()
print "----"
# a = l.reverse_copy()
l.reverse_copy_r()
l.show()
# a.show()






