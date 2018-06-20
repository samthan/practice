def getPivot(first, last):
	return (first + last) / 2
	# return first

def partition(arr, first, last):
	idx = getPivot(first, last)
	pivot = arr[idx]
	left = first
	right = last

	while left < right:
		while arr[left] <= pivot and left < right:
			left += 1
		while arr[right] > pivot:
			right -= 1

		if left < right:
			arr[left], arr[right] = arr[right], arr[left]


	arr[idx], arr[right] = arr[right], arr[idx]
	print "left, right", left, right
	print pivot, arr
	return right

# To handle duplicates in quicksort, you need to do it from 
# start - pivot - 1 and pivot + 1 to end

def quicksort(arr, left, right):
	if left >= right:
		return

	index = partition(arr, left, right)
	# print index, arr
	quicksort(arr, left, index - 1)
	quicksort(arr, index + 1, right)


def main():
	a = [1, 3, 4, 6, 7, 3, 2, 3, 3]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	c = [1, 3, 5, 8, 7, 9, 6, 2, 8]
	d = [6, 4, 7, 8, 2, 3, 0, 9, 1]
	e = [1, 1, 1, 1, 1, 1, 1, 1, 1]
	f = [None, 25, 20, 26, 26, 0, 162, 25]
	g = [4, 5, 6, 1, 3, 2, 9, 8, 12, 11]
	h = [1, 6, 5, 3, 4]
	i = [1, 3, 1, 6, 5, 3, 4, 3]
	j = [5, 5, 5, 1, 4, 3, 2, 2, 1, 9]

	# quicksort(i, 0, len(i) - 1)
	quicksort(j, 0, len(j) - 1)
	print j



if __name__ == "__main__":
	main()