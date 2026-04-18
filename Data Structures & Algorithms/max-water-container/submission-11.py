class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Note:
            - find maximum possible amount of water from a container
            - water container area = (r - l) * min(l, r)
        Bruteforce - 2 loops:
            - iterate n^2 times and calculate every possibility
            - TC: O(n^2) / SC: O(1)
        Two-pointer:
            - initialize l and r
                - l, r = 0, len(heights)-1
                - while l < r:
                    - compute area
                        - area = (r - l) * min(l, r)
                    - update max area
                    - if l < r:
                        - l += 1
                    - else:
                        - r -= 1
            - TC: O(n) / SC: O(1)
        """
        mx = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            mx = max(mx, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return mx