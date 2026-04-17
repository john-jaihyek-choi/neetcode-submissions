class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # TC: O(n) / SC: O(n)
        # freq_col = [[] for _ in range(len(nums) + 1)] # TC: O(n) / SC: O(n)
        freq = Counter(nums) # TC: O(n) / SC: O(n)

        # for n, freq in freq.items(): # TC: O(n) / SC: O(n)
        #     freq_col[freq].append(n)

        # res = []
        # for i in range(len(freq_col) - 1, 0, -1): # TC: O(n) / SC: O(n)
        #     nums = freq_col[i]
        #     for n in nums: # TC: O(k) -> O(1)
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        # return res

        pairs = []
        for n, freq in freq.items():
            pairs.append([freq, n])

        pairs.sort()
        n = len(pairs) - 1
        res = []
        for i in range(n, n - k, -1):
            res.append(pairs[i][1])

        return res
            
