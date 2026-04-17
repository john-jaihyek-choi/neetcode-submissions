class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_stack = []

        for i, temp in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]] < temp:
                days = i - temp_stack[-1]
                res[temp_stack[-1]] = days
                temp_stack.pop()
            temp_stack.append(i)

        return res
