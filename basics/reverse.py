# 1) Using reverse() function - reverses the OG array
def reverse_array_using_reverse(nums):
    nums.reverse()
    return nums

nums_1 = [8,4,6,3,2,1]
print("1",reverse_array_using_reverse(nums_1))



# 2) Using reversed(), reverses and returns an iterable, remember the <list_reverseiterator object at 0x1046c33d0>
def reverse_using_reversed(nums):
    new = reversed(nums)
    return list(new)

nums_2 = [8,4,6,3,2,1]
print("2",reverse_using_reversed(nums_2))


# 3) Using slice, learn slicing
def reverse_using_slice(nums):
    return nums[::-1]

nums_3 = [8,4,6,3,2,1]
print("3",reverse_using_slice(nums_3))


# 4) Using loop , new loop
def reverse_using_loop_new_array(nums):
    new_arr = []
    for a in nums:
        new_arr.insert(0,a)
    return new_arr

nums_4 = [8,4,6,3,2,1]
print("4",reverse_using_loop_new_array(nums_4))


# 5) Using loop, in-place reverse
def reverse_using_loop_in_place(nums):
    start = 0
    end = len(nums)-1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end -=1
    return nums

nums_5 = [8,4,6,3,2,1]
print("5",reverse_using_loop_in_place(nums_5))
