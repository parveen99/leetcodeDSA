#brute force

num = 89898
def bruteforce(num):
    rev = num[::-1]
    if(rev == num):
        return "YEAH"
    else:
        return "NAH"