class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                c = c+1
                
        return c
