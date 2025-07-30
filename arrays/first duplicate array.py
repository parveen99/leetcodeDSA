
def firstRepeated(arr):
    seen = {}
    for i in arr:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1


    for i,k in seen.items():
        if(k > 1):
            return arr.index(i) + 1
        
    return -1


print(firstRepeated([7 ,4, 0, 9, 4, 8, 8, 2, 4, 5, 5, 1]))
    
#Counter also works