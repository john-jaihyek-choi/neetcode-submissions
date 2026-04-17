"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. create a deep copy of each node in the traversal to a dictionary
        copy = {None: None}
        node = head
        while node:
            val = node.val
            nxt = node.next
            random = node.random

            copied_node = Node(val, None, None)
            copy[node] = copied_node

            node = node.next

        # 2. iterate on the copy dictionary to set next and random
        cur = head
        while cur:
            copied_node = copy[cur]
            copied_node.next = copy[cur.next]
            copied_node.random = copy[cur.random]
            cur = cur.next

        return copy[head]
        


        