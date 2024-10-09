# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 예외 
        if not head:
            return head
        odd = head
        even = even_head = head.next
        while even and even.next:
            odd.next , even.next = odd.next.next, even.next.next 
            odd,even = odd.next,even.next
            
        odd.next = even_head
        return head