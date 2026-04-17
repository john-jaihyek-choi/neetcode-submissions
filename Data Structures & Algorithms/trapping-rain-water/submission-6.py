class Solution:
    def trap(self, height: List[int]) -> int:
        # left max can be recalculated as iterating
        # max(cur i, left max) will tell us the bottleneck of the area
        # height[i] can be subtracted from the area calculated for that portion of the iteration
        
        l_max, r_max = 0, 0
        area = 0
        l, r = 0, len(height) - 1
        while l < r:

            if height[l] <= height[r]:
                area += max(max(l_max, height[l]) - height[l], 0)
                l_max = max(l_max, height[l])
                l += 1
            else:
                area += max(max(r_max, height[r]) - height[r], 0)
                r_max = max(r_max, height[r])
                r -= 1

        return area