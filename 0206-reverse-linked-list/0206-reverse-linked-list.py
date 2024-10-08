# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 새로운 저장소 
        l1 = None
        while head:
            # l1.val을 하면 오류가 나는데? - l1.val이 None이기 떄문에
            # l1.val,l1.next,head = head.val, l1,head.next
            head.next,next = l1,head.next 
            l1,head = head, next
        return l1 

