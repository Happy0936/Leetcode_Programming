class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod=1
        arr=[]
        a=0
        for i in range (len(nums)):

            if nums[i]==0:
                a=a+1
            else:
                prod =prod*nums[i]             
        for i in range (len(nums)):
            if a>1:
                arr.append(0)

            elif nums[i]==0:
                val= prod
                arr.append(val)
            else:  
                if a==1:
                    arr.append(0)
                else:    
                    val= prod // nums[i]
                    arr.append(val)
        return arr        