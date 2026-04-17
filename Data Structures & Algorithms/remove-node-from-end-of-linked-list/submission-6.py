# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = head
        for _ in range(n):
            lead = lead.next
        
        new_node = lag = ListNode(0, head)
        while lead:
            lead = lead.next
            lag = lag.next
        
        lag.next = lag.next.next
        return new_node.next