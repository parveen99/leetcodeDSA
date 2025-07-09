# brute force


def maximum_sum_brute(arr, k):
    m = []
    n = len(arr)
    for i in range(n):
        if (i+(k-1) < n):
            m.append(sum(arr[i: i+k]))
    return max(m)


arr = [8, 6, 7, 9, 10]
# print(maximum_sum_brute(arr, 3))


def maximum_sum_optimal(arr, k):
    i, j = 0, 0
    n = len(arr)
    summ = 0
    maxx = 0
    while j < n:
        summ = summ + arr[j]
        if ((j - i) + 1 < k):
            j += 1
        elif ((j - i) + 1 == k):
            maxx = max(maxx, summ)
            summ = summ - arr[i]
            i += 1
            j += 1
    return maxx


print(maximum_sum_optimal(arr, 3))
