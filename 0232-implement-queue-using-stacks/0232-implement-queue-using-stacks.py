class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = [] 

    def reverse(self):
        if not self.stack2:
            while self.stack1:
                last = self.stack1.pop()
                self.stack2.append(last)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        
        self.reverse()
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.reverse() 
        return self.stack2[-1]

        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1)==0 and len(self.stack2) ==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()