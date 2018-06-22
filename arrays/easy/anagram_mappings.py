# Given two lists A and B, B is an anagram of A.  This means that B is made by randomizing
# the order of the elements in A

# Find an index mapping, P, from A to B.  A mapping P[i] = j means that the ith element in A
# appears in B at index j

# These lists A and B may contain duplicates; if so, output any of the answers

# Ex:
# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]

# Return: [1, 4, 3, 2, 0]


def anagramMappings(A, B):
        
    # bruteforce: n^2 search.  for each value at A[i], search B for corresponding value and append j
    def bruteforce(A, B):
        res = []
        for i in range(len(A)):
            search = A[i]
            for j in range(len(B)):
                if B[j] == search:
                    res.append(j)
                    break
        
        return res
    
    # optimized, use a hash table keep track of values and indices, make 3 traversals 1 - get values, 2 - get indices, 3 - get results
    def optimized(A, B):
        idxes = dict()
        res = []
        # get values
        for i in range(len(A)):
            if A[i] not in idxes:
                idxes[A[i]] = -1
        
        # get idxes of values
        for j in range(len(B)):
            idxes[B[j]] = j
        
        for k in range(len(A)):
            res.append(idxes[A[k]])
        
        return res
    
    return optimized(A, B)

