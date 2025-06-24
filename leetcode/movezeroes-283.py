def move_zeroes(nums):
    i, nonzero = 0, 0
    n = len(nums)
    while i < len(nums):
        if(nums[i] != 0):
            nums[i], nums[nonzero] = nums[nonzero], nums[i]
            nonzero += 1
        i += 1
    return nums



    #     if((num[right] != 0)):
    #         num.insert(left, num[right])
    #         num[right+1] = 0
    #         del num[right]
    #         left +=1
    #     right += 1
    # return num



num = [16, 0, 13, 0]
print(move_zeroes(num))