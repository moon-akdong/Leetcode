class MyQueue(object):

    def __init__(self):
        self.stack = [] 
        self.output = [] 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.output.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.output:
            while self.stack:
                self.output.append(self.stack.pop())
        return self.output[-1]
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.output) ==0 and len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()