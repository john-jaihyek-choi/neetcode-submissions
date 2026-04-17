# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Node to Array, then merge approach
        # iterate on the input head to tail and store each node in an array
        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next
        # iterate on the array with two pointer l and r
        l, r = 0, len(node_list) - 1
        while l < r:
            left = node_list[l]
            right = node_list[r]

            temp = left.next
            left.next = right
            right.next = temp

            l += 1
            r -= 1
        # once iteration is complete, disconnect the left-end pointer
        node_list[l].next = None

        return 
        
        
        
