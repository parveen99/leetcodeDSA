'''
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

'''
Traversing Array -> O(n)
Sort -> O(n log n)
Time complexity -> O(n log n)

Space -> O(n)

'''
class Solution:
    def sortedSquaresArrbrute(self, nums):
        ress = []
        for i in nums:
            ress.append((abs(i)) * abs(i))
        return sorted(ress)
    
    def sortedSquaresArrOptimal(self, nums):
        i , j = 0, len(nums)-1
        ress = []
        while (i <= j):
            if((nums[i]* nums[i]) > nums[j]* nums[j]):
                ress.append(nums[i]* nums[i])
                i += 1
            else:
                ress.append(nums[j]* nums[j])
                j -= 1
        return ress[::-1]


'''
reverse() takes O(n)-> Time and O(1) space as its in place

Here Time over all is -> O(n), space -> O(n)

'''





call = Solution()
nums = [-4,-1,0,3,10]
res = call.sortedSquaresArrbrute(nums)
res_1 = call.sortedSquaresArrOptimal(nums)
print(res)
print(res_1)