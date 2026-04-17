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

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

        