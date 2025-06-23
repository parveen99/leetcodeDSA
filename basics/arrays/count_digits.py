import math

# Count digits in a number


num = 89763
# Brute Force
def function_brutal(num):
    c = 0
    while num>0:
        c+=1
        num = num//10
    return c

print(function_brutal(num))

# Optimal 
# int is better than floor , as floor needs a math import
def optimal(num):
    return (int(math.log10(num)+1))

print(optimal(num))