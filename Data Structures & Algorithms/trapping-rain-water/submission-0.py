class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_list, max_right_list = [0], [0]
    
        l, r = 0, len(height) - 1
        max_left, max_right = 0, 0

        while r > 0:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])

            max_left_list.append(max_left)
            max_right_list.append(max_right)

            l+=1
            r-=1

        max_right_list.reverse()

        area = 0
        for i, h in enumerate(height):
            area += max(
                0,
                min(max_left_list[i], max_right_list[i]) - h
            )

        return area