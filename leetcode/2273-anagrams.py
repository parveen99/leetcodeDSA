from collections import Counter

'''
note: dont store len of words outside the condition, while the problems 
involves removing elements
'''


class Solution(object):
    def removeAnagrams(self, words):
        i = 1
        while (i < len(words)):
            if (Counter(words[i-1]) == Counter(words[i])):
                words.pop(i)
            else:
                i += 1
        return words


s = Solution()
words = ["yjonq", "yqnoj", "oyqjn", "nqoyj",
         "onjqy", "joqyn", "qynjo", "jynoq"]
result = s.removeAnagrams(words)
print(result)
