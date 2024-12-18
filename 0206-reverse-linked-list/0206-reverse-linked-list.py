# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        root = head 
        prev = None 

        while root:
            next,root.next = root.next, prev 
            # root = 1->None , next = 2->3->4->5
            prev , root = root , next
            # root = 2->3->4->5,prev : 1-> None 
        return prev 