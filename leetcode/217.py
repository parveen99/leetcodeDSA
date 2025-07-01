# HashMap -> O(n)

def containsDuplicate(nums):
    seen = {}
    for key,value in enumerate(nums):
        if (nums[key] in seen):
            return True
        else:
            seen[value] = 1
    return False


nums = [3,3]
print(containsDuplicate(nums))

#HashSet

'''
one loop through nums -> O(n)
set -> O(n)

O(n+n) -> O(2n) -> Drop constants -> O(n)
'''

def containsDuplicate(nums):
    sett = set()
    for i in nums:
        if i in sett:
            return True
        else:
            sett.add(i)
    return False


    







nums_1 = [4]
print(containsDuplicate(nums_1))

# uses sort -> O(n log n)

'''
nums.sort() takes O(n log n) time (Timsort in Python).

The for loop runs in O(n) time.

But since O(n log n) dominates O(n), the total time complexity is:
'''

def containsDuplicate(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

nums = [3,3]
print(containsDuplicate(nums))