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
        # Each copied node to dictionary, then reassign next and random approach:
            # initialize an initial dictionary with {None: None} dictionary to store the copied_nodes (node_dict)
            # cur = head
            # iterate on cur while valid:
                # create a new node with val as cur.val (copied_node)
                # store the copied_node as a value in a dictionary (node_dict) with key as cur
            # new_head = lag = ListNode(None, head)
            # lead = lag.next
            # iterate while lead is valid:
                # new_node = node_dict[lead]
                # new_node.next = node_dict[lead.next]
                # new_node.random = node_dict[lead.random]
                # temp = lag.next
                # lag.next = new_node
                # lead = lead.next
                # lag = temp
            # return new_head.next

            # tail_node = None
            node_dict = dict({None: None})
            cur = head
            while cur:
                node_dict[cur] = Node(cur.val)
                cur = cur.next

            cur = head
            while cur:
                new_node = node_dict[cur]
                new_node.next = node_dict[cur.next]
                new_node.random = node_dict[cur.random]
                cur = cur.next

            return node_dict[head]

