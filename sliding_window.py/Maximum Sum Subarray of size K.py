'''Input:
nums = [1, 12, -5, -6, 50, 3]
k = 4'''

#maximum sum of a subarray
# fixed length sliding window

"""
Python Initialization Values Reference
=====================================

MAX VALUE / SUM (General case)
Goal: Find maximum value or calculate running sum
Use: float('-inf') | negative infinity, infinetly larger number
Why: Safe default that works with any numeric comparison, clean initialization

MIN VALUE / SUM (General case) 
Goal: Find minimum value or calculate running sum
Use: float('inf') | positive infinity
Why: Same idea as max - safe default for any numeric comparison

FIRST ELEMENT INITIALIZATION
Goal: You want to use the first element as starting point
Use: nums[0] 
Why: Fine when array is guaranteed to be non-empty and safe to access

Usage Examples:
max_val = float('-inf')  # For finding maximum
min_val = float('inf')   # For finding minimum  
start = nums[0]          # When first element is safe to use
"""


nums = [1, 12, -5, -6, 50, 3]
k = 4
def optimal(nums, k):
    i,j,summ, maxx = 0,0,0,0
    n = len(nums)

    while j < n:
        summ = summ + nums[j]
        if(j - i + 1 < k):
            j += 1
        elif(j - i + 1 == k):
            maxx = max(summ, maxx)
            summ = summ - nums[i]
            i += 1
            j += 1
    return maxx

res = optimal(nums, k)
print(res)


# variation = I want the subarray that gives the maximum sum

    

def optimal_variation(nums, k):
    i,j,summ, maxx, start_index = 0,0,0,0, 0
    n = len(nums)

    while j < n:
        summ = summ + nums[j]
        if(j - i + 1 < k):
            j += 1
        elif(j - i + 1 == k):
            if( summ > maxx):
                maxx = summ
                start_index = i
            summ = summ - nums[i]
            i += 1
            j += 1
    return nums[start_index: start_index+k] #if you do [i: j+1] this will only give you last window, not the correct window

res_1 = optimal_variation(nums, k)
print(res_1)


# if they want last subarray of window size k -> [-k:]
# if they want first subarray of window size k -> [0: k]