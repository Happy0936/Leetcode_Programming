class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        num=0
        while x > 0:
            b = x % 10
            num=num*10+b
            x = x // 10
        num = sign*num

        if num>=-2**31 and num<=2**31-1:
            return num

        else:
            return 0

