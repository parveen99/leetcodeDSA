def intersection(c, nums2):
    ans = []
    nums_1 = list(set(nums1))
    nums_2 = list(set(nums2))
    i, j = 0, len(nums_1)
    while(i<j):
        if(nums_1[i] in nums_2):
            ans.append(nums_1[i])
        i += 1
    return ans



nums1 = [1,2,2,1,6,7,8]
nums2 = [2,2,7,8]
intersection(nums1, nums2)