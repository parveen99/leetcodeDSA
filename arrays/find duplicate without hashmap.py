'''
Input:  [1, 2, 3, 2, 4, 5]
Output: [2]

'''


def duplicate(arr):
    res = []
    unique = []

    for i in arr:
        if i not in unique:
            unique.append(i)
        elif i not in res:
            res.append(i)
    return res




arr = [1, 2, 3, 2, 4, 5,2]

print(duplicate(arr))