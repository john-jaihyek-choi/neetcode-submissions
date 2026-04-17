# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Intuition:
            - find mid point, reverse the last half, then alternatingly merge
        """

        # find mid point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        reverted, cur = None, slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = reverted
            reverted = cur
            cur = temp
        
        # alternate
        left, right = head, reverted
        while left and right:
            temp1, temp2 = left.next, right.next
            left.next, right.next = right, left.next
            left, right = temp1, temp2

        
        return