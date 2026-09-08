class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        for i in range (len(nums)):
            arr.append(nums[i]*nums[i])
        arr.sort()
        return arr    