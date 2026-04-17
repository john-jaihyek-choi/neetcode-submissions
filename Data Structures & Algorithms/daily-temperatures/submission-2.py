class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_index = []

        for i in range(len(temperatures)):
            while temp_index and temperatures[temp_index[-1]] < temperatures[i]:
                days = i - temp_index[-1]
                res[temp_index[-1]] = days
                temp_index.pop()
            
            temp_index.append(i)

        return res