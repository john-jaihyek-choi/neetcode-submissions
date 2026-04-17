# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer approach:
            # initialize fast and slow to head
            # iteratate while fast and fast.next is valid:
                # traverse fast twice as fast as slow
                # traverse slow at normal pace
                # if fast == slow
                    # return True
            # return False

        # fast, slow = head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        #     if fast == slow:
        #         return True

        # return False

        # less efficient hash approach:
            # initialize an empty dictionary to hash the nodes
            # set a cur to iterate on, starting from head
            # while cur is valid:
                # if cur.next is in dictionary:
                    # return True
                # store the cur node to the dictionary
                # traverse the cur to cur.next
            # return false

        node_map = {}
        cur = head
        while cur:
            if cur.next in node_map:
                return True
            node_map[cur] = None
            cur = cur.next
        
        return False



        