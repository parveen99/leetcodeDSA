#brute force -> time limit exceeded

def findDisappearedNumbersBrute(nums):
    res = []
    for i in range(0,len(nums)):
        if(i+1 not in nums):
            res.append(i+1)
    return res


nums = [1,1]
findDisappearedNumbersBrute(nums)



def findDisappearedNumbersOptimal(nums):
    


nums = [4,3,2,7,8,2,3,1]
findDisappearedNumbersOptimal(nums)




