#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Ex:
# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.


# use a map to keep track of characters seen.  If character is already in map, then 
# mark it as true, otherwise, default is false
# iterate through s second time, return idx of first character that is false in map
def firstUniqChar(s):
    chars = {}
    for c in s:
        if c in chars:
            chars[c] = True
        else:
            chars[c] = False
    
    for i in range(len(s)):
        if chars[s[i]] == False:
            return i
    
    return -1

s = "leetcode"
print firstUniqChar(s)

s = "loveleetcode"
print firstUniqChar(s)