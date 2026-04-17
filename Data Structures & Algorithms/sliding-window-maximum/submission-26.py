class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # input:
            # nums: List[int]
            # k: int
                # size of the window
        # goal: return a list that contains the maximum element in the window at each step
        # Sliding window approach:
            # main challenge of the problem:
                # how to know the maximum within the window boundary
            # l and r
                # when to move l?
                    # l moves when r has reached k
                        # when r >= k, l moves
                # when to move r?
                    # every iteration
            # how do I track max value within the boundary?
                # as r and l moves, store the max within the boundary
                    # how?
                        # using stack or queue?
                            # won't work since stack can't pop the bottom. It's one way pop
                        # double ended queue?
                            # double ended queue can pop and append from each end of the list O(1)
                    # How can I properly store the max?
                        # if we keep the deque in a strictly decreasing order, we can ensure we have access to max in O(1) tine
                        # if value at the top of the deque is greater than the one appending, append.
                        # if value at the top of the dque is less than the one appending, pop until top of the stack is greater, then append
                    # But how do I keep track of max within boundary in each iteration?
                        # since l pointer represents an index of the number
                            # storing index to the number can ensure that we can pop the bottom of the stack (max) when out of bounds
                                # when l > stack[0]
                            # even if the bottom is popped, the next number will be guaranteed to be a max value
            # return value?
                # need to return a max value at each index in each slide
            # Variables to track:
                # res: List[int]
                # l and r pointer
                    # l: int
                    # r: int
                # q: Deque[]
            
            # Pseudocode:
                # initialize an empty deque (deque)
                # initialize an empty array for response (res)
                # initialize an l pointer to 0
                # loop nums (r = index, n = nums[r])
                    # while q is valid and value of nums[q[-1]] < n:
                        # pop the top of the q
                    # append r to the q
                    # if r >= k:
                        # res.append(nums[q[0]])
                        # if l > q[0]:
                            # q.popleft()
                        # increment l by 1
            
            q, res = deque(), []
            l = 0
            for r, n in enumerate(nums):
                while q and nums[q[-1]] < n:
                    q.pop()
                
                q.append(r)

                if r + 1 >= k:
                    if l > q[0]:
                        q.popleft()
                    
                    l += 1
                    res.append(nums[q[0]])
                    
                
            return res
                    


