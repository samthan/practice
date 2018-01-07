# iterative and recursive implementations of binary search in a sorted array

# returns index of element if found in array, else -1
def bsi(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) / 2

		if arr[mid] == target:
			return mid
		elif target < arr[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return -1

def bsr(arr, tar, low, high):
	if low > high:
		return -1

	mid = (low + high) / 2

	if arr[mid] == tar:
		return mid
	elif tar < arr[mid]:
		return bsr(arr, tar, low, mid - 1)
	else:
		return bsr(arr, tar, mid + 1, high)



a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [3, 5, 7, 9, 10, 22, 13]
c = [1, 1, 1, 1, 1, 2, 3, 5]

print bsi(a, 3)
print bsi(a, 7)
print bsi(a, 9)
print bsi(b, 22)
print bsi(b, 3)
print bsi(c, 1)
print "------"
print bsr(a, 3, 0, 7)
print bsr(a, 7, 0, 7)
print bsr(a, 9, 0, 7)
print bsr(b, 22, 0, 7)
print bsr(b, 3, 0, 7)
print bsr(c, 1, 0, 7)
