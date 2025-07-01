def repeatedCharacter(s):
    seen = {}
    for i in s:
        if i in seen:
            return i
        seen[i] = 1



s = "abcdd"
print(repeatedCharacter(s))