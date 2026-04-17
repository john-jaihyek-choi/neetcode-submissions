class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Intuition:
            - Max Heap:
                - heapify nums
                - while k > 0:
                    - heappop from the heapq
                    - decrement k
            - Min Heap:
                - heapify nums
                - while len(min_heap) > k:
                    heapq.heappop(min_heap)
            - Use built-in nlargest:
                - use heapq.nlargest()
        """
        # # TC: O(n + k log n) / SC: O(n)
        # max_heap = [-n for n in nums] # TC: O(n) / SC: O(n)
        # heapq.heapify(max_heap) # TC: O(n)
        
        # res = abs(max_heap[0]) 
        # while k > 0: # TC: O(k)
        #     res = heapq.heappop(max_heap) # TC: O(log n)
        #     k -= 1

        # return -res

        # # TC: O(n - k log n) / SC: O(1)
        # heapq.heapify(nums) # TC: O(n)
        
        # while len(nums) > k: # TC: O(n - k)
        #     heapq.heappop(nums) # TC: O(log n)

        # return heapq.heappop(nums) # TC: O(log n)

        # TC: O(n - k log n) / SC: O(1)
        return heapq.nlargest(k, nums)[-1]

