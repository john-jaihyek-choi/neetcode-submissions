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
        slow, fast = head, head.next

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
        head1, head2 = head, reverted
        while head1 and head2:
            temp1, temp2 = head1.next, head2.next
            head1.next, head2.next = head2, head1.next
            head1, head2 = temp1, temp2

        
        return