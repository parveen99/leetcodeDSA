#Reverse Words in a String III

'''
s = "Let's take LeetCode contest"
output "s'teL ekat edoCteeL tsetnoc"
'''

def reverseString(s):
    arr = s.split()
    print(arr)
    n = len(arr)
    res = []
    for word in arr:
        n = reversed(word)
        res.append(''.join(list(n)))
    return ' '.join(res)



'''

Operations:
	1.	s.split() → O(n)
	2.	Loop over k words and reverse each of them:
	•	Each word has length ≤ n, and the sum of all word lengths = O(n)
	•	So reversing each word: O(n)
	3.	' '.join(res) → O(n) to join all words with spaces

Total Time Complexity:
O(n) + O(n) + O(n) = \boxed{O(n)}

Space -> O(n)


'''
s = "Let's take LeetCode contest"
res = reverseString(s)
print(res)