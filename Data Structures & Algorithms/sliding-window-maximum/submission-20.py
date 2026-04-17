from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l, r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            r += 1

            if q and q[0] < l:
                q.popleft()

            if r >= k:
                l += 1
                res.append(nums[q[0]])

        return res
        # res = []
        # q = deque()
        # l, r = 0, 0
        # while r < len(nums):
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)

        #     if q and q[0] < l:
        #         q.popleft()

        #     if r + 1 >= k:
        #         l += 1
        #         res.append(nums[q[0]])
                
        #     r += 1

        # return res
        