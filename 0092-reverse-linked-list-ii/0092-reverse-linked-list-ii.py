# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 예외
        if not head or left == right:
            return head

        start = root = ListNode(0) # range 오류 
        root.next = head
        # start
        for _ in range(left-1): 
            start = start.next 
 
        # tmp,end 
        # tmp - 넘어와야할 지점 
        # end - 어디까지 위치변경이 되었는지! 
        end = start.next
        for _ in range(right-left):
            tmp, start.next, end.next = start.next , end.next , end.next.next
            start.next.next = tmp
            #print('start :',start,"tmp",tmp,"end",end)
        return root.next

        