# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Note:
            - given 2 non-empty linked list
            - l1 and l2 can be of different length
            - l1 and l2 are reversed
                ex) if l1 = [1,2,3], l2 = [4,5,6]
                    then l1 = 321 and l2 = 654
            - Things to consider:
                - carryover
                    - best a number could get is 18 + 1 = 19
                - l1 and l2 are already reversed, so the output is already reversed too
        Intuition:
            - traverse l1 and l2 together, sum up the value, then keep carryover
                - initialize carryover to 0
                - initialize new head for the sum value
                - initialize head1 and head2
                - traverse while head1 and head2
                    - set new.val to (head1.val + head2.val) % 10 + carryover
                    - carryover = (head1.val + head2.val) // 10
                    - set head1 to head1.next
                    - set head2 to head2.next
                - extend new.next to head1 or head2
                - if there's carryover:
                    - set new.next.val += carryover
        """

        carryover = 0
        head1, head2 = l1, l2
        dummy = new = ListNode()
        
        while head1 or head2:
            h1 = head1.val if head1 else 0
            h2 = head2.val if head2 else 0
            sum_val = h1 + h2 + carryover
            print(sum_val)
            remainder = sum_val % 10
            carryover = sum_val // 10
            new.next = ListNode(remainder)
            new = new.next
            head1, head2 = head1.next if head1 else None, head2.next if head2 else None
        
        if carryover:
            new.next = ListNode(carryover)
        
        
        return dummy.next