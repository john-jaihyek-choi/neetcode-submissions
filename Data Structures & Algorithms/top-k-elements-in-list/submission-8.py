class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_index = [[] for i in range(len(nums))] 
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] += 1

        for num, count in count_map.items():
            count_index[count - 1].append(num)



        res = []
        for i in range(len(count_index) - 1, -1, -1):
            if len(res) == k:
                return res
            for j in range(len(count_index[i])):
                res.append(count_index[i][j])

        return res
            
        

