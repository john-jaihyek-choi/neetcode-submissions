class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()

        return self.findKthLargest(self.k)

    def findKthLargest(self, k: int) -> int:
        if len(self.nums) < k - 1:
            return None

        return self.nums[len(self.nums) - self.k]