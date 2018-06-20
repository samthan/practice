def merge(arr, start, mid, end):
	n1 = mid - start  + 1
	n2 = end - mid

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(n1):
		L[i] = arr[start + i]

	for j in range(n2):
		R[j] = arr[mid + 1 + j]

	i = j = 0
	k = start

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1

		k += 1

	while i < n1:
		arr[k] = L[i]
		k += 1
		i += 1

	while j < n2:
		arr[k] = R[j]
		k += 1
		j += 1

def mergeSort(arr, start, end):
	# print start, end
	if start >= end:
		return

	# overflow risk
	mid = start + ((end - start) / 2)

	mergeSort(arr, start, mid)
	mergeSort(arr, mid + 1, end)
	merge(arr, start, mid, end)




a = [4, 7, 1, 6, 5, 4, 2, 3]

mergeSort(a, 0, len(a) - 1)
print a






