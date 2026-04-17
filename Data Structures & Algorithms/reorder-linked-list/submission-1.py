# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        node_list = []

        node = head
        while node:
            node_list.append(node)
            node = node.next
        

        # Utility.print_linked_list(node_list[0])
        # for node in node_list:
        #     print(node.val)

        # print(node_list)

        l, r = 0, len(node_list) - 1
        while l < r:
            l_temp = node_list[l].next

            node_list[l].next = node_list[r]
            node_list[r].next = l_temp
            
            l += 1
            r -= 1
        
        node_list[l].next = None
        
        return 
        
        
