class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # intialize a dictionary which to store the count of each integer in nums array to get the unique count of each occurance of a number (count_dict)

        # iterate the nums array and store the total count of number occurances 

        # initialize an array of arrays where the length of the outer array is len of nums + 1 (frequency)
            # this is to store the total possible frequency (wherein nums array contains same number in every index)
            #       c: 0   1    2   3  ...
            # nums[i]:[[], [1], [2], [3], ...]

        # iterate the items in the count_map dictionary and append the key (value of the nums[i]) to its respective index (count)

        # initialize an empty array to return as a response of the function (res_array)

        # iterate the frequency array from the end of the list and append it to res_array for k many times

        count_map = dict()
        
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        print(count_map)
        
        frequency_list = [[] for i in range(len(nums) + 1)]

        for num, count  in count_map.items():
            frequency_list[count].append(num)

        print(frequency_list)

        res_list = []

        for i in range(len(frequency_list) - 1, 0, -1) :
            for num in frequency_list[i]:
                if len(res_list) == k:
                    return res_list
                res_list.append(num)

        return res_list

        

