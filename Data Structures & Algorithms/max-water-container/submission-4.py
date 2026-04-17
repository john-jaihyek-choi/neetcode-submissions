class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area, l, r = 0, 0, len(heights) - 1

        while l < r:
            max_area = max(max_area, min(heights[l], heights[r]) * (r - l) )

            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return max_area