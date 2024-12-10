class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.circular = [None] * k
        self.maxlen = k
        self.front = 0 
        self.rear = 0 
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.circular[self.rear] is None:
            self.circular[self.rear] = value 
            self.rear = (self.rear + 1) % self.maxlen

            return True
        else:
            return False 
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.circular[self.front] != None:
            self.circular[self.front] = None 
            self.front = (self.front +1) % self.maxlen
            return True
        else:
            return False

        

    def Front(self):
        """
        :rtype: int
        """
        if self.circular[self.front] == None:
            return -1 
        return self.circular[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.circular[self.rear-1] == None:
            return -1 
        return self.circular[self.rear-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.rear % self.maxlen == self.front % self.maxlen and None in self.circular:
            return True 
        else:
            return False


        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.rear % self.maxlen == self.front % self.maxlen and None not in self.circular:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()