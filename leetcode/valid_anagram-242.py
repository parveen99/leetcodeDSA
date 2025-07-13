#brute force hain 
'''
⏱Time Complexity:
	1.	sorted(s) — Sorting a string of length n takes O(n log n) time.
	2.	sorted(t) — Similarly, sorting string t of length m takes O(m log m).
	3.	join() — Joining takes O(n) and O(m) respectively.
	4.	Comparing s1 == s2 — Takes O(n) (or O(max(n, m)) in general case).

Total time complexity:
O(n log n + m log m)
(If both strings are the same length n, then it’s O(n log n).)
'''

'''
Space Complexity:
	1.	sorted() creates lists: O(n) and O(m)
	2.	join() creates new strings: O(n) and O(m)

Total space complexity:
O(n + m)

(Or O(n) if both strings are same length.)

'''

def valid_anagram_brute(s, t):
    s1= ''.join(sorted(s))
    s2 = ''.join(sorted(t))
    if(s1 == s2):
        return True
    else:
        return False



s = 'rat'
t = 'tar'

print(valid_anagram_brute(s,t))


# better approach using counter

'''
Counter(s) - O(n)
Counter(t) - O(m)

So Time -> O(n + m)

'''

from collections import Counter

def valid_anagram_better(s, t):
    if(Counter(s) == Counter(t)):
        return True
    else:
        return False

print(valid_anagram_better(s, t))