from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l, r = 0, 0
        while r < len(nums):
            if q and nums[q[-1]] < nums[r]:
                while q and nums[q[-1]] < nums[r]:
                    q.pop()
            q.append(r)
            r += 1

            if r >= k:
                l += 1
                res.append(nums[q[0]])
                
                if q and q[0] < l:
                    q.popleft()\
                    
        return res
        