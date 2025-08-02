'''
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def optimal(haystack, needle):
    i = 0
    j = len(needle)

    while ( j < len(haystack)+ 1):
        if(haystack[i: j] == needle):
            return i
        i = i + 1
        j = j + 1
    return -1
    




print(optimal('sadbutsad', 'but'))