from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition:
            - bruteforce:
                - recalculate the max for every subarray
            - sliding window 
        """
        # Bruteforce:
        # l = 0
        # res = []
        # for r in range(k-1, len(nums)):
        #     res.append(max(nums[l:r+1]))
        #     l += 1

        # return res

        # Optimal
        q = deque()
        l = 0
        res = []
        for r in range(0, len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1

        return res

        