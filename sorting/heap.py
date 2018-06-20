import heapq
# def heapify(i):
# 	sp = swap(i, min(2 * i + 1, 2 * i + 2))

# 	if (sp != -1):
# 		heapify(sp)

# def buildHeap(arr, n):

# 	for i in range(n / 2, -1, -1):
# 		heapify(i)


# # def delete_min(arr):
# # 	elt = arr[0]
# # 	swap(arr, 0, h.size)
# # 	h.size -= 1
# # 	heapify(0)
# # 	return elt

# # todo
# # insert, use reverseheapify

# def reverseHeapify(i):
# 	sp = swap(i, min(i, (i - 1) / 2))

# 	if sp != -1:
# 		reverseHeapify(sp)


# def heapSort(arr, n):
# 	buildHeap(arr, n)

# 	for i in range(arr):
# 		delete_min(arr)

# 	return arr.reverse()


def mergeArrays(arr):
        
    max_heap = False
    
    if arr[0][0] > arr[0][-1]:
        max_heap = True
        
    
    temp = arr[0]
    for i in range(1, len(arr)):
        temp += arr[i]
        
    if not max_heap:
        heapq.heapify(temp)
    else:
        heapq._heapify_max(temp)
    
    res = []
    while temp:
        if not max_heap:
            res.append(heapq.heappop(temp))
        else:
            res.append(heapq._heappop_max(temp))
        
    return res


res = mergeArrays([[26, -15, -20], [27, 19, -18]])
print res
