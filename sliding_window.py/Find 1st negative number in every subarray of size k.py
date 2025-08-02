'''

Input:
nums = [12, -1, -7, 8, 15, 30, 16, 28]
k = 3

Output:
[-1, -1, -7, 0, 0, 0]

'''


def sliding_brute(nums, k):
    b = []
    for i in range(0, len(nums)-k+1):
        for j in range(i, i+k):
            if(j-i+1 == k):
                print(nums[i:j+1])
                temp = nums[i: j+1]
                f = False
                for i in temp:
                    if(i < 0):
                        b.append(i)
                        f = True
                        break
                if f == False:
                    b.append(0)

    return sliding_brute

    

def optimal(nums, k):
    i,j = 0,0
    res = []
    while (j < len(nums)):
        j = j + 1
        if(j - i + 1 < k):
            print(j)
            if(nums[j] < 0):
                res.append(nums[j])
        # elif(j - i + 1 == k):
        #     i = i + 1


    print(res)


        




optimal([12, -1, -7, 8, 15, 30, 16, 28], 3)

# sliding_brute([12, -1, -7, 8, 15, 30, 16, 28], 3)