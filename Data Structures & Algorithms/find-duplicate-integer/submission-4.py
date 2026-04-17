class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat the list similar to a linked list
        # 1. detect a cycle
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # 2. Once cycle is detected, use two pointers to traverse at the same speed
            # if two pointers meet, it represents the beginning of the loop
            # Floyd's Turtoise & Hare algorithm
        head, cycle_point = 0, slow
        while head != cycle_point:
            head = nums[head]
            cycle_point = nums[cycle_point]

        return cycle_point
        
