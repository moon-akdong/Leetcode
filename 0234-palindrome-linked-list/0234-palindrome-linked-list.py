# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = []
        node = head
        rev = None
        # slow-fast 러너 풀이 
        fast = slow = node 
        while fast and fast.next:
            fast = fast.next.next
            rev,rev.next,slow = slow,rev,slow.next
        if fast:
            slow = slow.next 
        # 팰린드롬 판단 
        while rev and rev.val == slow.val:
            slow,rev = slow.next, rev.next
        return not rev 
