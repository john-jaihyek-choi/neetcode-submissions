
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quick Select Approach:
            -  General Step:
                1. Identify a position in nums arr where kth largest element should be in as if it is sorted:
                    - ex)       0  1  2  3  4
                        nums = [3, 2, 1, 5, 4], k = 2
                        - kth_pos = len(nums) - k = 5 - 2 = 3
                2. Write a recursive function that iterates from Left bound to Right bound (args: l, r)
                    Note - This is to recursively iterate the partition (left or right) that would contain kth position
                    - Set a "pivot" point
                        - simply set nums[r]
                    - define partition = l
                    - iterate from l to r (i = index):
                        - if nums[i] <= pivot:
                            - set nums[i], nums[parition] = nums[partition], nums[i]
                            - increment partition pointer by 1
                    - update the swap the pivot value with nums[partition]
                        - nums[partition], nums[r] = nums[r], nums[partition]
                    - if partition > k:
                        - kth position is to the left of the partition pointer
                            - repeat the recursive step with boundary l and partition - 1
                    - if partition < k:
                        - kth position is to the right of the partition pointer
                            - repeat the recursive step with boundary partition + 1 and r
                    - else:
                        - return nums[p]
        """

        kth_pos = len(nums) - k

        def checkPartition(l: int, r: int) -> int:
            pivot, partition = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    partition += 1
            
            nums[partition], nums[r] = nums[r], nums[partition]
            
            if partition > kth_pos:
                # check left
                return checkPartition(l, partition - 1)
            elif partition < kth_pos:
                # check right
                return checkPartition(partition + 1, r)
            else:
                return nums[partition]
        
        return checkPartition(0, len(nums) - 1)

class Solution1:
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
        max_heap = [-n for n in nums] # TC: O(n) / SC: O(n)
        heapq.heapify(max_heap) # TC: O(n)
        
        res = abs(max_heap[0]) 
        while k > 0: # TC: O(k)
            res = heapq.heappop(max_heap) # TC: O(log n)
            k -= 1

        return -res

        # # TC: O(n - k log n) / SC: O(1)
        heapq.heapify(nums) # TC: O(n)
        
        while len(nums) > k: # TC: O(n - k)
            heapq.heappop(nums) # TC: O(log n)

        return heapq.heappop(nums) # TC: O(log n)

        # TC: O(n log k) / SC: O(1)
        return heapq.nlargest(k, nums)[-1]

