class ListNode:
    def __init__(self,key=None,val = None):
        self.key = key 
        self.value = val 
        self.next = None 

class MyHashMap(object):

    def __init__(self):
        self.table = collections.defaultdict(ListNode)
        self.size = 1000

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return 
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value 
                return 
            if p.next is None:
                break 
            p = p.next
        p.next = ListNode(key,value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.size
        # 조회 하려는 키가 없는 경우 
        if self.table[index].value is None:
            return -1 
        # 키가 있는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value 
            p = p.next
        return -1 

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size 
        if self.table[index].value is None:
            return 
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        
        prev = p 
        while p:
            if p.key == key:
                prev.next = p.next 
                return 
            prev,p = p, p.next 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)