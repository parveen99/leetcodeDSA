n = 5
0, 1, 1, 2, 3, 5, 8, ...

# O(n) - Time
def fiboOptimal(n):
    a, b = 0, 1
    for _ in range(0,n+1):
        print(a, end=" ")
        a, b = b, a+b


fiboOptimal(7)
print()

def fiboRecursive(n):
    if ( n == 1):
        return 1
    if ( n == 0):
        return 0
    return fiboRecursive(n-1)+fiboRecursive(n-2)


print(fiboRecursive(7))


'''

F(n) -> F(n-2) + F(n-1)

'''


'''

Base Case : gives value

Recursive Case : points to another box
'''