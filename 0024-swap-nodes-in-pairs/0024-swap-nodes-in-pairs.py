# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            p = head.next
            # 백트래킹 되면서 넘어오는 곳 
            head.next = self.swapPairs(p.next)
            # 페어로 뒤집히는 곳 
            p.next = head 
            return p # 4->3->none 

        return head 

        # 반복풀이 
        # root=prev = ListNode(None)
        # # 연결리스트 이기 때문에
        # while head and head.next:
        #     # 페어의 두번째 값 
        #     b = head.next
        #     # 페어가 가리키는 값이 head가 가리키게 만들기 1->3->4
        #     head.next = b.next
        #     # 순서 뒤바꾸기 2->1->3->4
        #     b.next = head
            
        #     prev.next = b # None->2->1->.. 
        #     head = head.next # 3->4
        #     prev = prev.next.next # prev = 1 위치

        # return root.next if root.next else head


            
        