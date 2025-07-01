# Brute force -> O(n*m)

# n is the jewels and m is stones


# Optimal O(n+m)

'''
set(jewels) takes O(n) time to build — where n = len(jewels)

Iterating over stones is O(m) — where m = len(stones)

Each s in jewel_set is O(1) (average-case for sets)
'''
