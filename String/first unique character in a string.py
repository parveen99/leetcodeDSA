'''
Input: s = "leetcode"

Output: 0

'''




def firstUniqChar(s):
    seen = {}
    for i in s:
        if(i in seen):
            seen[i] = seen[i] + 1 
        else:
            seen[i] = 1
    for i,j in seen.items():
        if j == 1:
            return s.index(i)
    return -1

print(firstUniqChar("leetcode"))