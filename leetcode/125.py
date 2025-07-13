'''
isalnum() return a boolean True only if the character is a alphabest or numeric

Why we need internal while , as it helps skips comparison of 
'''
def isPalindrome(s):
    i , j = 0, len(s)-1
    while i<j:
        while i<j and not s[i].isalnum():
            i = i+1
        while i<j and not s[j].isalnum():
            j = j-1
        if s[i].lower() != s[j].lower():
            return False
        i , j = i+1, j-1
    return True
    

print(isPalindrome("A man, a plan, a canal: Panama"))
