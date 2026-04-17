# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the mid point (fast and slow pointer)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 2. reverse the right half of the list (reversal)
        new, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp
        
        slow.next = None
        
        # 3. traverse the left and the right half simultaneously and append each node alternatingly
        while head and new:
            l_temp, r_temp = head.next, new.next

            head.next = new
            new.next = l_temp

            head, new = l_temp, r_temp
            
        
        return






        
        
        
