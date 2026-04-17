# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lag, lead = head, head.next
        
        while lead and lead.next:
            if lead == lag:
                return True
            lead = lead.next.next
            lag = lag.next

        return False