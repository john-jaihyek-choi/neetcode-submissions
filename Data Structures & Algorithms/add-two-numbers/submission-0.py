# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = cur = ListNode()
        carry_over = 0
        while l1 or l2 or carry_over:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            sum = l1_val + l2_val + carry_over
            
            carry_over = sum // 10
            cur.next = ListNode(sum % 10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return new_node.next

