class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return max(nums)
        elif k == 1:
            return nums
        
        output = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            # if q is non-empty AND the value in q[-1] (current minimum) is greater than nums[r], pop the q, then append the nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # if the current max is out of bounds (less than l), pop the q from the left to remove the max
            if l > q[0]:
                q.popleft()

            # if r - l + 1 (size of the window) has reached k, then start incrementing l pointer
            if r - l + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            
        return output
            
