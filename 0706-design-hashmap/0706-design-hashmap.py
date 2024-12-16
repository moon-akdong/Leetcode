class ListNode:
    def __init__(self,key=None,val = None):
        self.key = key 
        self.value = val 
        self.next = None 
class MyHashMap(object):

    def __init__(self):
        self.size = 10000 
        # At most 10^4 calls will be made to put, get, and remove.
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hashKey = key % self.size 
        # 비어 있다면 삽입 
        
        if self.table[hashKey].value is None:
            self.table[hashKey] = ListNode(key,value)
            return 
        p = self.table[hashKey]
        while p:
            # 키가 동일 하다면 업데이트 
            if p.key == key:
                p.value = value
                return 
        # 동일하지 않다면 연결리스트 다음에 넣어주기 
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key,value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hashKey = key % self.size
        if self.table[hashKey].value is None:
            return -1 
        
        p = self.table[hashKey]
        while p:
            if p.key == key:
                return p.value 
            if p.next is None:
                return -1 
            p = p.next
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashKey = key % self.size
        # 아예 없는 경우
        if self.table[hashKey].value is None:
            return 
        # 있는데, 충돌이 없었던 key 
        p = self.table[hashKey]
        if p.key == key:
            self.table[hashKey] = ListNode(None) if p.next is None else p.next
            return 
        # 있는데, 충돌이 있었어서 뒤에꺼도 확인해야 되는 경우
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