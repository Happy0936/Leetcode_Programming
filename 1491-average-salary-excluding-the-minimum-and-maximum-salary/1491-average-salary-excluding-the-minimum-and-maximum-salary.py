class Solution:
    def average(self, salary: list[int]) -> float:
        sum=0
        a=min(salary)
        b=max(salary)
        for i in range (len(salary)):
            sum=sum+salary[i]

        return ((sum-a-b)/(len(salary)-2))    
       