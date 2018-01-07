# counts number of times a sorted array is rotated to the right


# unique start element attribute is that right and left
# will be greater, return the index of that element
# python will allow us to index list[-1]
def count_helper(arr, n, low, high):
	if low > high:
		return -1

	mid = (low + high) / 2
	a = (mid - 1 + n) % n
	b = (mid + 1) % n

	if arr[a] > arr[mid] and arr[b] > arr[mid]:
		return mid
	
	left = count_helper(arr, n, low, mid - 1)
	right = count_helper(arr, n, mid + 1, high)

	return left if left != -1 else right


# recursive implementation
def count_rotation(arr):
	return count_helper(arr, len(arr), 0, len(arr) - 1)


def count_rotation_2(arr):
	low = 0
	high = len(arr) - 1
	n = len(arr)
	while low <= high:

		if arr[low] <= arr[high]:
			return low

		mid = (low + high) / 2
		a = (mid - 1) % n
		b = (mid + 1 + n) % n

		if arr[a] > arr[mid] and arr[b] > arr[mid]:
			return mid
		elif arr[mid] <= arr[high]:
			high = mid - 1
		else:
			low = mid + 1

	return -1


a = [5, 6, 7, 8, 1, 2, 3, 4]
b = [0, 1, 2, 3, 4, 5, 6, 7]
c = [8, 9, 10, 11, 2, 3, 4, 5]

# print count_rotation(a)
# print count_rotation(b)
# print count_rotation(c)

print count_rotation_2(a)
print count_rotation_2(b)
print count_rotation_2(c)




