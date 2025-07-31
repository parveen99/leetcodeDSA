# Time - O(n) and Space - O(1)

nums = [4,3,2,7,8,2,3,1]

def optimal(nums):
    res = []
    for i in nums:
        i = abs(i)
        if(nums[i-1] < 0):
            res.append(i)
        nums[i-1] = -nums[i-1]
        print(res)
    return res

            



print(optimal(nums))