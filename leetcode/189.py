
# using slicing, extra memory -> time => O(n); space => O(n)
# copying the array and then doing it -> time => O(n); space => O(n)
# def rotateArrayExtraArray(nums, k):
#     copy = nums[:]
#     n = len(nums)
#     for i in range(0, n):
#         new_index = (i+k) % n
#         copy[new_index] = nums[i]
#     return copy

# print(rotateArrayExtraArray(nums, k))


#Both of the above are not inplace reversal -> time => O(n); space => O(1)
def rotateArrayInPlaceReversal(nums, k):
        k = k % len(nums)
        left, right = 0, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left, right = 0, k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left, right = k, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


nums = [1,2,3,4]
k = 1
print(rotateArrayInPlaceReversal(nums, k))