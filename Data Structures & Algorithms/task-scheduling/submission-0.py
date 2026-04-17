import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Intuition:
            - Using Hashmap to store frequency of tasks and heapify, then use queue to store the "popped" items
                - store frequency of each tasks (26 unique tasks) in hashmap
                    ex) tasks = ["X","X","Y","Y"]
                    {
                        X: 2,
                        Y: 2
                    }
                - heapify frequency dictionary (max_heap)
                - create a queue
                - while max_heap is non-empty or q is non-empty:
                    - if max_heap:
                        - heappop from the max_heap
                            - this will contain task with highest frequency
                        - store the popped value - 1 to queue to store the order
                    - else:
                        - increment cyle by 1 since iteration is complete
                        while q:
                            - push the q.popleft() to max_heap
        """

        cpu_tasks = Counter(tasks)
        max_heap = [-freq for freq in cpu_tasks.values()]
        heapq.heapify(max_heap)

        q = deque()
        cycle = 0
        while max_heap or q:
            cycle += 1
            
            if max_heap:
                freq = heapq.heappop(max_heap) + 1
                if freq < 0:
                    q.append(tuple([freq, cycle + n]))
            

            if q and q[0][1] == cycle:
                heapq.heappush(max_heap, q.popleft()[0])

        return cycle

