class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z=x
        a=0
        while x>0:
            b=x%10
            a=a*10+b
            x=x//10

        if a==z:
            return True
        else:
            return False  