class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bruteforce:
            # iterate the nums array and collect frequency
            # sort the frequency.keys descending
            # iterate the sorted array and append the items to output
        # Optimal solution:
            # use array hashing and dictionary:
            # initialize an empty array with size of n where n = size of nums
            # initialize freq_map to collect counts
            # iterate on the freq_map to store each num to count index in the array
            # iterate from the back of the array and append the num to output
                # stop when output arr len is k
        count_arr = [[] for _ in range(len(nums) + 1)]
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        for num, freq in freq_map.items():
            count_arr[freq].append(num)

        output = []
        for i in range(len(count_arr) - 1, -1, -1):
            while count_arr[i]:
                output.append(count_arr[i].pop())
                if len(output) == k:
                    return output
        
        return output
        

