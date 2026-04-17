# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        new, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp

        slow.next = None
        left, right = head, new

        while left and right:
            l_temp, r_temp = left.next, right.next

            left.next = right
            right.next = l_temp

            left, right = l_temp, r_temp
        
        return
        
        
