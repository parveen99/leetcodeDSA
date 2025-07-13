
# word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

'''
The reason we are choosing to not append to string is coz string is immutable 
any append operation would take O(n), but in array it will be O(1)
'''

def mergeAlternately(word1, word2):
    A , B = len(word1), len(word2)
    a, b = 0,0
    res = []
    word = 1
    while(a < A and b < B):
        if( word == 1):
            res.append(word1[a])
            a += 1
            word = 2
        else:
            res.append(word2[b])
            b += 1
            word = 1
    while a < A:
        res.append(word1[a])
        a += 1
    while b < B:
        res.append(word2[b])
        b += 1

    return ''.join(res)

    
        
word1 = "abc"
word2 = "pqre"
mergeAlternately(word1, word2)