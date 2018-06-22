# Dutch national flag problem
# Given array of reds, whites, and blues, sort them in place in the array
def dutch_national_flag(arr):
	i = j = 0
	k = len(arr) - 1

	while j <= k:
		if arr[j] < 1:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j += 1
		elif arr[j] > 1:
			arr[j], arr[k] = arr[k], arr[j]
			k -= 1
		else:
			j += 1

	return arr

arr = [0, 0, 1, 1, 2, 2]
print "before", arr
print dutch_national_flag(arr)
arr = [1, 0, 2, 2, 1, 0]
print "before", arr
print dutch_national_flag(arr)
arr = [1, 1, 1, 0, 2, 0]
print "before", arr
print dutch_national_flag(arr)
arr = [2, 2, 2, 1, 0, 0]
print "before", arr
print dutch_national_flag(arr)
