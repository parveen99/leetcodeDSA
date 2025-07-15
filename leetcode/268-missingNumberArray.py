def missingNumberArrayBrute(nums):
    seen= {}

    for num in nums:
        seen[num] = True

    for i in range(0, len(nums)+1):
        if(i not in seen):
            return i


'''

O(n) -> traversing the array
O(1) -> adding element to dict
O(n) -> looping through and checking

in total Time -> O(n)

Space - O(n) -> storing in dict

'''

nums = [0,3,1]
res = missingNumberArrayBrute(nums)
print(res)


'''
Now do it in O(n) -> Time and O(1) -> Space
Which means without using any extra space
'''

