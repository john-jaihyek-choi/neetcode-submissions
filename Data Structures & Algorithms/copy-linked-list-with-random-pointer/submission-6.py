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
        # traverse the head to store the nodes in dict
        # create new_node and append to it as traversing the head
        node_dict = {None: None}

        cur = head
        while cur:
            node_dict[cur] = Node(cur.val)
            cur = cur.next
        
        new_node = node = Node(0)
        cur = head
        while cur:
            copied_node = node_dict[cur]
            copied_node.next = node_dict[cur.next]
            copied_node.random = node_dict[cur.random]

            node.next = copied_node

            cur = cur.next
            node = node.next


        return new_node.next



        