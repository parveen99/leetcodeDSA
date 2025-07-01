#Brute Force -> n ** 2 approach
def two_sum_brute_force_1(nums, target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if(i!=j and nums[i]+nums[j]==target):
                return [i,j]



nums = [1,2,3,4]
target = 7
print(two_sum_brute_force_1(nums,target))



#Brute force -> slightly less than n ** 2 approach

def two_sum_brute_force_2(nums, target):
    for i in range(0, nums[i]):
        for j in range(i+1, nums[i]):
            if(nums[i]==nums[j]==target):
                return [i,j]

print(two_sum_brute_force_1(nums,target))


#Better solution -> Hashing -> HashMap -> Dict O(n log n) -> This is mostly good

def two_sum_better(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum_better(nums,target))

# Optimal -> Two pointers -> If you wanna find whether two sum is present or not then go for this, otherwise if they ask for indexes, 
# then HashMap is best, Two pointers in that case is a disaster

# For Two pointers, always sort or make sure if the input is sorted 
# here we only return if two sum is possible or not

def two_sum_optimal(nums,target):
    left = 0
    right = len(nums)-1
    while left< right:
        if(nums[left] + nums [right] == target):
            return "Yeah"
        elif(nums[left] < nums[right]):
            left += 1
        else: 
            right -=1
    return "No"


print(two_sum_optimal(nums,target))