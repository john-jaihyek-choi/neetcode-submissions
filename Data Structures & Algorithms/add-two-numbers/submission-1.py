# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize a new_node to append the nodes to (new_node)
            # new_node = node = ListNode()
        # initialize a carry over to 0 (carry_over)
        # while l1 or l2 or carry_over is non-empty/valid:
            # set l1_val equal to l1.val if l1 is valid, else 0
            # set l2_val equal to l2.val if l2 is valid, else 0

            # sum_val = l1_val + l2_val + carry_over

            # carry_over = sum_val // 10

            # node.next = ListNode(sum_val % 10)

            # l1 = l1.next
            # l2 = l2.next

        # return new_node.next

        new_node = node = ListNode()
        carry_over = 0
        while l1 or l2 or carry_over:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = l1_val + l2_val + carry_over
            carry_over = sum_val // 10
            
            node.next = ListNode(sum_val % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            node = node.next

        return new_node.next