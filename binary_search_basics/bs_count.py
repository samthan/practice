def bs_count_helper(arr, target, left):
	low = 0
	high = len(arr) - 1
	res = -1

	while (low <= high):
		mid = (low + high) / 2

		if arr[mid] == target:
			res = mid

			if left:
				high = mid - 1
			else:
				low = mid + 1
		elif arr[mid] > target:
			high = mid - 1
		else:
			low = mid + 1

	return res

def bs_count(arr, target):
	left = bs_count_helper(arr, target, True)
	right = bs_count_helper(arr, target, False)

	if left == -1 and right == -1:
		return 0
	elif left == -1 or right == -1:
		return 1
	else:
		return right - left + 1




a = [1, 2, 2, 2, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7, 7, 8, 9]

print bs_count(a, 2)
print bs_count(a, 1)
print bs_count(a, 3)
print bs_count(a, 5)
print "------------"
print bs_count(b, 7)
print bs_count(b, 10)
print bs_count(b, 4)
print bs_count(b, 2)
