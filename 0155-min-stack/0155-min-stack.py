class MinStack(object):

    def __init__(self):
        self.st=[]
        self.min=[]    

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.st)==0 or self.min[-1]>=value:
            self.min.append(value)
        self.st.append(value)

        

    def pop(self):
        """
        :rtype: None
        """
        q1=self.st.pop()
        q2=self.min[-1]
        if q1==q2:
            self.min.pop()
        

        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()