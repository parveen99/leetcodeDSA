'''

Maximum Avg


'''


nums = [1, 12, -5, -6, 50, 3]
k = 4



def optimal(nums, k):
    i,j, summ, maxx = 0,0,0, float('-inf')
    n = len(nums)
    while j < n:
        summ = summ + nums[j]
        avg = summ / k
        if( j - i + 1 < k):
            j += 1

        elif( j - i + 1 == k):
            maxx = max(avg, maxx)
            summ = summ - nums[i]
            i += 1
            j += 1
    return maxx





val = optimal(nums, k)
print(val)




def brute(nums, k):
    





val_1 = brute(nums, k)
print(val_1)