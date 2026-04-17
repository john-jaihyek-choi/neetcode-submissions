# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative:
        new, cur = None, head

        # p  c  n
        #   [0, 1, 2, 3]
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp
        
        return new
