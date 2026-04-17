# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # lead and lag pointer
        # 1. iterate the head n many times and traverse the nodes (lead)
        lead = head
        for i in range(n):
            lead = lead.next

        # 2. traverse the lead and lag node until lag reaches the end of the list
        dummy = lag = ListNode(None, head)
        while lead:
            lead = lead.next
            lag = lag.next

        # 3. set lag.next to lag.next.next
        lag.next = lag.next.next

        return dummy.next