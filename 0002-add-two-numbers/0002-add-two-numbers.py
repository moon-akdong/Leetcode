# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sumNum = 0
            if l1:
                sumNum += l1.val
                l1 = l1.next
            if l2:
                sumNum += l2.val
                l2 = l2.next
            carry,Num = divmod(sumNum+carry,10)
            head.next = ListNode(Num) 
            # root랑 같은 객체를 참조하기 때문에 root에도 같은 값으로 들어감? 
            head = head.next # 이 친구 때문에 이해가 안되긴 하는데.. 여기서 root와 참조하는 값이 왜 아직 같지? 
        return root.next # head랑 같은 객체를 참조하고 있기 때문에? 
