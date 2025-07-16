import sys


def brute(n):
    val = 1
    for i in range(1, n+1):
        val *= i

    return val

res = brute(4)
print(res)



def recursion(n):
    if(n == 0):
        return 1

    return n * recursion(n-1)

print(recursion(5))

# 0! = 1; 1!= 1


# By default recursion limit is 1000
'''
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())
'''
