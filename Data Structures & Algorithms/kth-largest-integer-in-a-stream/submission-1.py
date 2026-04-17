class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        pass
        

    def add(self, val: int) -> int:
        pass
        
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums) # TC: O(nlogn) / SC: O(n)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.insert(self.findInsertIndex(val), val) # TC: O(n + log n)
        return self.findKthLargest(self.k) # TC: O(1)

    def findInsertIndex(self, val) -> int:
        # TC: O(log n)
        l, r = 0, len(self.nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if val > self.nums[m]:
                l = m + 1
            elif val < self.nums[m]:
                r = m - 1
            else:
                return m
        
        return l


    def findKthLargest(self, k: int) -> int:
        if len(self.nums) < k - 1:
            return None

        return self.nums[len(self.nums) - k] # TC: O(1)

class KthLargest1:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums,reverse=True) # TC: O(nlogn) / SC: O(n)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True) # TC: O(nlogn)

        return self.findKthLargest(self.k) # TC: O(1)

    def findKthLargest(self, k: int) -> int:
        if len(self.nums) < k - 1:
            return None

        return self.nums[k - 1] # TC: O(1)