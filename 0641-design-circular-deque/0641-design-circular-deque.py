class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.head, self.rear = ListNode(None),ListNode(None)
        self.k,self.len = k,0
        self.head.right, self.rear.left = self.rear, self.head 

    def _add(self,node,new):
        n = node.right 
        node.right = new
        new.left,new.right = node,n
        n.left = new

    def _del(self,node):
        n = node.right.right
        node.right=n
        n.left = node

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head,ListNode(value))
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False
        self.len += 1 
        self._add(self.rear.left,ListNode(value))
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.len -=1 
        self._del(self.head)
        return True
        
    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.len -=1 
        self._del(self.rear.left.left)
        return True 

    def getFront(self):
        """
        :rtype: int
        """
        return self.head.right.val if self.len else -1 
        

    def getRear(self):
        """
        :rtype: int
        """
        return self.rear.left.val if self.len else -1 
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.k
        


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