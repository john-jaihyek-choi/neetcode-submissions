# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n == 1:
        #     return head.next

        lead = head
        for _ in range(1, n):
            lead = lead.next
        
        new_node = lag = ListNode()
        lag.next = head
        while lead and lead.next:
            lag = lag.next
            lead = lead.next

        print(lag.val)
        # print(lead.val)
        
        lag.next = lag.next.next

        return new_node.next