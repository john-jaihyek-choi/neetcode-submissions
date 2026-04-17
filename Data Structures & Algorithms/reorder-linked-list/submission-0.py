# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        new, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp

        right = new
        left = head
        slow.next = None

        while left and right:
            l_temp = left.next
            r_temp = right.next

            left.next = right
            right.next = l_temp

            left = l_temp
            right = r_temp
        
        
