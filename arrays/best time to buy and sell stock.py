'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''


def brute(nums):
    mini = min(nums)
    mini_index = nums.index(mini)
    if(len(nums) - (mini_index+1) > 0 ):
        maxi = max(nums[mini_index + 1: len(nums)])
        return maxi - mini
    return 0

    # not all conditions satisfied here

# satisfies all cases but time complexity is n**2
def brute_2(nums):
    maxx = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[j] > nums[i]):
                diff = nums[j] - nums[i]
                maxx = max(diff, maxx)
    return maxx



def optimal(nums):
    maxx = 0
    l, r = 0,1

    while(r < len(nums)):
        if(nums[l] < nums[r]):
            profit = nums[r] - nums[l]
            maxx = max(maxx, profit)
            r = r+1

        else:
            l = r
            r = r + 1
    return maxx








print(optimal([7,1,4,3]))

# print(brute_2([7,6,4,3,1]))
# print(brute([2,4,1]))