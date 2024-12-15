class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k,self.present = k,0
        self.head,self.tail = ListNode(None),ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head 
    
    def _add (self,point,value):
        prev = point.right # tail 
        point.right = value
        value.left,value.right = point,prev 
        prev.left = value 

    def _del(self,point):
        prev = point.right.right
        point.right = prev 
        prev.left = point  

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        
        if self.isFull():
            return False 
        self._add(self.head,ListNode(value))
        self.present +=1 
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False 
        self._add(self.tail.left,ListNode(value))
        self.present +=1 
        return True 

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False 
        self._del(self.head)
        self.present-=1 
        return True
        
    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False 
        self._del(self.tail.left.left)
        self.present-=1 
        return True
        
    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1 
        return self.head.right.val
        
    def getRear(self):
        """
        :rtype: int
        """
        if self.present ==0:
            return -1 
        return self.tail.left.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.present == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.present == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()