class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Note:
            # the max freq of number will be the len(nums)

        # instantiate an array with len(nums) with an initial value in each index with [] (freq_list)
            # empty list for easy append to the list
        # instantiate a count map to count the frequency counts (freq_counts)
        # iterate the nums array
            # set the count of nums[i] plus one in freq_counts
        # iterate the freq_counts map items:
            # store the count value to the freq_list[count]
        # instantiate an empty res array (res)
        # iterate the freq_list from the end of the array
            # iterate the freq_list[i]
                # if length of res >= k:
                    # return res
                # append the freq_list[i][j] to res

        freq_list = [[] for i in range(len(nums) + 1)]
        freq_counts = defaultdict(int)

        for n in nums:
            freq_counts[n] += 1

        print(freq_counts)

        for num, count in freq_counts.items():
            freq_list[count].append(num)

        print(freq_list)

        res = []
        for i in range(len(freq_list) - 1, -1, -1):
            for j in range(len(freq_list[i])):
                if len(res) >= k:
                    return res
                res.append(freq_list[i][j])
        
        return res
