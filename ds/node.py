class Node:

	def __init__(self, data_):
		self.data = data_
		self.next = None

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		__repr__ = __str__

# Linked Lists

# Advantages
# - Linked lists are dynamic data structures
# 	- they are allowed to grow and be pruned during runtime
# - Insertion and deletion are easily implemented
# - Other DS can be implemented with linked lists
# - Don't need to predefine linked list size


# Disadvantages
# - Use more memory than arrays because of pointer size
# - Only offer sequential access, no random memory access
# - Nodes stored incontiguously in memory, can affect access time
# - Difficult to traverse in reverse if singly linked, adding reverse pointer also increases memory size


#######################################################


# Arrays

# Advantages

