class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        if nums[0]!=0:
            return 0
        for i in range (0,n):
            if nums[i] != i:
                return i
        return n
