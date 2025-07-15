def reverseVowels(s):
    left = 0
    right = len(s)-1
    s = list(s)
    vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while left < right:
        while left < right and s[left] not in vow:
            left += 1
        while left < right and s[right] not in vow:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


s = "a.b,."
print(reverseVowels(s))
