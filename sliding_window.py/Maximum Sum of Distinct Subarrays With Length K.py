
from collections import defaultdict
# we need a hashmap here, not just a hashset
nums = [1,5,4,2,9,9,9]
k = 3
def optimal(nums, k):
    i,j,summ, maxx = 0,0,0,0
    seen = defaultdict(int)


    while (j < len(nums)):
        summ = summ + nums[j]
        seen[nums[j]] += 1
        if(j - i + 1 < k): # until it reaches window size 
            j = j + 1
        elif( j - i + 1 == k): # reaches window size 
            if(len(seen) == k): # add to maxxx only if distinct
                maxx = max(summ, maxx)
            summ = summ - nums[i] 
            seen[nums[i]] -= 1
            if(seen[nums[i]] == 0):
                seen.pop(nums[i])
            i = i + 1 # to maintain window size
            j = j + 1 # to maintain window size
    return maxx

    





res_1 = optimal(nums, k)
print(res_1)