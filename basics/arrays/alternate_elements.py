# 1) Using even index approach
def alternate_elements_using_even_index(nums):
    new_arr = []
    for index,value in enumerate(nums):
        if(index)%2 == 0:
            new_arr.append(value)
    return new_arr

# Note: enumerate is slightly more efficient than range


nums_1 = [3,5,2,1,90,67.43, -4]
print(alternate_elements_using_even_index(nums_1))


# 2) using incremental operator approach
def alternate_elements_incremental_operator(nums):
    new_arr = []
    for i in range(0,len(nums),2):
        new_arr.append(nums[i])
    return new_arr

nums_2 = [3,5,2,1,90,67.43, -4]
print(alternate_elements_incremental_operator(nums_2))