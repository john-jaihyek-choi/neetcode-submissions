class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = defaultdict(int)

        for num in nums:
            res_dict[num] += 1

        print(res_dict)

        return sorted(res_dict, key=res_dict.get)[-k:]