'''
input -> [1, 2, 3, 4, 5]  
output -> [2, 3, 4, 5, 6]  
'''

# def manipulate(a):
#     b = []
#     for i in a:
#         b.append(i+1)
#     return b


def manipulate(a):
    return [i+1 for i in range(1, len(a))]


# print(manipulate(a))


'''
input -> [1, 2, 3, 4, 5]
output -> [5, 4, 3, 2, 1]
'''


def reverse_1(a):
    b = []
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    return b


def reverse_2(a):
    b = []
    for i in range(0, len(a)):
        b.insert(0, a[i])
    return b


a = [1, 2, 3, 4, 5]
print(reverse_1(a))
print(reverse_2(a))
