class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_col = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n, freq in freq.items():
            freq_col[freq].append(n)

        res = []
        for i in range(len(freq_col) - 1, 0, -1):
            nums = freq_col[i]
            for n in nums:
                res.append(n)
                if len(res) == k:
                    return res

        return res
