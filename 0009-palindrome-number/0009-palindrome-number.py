class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        n=x
        b=0
        while n>0:
            a=n%10
            b=b*10+a
            n=n//10
        if b==x:
            return True
        else:
            return False        