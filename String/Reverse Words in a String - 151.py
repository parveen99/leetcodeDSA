'''
Input: s = "the sky is blue"
Output: "blue is sky the"

'''


def reverse_words(s):
    new = s.split()
    i , j = 0, len(new)-1
    while(i < j):
        print(new[i])
        print(new[j])
        new[i], new[j] = new[j], new[i]
        i += 1
        j -= 1
    return ' '.join(new)




print(reverse_words("  hello world  "))