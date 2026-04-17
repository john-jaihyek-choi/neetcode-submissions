class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        for num_val, count in count_map.items():
            freq[count].append(num_val)

        response = []

        for i in range(len(freq) - 1, -0, -1):
            for number in freq[i]:
                response.append(number)
                if len(response) == k:
                    return response