class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack list will keep pair of (index, height)
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            pair = [i, h]

            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_i))
                pair[0] = prev_i

            stack.append(pair)

        while stack:
            i, h = stack.pop()
            w = len(heights) - i
            max_area = max(max_area, w * h)

        return max_area
            

