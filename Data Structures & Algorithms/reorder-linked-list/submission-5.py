# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle point
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 2. reverse the right halve
        new, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp
        
        # 3. clean up / cut off the left half end point
        slow.next = None
        left, right = head, new

        # 4. traverse the left and the right half together and append each nodes alternatingly
        while left and right:
            l_temp = left.next
            r_temp = right.next

            right.next = left.next
            left.next = right
            
            left = l_temp
            right = r_temp
            
        return




        
        
        
