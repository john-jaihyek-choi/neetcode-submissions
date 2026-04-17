# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # # Node to Array, then merge approach (TC: O(m + n) / SC: O(m + n))
        # # iterate on the input head to tail and store each node in an array
        # node_list = []
        # node = head
        # while node:
        #     node_list.append(node)
        #     node = node.next
        # # iterate on the array with two pointer l and r
        # l, r = 0, len(node_list) - 1
        # while l < r:
        #     left = node_list[l]
        #     right = node_list[r]

        #     temp = left.next
        #     left.next = right
        #     right.next = temp

        #     l += 1
        #     r -= 1
        # # once iteration is complete, disconnect the left-end pointer
        # node_list[l].next = None

        # return 

        # Halve the list, reverse, then merge approach (TC: O(m + n) / SC: O(1) ))
        # Find the mid point in the list (fast slow pointers)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the right half of the list (LL reversal)
        new, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = new
            new = cur
            cur = temp
        
        # disconnect left-tail's next to None to prevent cycle
        slow.next = None
        left, right = head, new
        # iteraterate on left half and right half and rereference (lead lag pointer)
        
        while left and right:
            l_temp = left.next
            r_temp = right.next

            left.next = right
            right.next = l_temp

            left = l_temp
            right = r_temp

        return 
            
        


        
        
        
