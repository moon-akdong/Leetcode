# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 팰린드롬 문제
        # 리스트에서는 슬라이딩으로 풀었음 
        # 연결 리스트 
        
        # fast-slow 풀이 
        slow = fast = head
        # 비교하기위한 연결리스트  
        rev = None
        # 조건1.
        while fast and fast.next:
            fast = fast.next.next
            # 조건3 - slow를 뒤집은 연결리스트
            rev,rev.next,slow = slow,rev,slow.next 
        
        # 조건2 
        if fast:
            slow = slow.next
        
        #조건3 
        while rev and rev.val == slow.val:
            slow,rev = slow.next, rev.next
        return not rev 
            

            

        
        