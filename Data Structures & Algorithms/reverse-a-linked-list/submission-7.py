# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iterative:
        # new, cur = None, head
        # # n  c  t
        # #   [3, 2, 1, 0]
        # while cur:
        #     temp = cur.next
        #     cur.next = new
        #     new = cur
        #     cur = temp

        # return new

        # recursive:
        if not head or not head.next:
            return head
        
        # #          h  nh 
        # #   [3, 2, 1, 0]
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head

