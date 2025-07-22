def isSubsequenceBrute(s, t):
    for i in s:
        if (i not in t):
            return False
    return True


s = "abc"
t = "ahbgdc"

res = isSubsequenceBrute(s, t)
print(res)


def isSubsequenceOptimal(s, t):
    S = len(s)
    T = len(t)

    if (s == ""):
        return True
    if (S > T):
        return False
    j = 0

    for i in range(0, T):
        if (t[i] == s[j]):
            if (j == S-1):
                return True
            j += 1
    return True

# T -> O(n) => we traverse through array once
# S -> O(1) => we didnt use any datastructures


s = "abc"
t = "ahbgdc"

print(isSubsequenceOptimal(s, t))
