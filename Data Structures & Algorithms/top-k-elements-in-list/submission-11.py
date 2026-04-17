class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brainstorm:
            # need to return "k"-most frequent elements from nums array
                # if multiple, return all
            # ideas:
                # first-thought solution:
                    # initialize an array with default value of empty array with length of n + 1 (freq_arr)
                    # initialize an empty dictionary to store counts
                    # iterate on nums (n = nums[i])
                        # increment the count of n to counter dictionary
                    # iterate on the key and values of the counter (key = number, count = value)
                        # freq_arr[count].append(number)
                    # initialize empty array, res = []
                    # iterate the freq_arr from the end of the arr (item = freq_arr[i])
                        # while item:
                            # if k <= 0:
                                # return res
                            # res.append(item.pop())
                    # return res
        freq_arr = [[] for _ in range(len(nums)+1)]
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for number, count in counter.items():
            freq_arr[count].append(number)
        
        res = []

        for i in range(len(freq_arr) - 1, -1, -1):
            while freq_arr[i]:
                if k <= 0:
                    return res
                res.append(freq_arr[i].pop())
                k -= 1

        return res
                