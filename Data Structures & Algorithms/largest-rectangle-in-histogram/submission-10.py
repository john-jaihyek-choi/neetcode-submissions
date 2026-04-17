class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack to store individual bar in an increasing/ascending order
            # when visiting the next bar, if the next bar is smaller, then pop the existing bars until we find a bar <= the current

        stack = []
        max_area = float('-inf')
        for i, h in enumerate(heights):
            pair = [i, h]
            
            while stack and h < stack[-1][1]:
                j, prev_h = stack.pop()
                pair[0] = j
                max_area = max(max_area, (i - j) * prev_h)

            stack.append(pair)

        while stack:
            i, h = stack.pop()
            w = len(heights) - i
            area = w * h
            max_area = max(max_area, area)


        return max_area

            
