from node import Node

# reverse string with stack
# kinda redundant but for demonstration purposes
def reverse(string):
	l = list(string)

	n = len(l)
	ans = ""
	for i in range(n):
		ans += l.pop()

	return ans

def reverse_linked(head):
	l = []

	while head:
		l.append(head)
		head = head.next

	ans = l[-1]

	while len(l):
		tmp = l[-1]
		l.pop()
		if len(l):
			tmp.next = l[-1]
		else:
			tmp.next = None

	return ans

def balanced_parens(arr):
	l = []

	for i in range(len(arr)):
		if arr[i] == '(':
			l.append(arr[i])
		else:
			if not len(l):
				return False
			l.pop()

	return True if len(l) == 0 else False


print balanced_parens("((((((((((")
print balanced_parens("((()))")
print balanced_parens("(()())")
print balanced_parens("()()()()()()")

# print reverse("GeeksForGeeks")
# print reverse('abcdefghijklmnopqrstuvwxyz')

# n = Node(0)
# a = n
# for i in range(1, 10):
# 	tmp = Node(i)
# 	n.next = tmp
# 	n = n.next

# a = reverse_linked(a)
# while a:
# 	print a
# 	a = a.next
