from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        l = 0
        # [ 1, 2 ]
        for r, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

        return res