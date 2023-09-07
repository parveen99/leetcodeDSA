class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        max_count = 0
        for i in nums:
            if(i == 1):
                c = c+ 1
            else:
                max_count = max(max_count, c)
                c=0
                
        return max(max_count, c)
                
            
        
        
        
