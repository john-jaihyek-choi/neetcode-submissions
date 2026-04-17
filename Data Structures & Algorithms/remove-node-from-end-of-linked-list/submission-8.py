# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Note:
            - remove nth node from the linked list
                - ex) if n = 2 where list = [1,2,3,4]
                    - 3 should be removed
        Intuition:
            - use lead pointer, then iterate til lead is None
                - initialize lead pointer at head
                - iterate n many times and traverse lead pointer
                - iterate lead and lag pointer while lead is valid
                - disconnect lag.next and connect with lag.next.next
        """

        dummy = ListNode(0, head)
        lag, lead = dummy, head
        for i in range(n-1):
            lead = lead.next

        while lead and lead.next:
            lag = lag.next
            lead = lead.next

        lag.next = lag.next.next

        return dummy.next