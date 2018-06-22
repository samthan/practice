# Given an array of intergers where 1 <= a[i] <= len(a), some elements appear twice, while others
# appear once.
# Find all elements of [1, n] inclusive that do not appear in this array.
# Do it without extra space and in O(n) runtime.


# bruteforce: counting sort, take an array of size n, mark the idx where idx = val - 1, iterate over second array
# add the idx + 1 into the result list
def bruteforce(nums):
    a = [0] * len(nums)
    
    for i in range(len(nums)):
        a[nums[i] - 1] += 1
    
    res = []
    for i in range(len(a)):
        if a[i] == 0:
            res.append(i + 1)
    
    return res

# optimized: use the given array as the marking array: idx = nums[i] - 1; multiply that idx by -1 if the value at
# nums[idx] is not negative; iterate through 2nd time and add all indexes where the value at index is positive
def optimized(nums):
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0:
            nums[idx] *= -1
    
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    
    return res

def findDisappearedNumbers(nums):
    return optimized(nums)


a = [4, 3, 2, 7, 8, 2, 3, 1]
print findDisappearedNumbers(a)
