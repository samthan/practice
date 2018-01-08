# find element in sorted circular array
def find_rot(arr, tar, n):
	low = 0
	high = n - 1

	while low <= high:


		mid = (low + high) / 2

		if arr[mid] == tar:
			return mid

		# if the right side is sorted
		if arr[mid] <= arr[high]:
			if tar > a[mid] and tar <= arr[high]:
				low = mid + 1
			else:
				high = mid - 1
		else:
			if arr[low] <= tar and tar < arr[mid]:
				high = mid - 1
			else:
				low = mid + 1
		# elif arr[low] <= arr[mid] and tar >= arr[low] and tar <= arr[mid]:
		# 	# print 'a'
		# 	high = mid - 1
		# elif arr[mid] <= arr[high] and tar >= arr[mid] and tar <= arr[high]:
		# 	# print 'b'
		# 	low = mid + 1
		# elif arr[low] > arr[mid]:
		# 	# print 'c'
		# 	high = mid - 1
		# else:
		# 	# print 'd'
		# 	low = mid + 1



	return -1





a = [5, 6, 7, 8, 9, 2, 3, 4]
b = [6, 6, 6, 7, 1, 2, 3, 4]
c = [2, 2, 2, 2, 2, 2, 0, 2]

print find_rot(a, 2, 8)
print find_rot(a, 4, 8)
print find_rot(a, 3, 8)
print find_rot(a, 5, 8)
print find_rot(a, 10, 8)
print "-----"
print find_rot(b, 6, 8)
print find_rot(b, 1, 8)
print find_rot(b, 7, 8)
print find_rot(b, 2, 8)
print "-----"
print find_rot(c, 2, 8)
print find_rot(c, 0, 8)
