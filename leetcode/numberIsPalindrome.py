def brute(n):
    return str(n) == str(n)[::-1]

print(brute(1232))
#Time -> O(n), Space -> O(n)


def mathOnly(n):
    reversed_num = 0
    og = n

    # negative numbers can't be palindrome
    if(n < 0):
        return False
    while ( n > 0):
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    return og == reversed_num

print(mathOnly(12321))
