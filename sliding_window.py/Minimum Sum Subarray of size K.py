'''Input:
nums = [1, 12, -5, -6, 50, 3]
k = 4'''


nums = [1, 12, -5, -6, 50, 3]
k = 2

# if you initialize minn as 0, then it won't consider the negative numbers, so initialize it as positive infinity
# floating-point constant ; infinitely large number; Time -> O(1); Space -> negligible
def optimal(nums, k):
    i,j,minn,summ = 0,0,float('inf'),0
    n = len(nums)
    while j < n:
        summ = summ + nums[j]
        if(j -i + 1 < k):
            j += 1
        elif( j - i + 1 == k):
            minn = min(minn, summ)
            summ = summ - nums[i]
            i = i + 1
            j = j + 1
    return minn


val = optimal(nums, k)
print(val)



def optimal_variation(nums, k):
    i,j,minn,summ, start_index = 0,0,float('inf'),0, 0
    n = len(nums)
    while j < n:
        summ = summ + nums[j]
        if(j -i + 1 < k):
            j += 1
        elif( j - i + 1 == k):
            if(summ < minn):
                minn = summ
                start_index = i

            summ = summ - nums[i]
            i = i + 1
            j = j + 1
    return nums[start_index: start_index+k]


val_1 = optimal_variation(nums, k)
print(val_1)




''''
🔁 Fixed-Window Pattern (Size = K)
	1.	Maximum Average Subarray of Size K
Given an array, find the subarray of size k with the maximum average.
	2.	Minimum Sum Subarray of Size K
Just like max, but for min sum instead.
	3.	Count Subarrays of Size K with All Distinct Elements
Like the one you just solved, but instead of max sum, just count how many such subarrays exist.
	4.	Max Frequency of Any Element in Subarray of Size K
In every subarray of size k, find the frequency of the most common element.
	5.	Longest Subarray with At Most K Distinct Elements
Variation: window size isn’t fixed, but you expand/contract based on distinct count.

⸻

🧪 With Additional Constraints:
	6.	Max Sum Subarray of Size K with No Repeating Digits
Like your earlier problem — sum only if subarray has all unique elements.
	7.	Maximum Even Sum Subarray of Size K
Only consider subarrays of size k with an even sum.
	8.	Sum of All Subarrays of Size K
Not just max/min — return the sum of every subarray of size k.


'''