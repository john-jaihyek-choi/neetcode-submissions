class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Intuition:
            - Max Heap:
                - heapify nums
                - while k > 0:
                    - heappop from the heapq
                    - decrement k

        """
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        res = abs(max_heap[0])
        while k > 0:
            res = heapq.heappop(max_heap)
            k -= 1

        return -res

