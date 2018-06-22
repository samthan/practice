# I pick a number from 1 to n.  Guess the number that I've picked
# Every time the guess is wrong, I till you -1 (<) or 1 (>). 0 if you guessed correctly
# With a predefined API call called guess(n), write a program to find the number that I've chosen

def guessNumber(self, n):
        
    def recursive_helper(low, high):
        if low == high:
            return low
        
        m = (low + high) / 2
        
        v = guess(m)
        if v == 0:
            return m
        elif v > 0:
            return recursive_helper(m + 1, high)
        else:
            return recursive_helper(low, m - 1)
    
    def iterative_helper(n):
        
        g = None
        low, high = 0, n
        while g != 0:
            m = (low + high) / 2
            
            g = guess(m)
            
            if g > 0:
                low = m + 1
            elif g < 0:
                high = m - 1
        
        return m
    
    return iterative_helper(n)