class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Fast and slow pointer to detect cycle, then using 2 pointers to find the beginning of the cycle
            # initialize a fast and slow pointer
                # slow = 0
                # fast = 0
            # while True:
                # slow = nums[slow]
                # fast = nums[nums[fast]]
                    # Note: nums[nums[fast]] DOES NOT literally jump 2 indicies at a time, it simply COVERS MORE GROUND than slow
                        # So at some point, the fast and slow will intersect
            # set a head starting point (beginning of a linked list)
                # head = 0
            # set a detected cycle point
                # cycle_pointer = slow
            #  while cycle_pointer != head:
                # set head to nums[head]
                # set cycle_pointer to nums[cycle_pointer]

            fast, slow = 0, 0
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break
            
            head, cycle_head = 0, slow
            while head != cycle_head:
                head = nums[head]
                cycle_head = nums[cycle_head]
            
            return cycle_head