class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            pair = [i, heights[i]]

            while stack and stack[-1][1] >= heights[i]:
                area = (i - stack[-1][0]) * stack[-1][1]
                max_area = max(max_area, area)
                pair[0] = stack[-1][0]
                stack.pop()
            
            stack.append(pair)

        while stack:
            area = (len(heights) - stack[-1][0]) * stack[-1][1]
            max_area = max(max_area, area)
            stack.pop()

        return max_area