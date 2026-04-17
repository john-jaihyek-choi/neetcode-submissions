# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #  -1    0  1  2  3    4
        # None [ 1, 2, 3, 4 ] None
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head