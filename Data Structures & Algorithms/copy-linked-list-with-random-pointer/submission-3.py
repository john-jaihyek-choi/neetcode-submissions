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
            # create a tail node to use in a case of node.next or node.random being null (tail_node)
            # initialize an empty dictionary to store the copied_nodes (node_dict)
            # cur = head
            # iterate on cur while valid:
                # create a new node (copied_node)
                    # val = cur.val
                    # next = tail_node if cur.next is None, else cur.next.val
                    # random = tail_node if cur.random is None, else cur.random.val
                # store the copied_node as a value in a dictionary (node_dict) with key as cur.val
            # new_head = lag = ListNode(None, head)
            # lead = lag.next
            # iterate while lead is valid:
                # new_node = node_dict[lead.val]
                # new_node.next = tail_node if new_node.next is None, else node_dict[lead..next]
                # new_node.random = tail_node if new_node.next is None, else node_dict[lead.random]
                # temp = lag.next
                # lag.next = new_node
                # lead = lead.next
                # lag = temp
            # return new_head

            # tail_node = None
            node_dict = dict({None: None})
            cur = head
            while cur:
                # val = cur.val
                # nxt = None if not cur.next else cur.next.val
                # random = None if not cur.random else cur.random.val

                # copied_node = Node(val, nxt, random)
                # copied_node = Node(cur.val)
                node_dict[cur] = Node(cur.val)

                cur = cur.next

            new_head = lag = Node(0, head)
            lead = head
            while lead:
                new_node = node_dict[lead]
                new_node.next = node_dict[lead.next]
                new_node.random = node_dict[lead.random]

                temp = lag
                lag.next = new_node
                lead = lead.next
                lag = temp.next

            return new_head.next

