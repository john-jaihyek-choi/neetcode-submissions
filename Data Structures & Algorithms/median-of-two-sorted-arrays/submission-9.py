class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B  = nums1, nums2
        
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            n1_lp_last = A[m1] if m1 >= 0 else float('-inf')
            n1_rp_start = A[m1 + 1] if m1 + 1 < len(A) else float('inf')
            n2_lp_last = B[m2] if m2 >= 0 else float('-inf') 
            n2_rp_start = B[m2 + 1] if m2 + 1 < len(B) else float('inf')

            # if nums1[m1] <= nums2[m2+1] and nums2[m2] <= nums1[m1 + 1]:
            if n1_lp_last <= n2_rp_start  and n2_lp_last <= n1_rp_start:
                if total % 2:
                    return min(n1_rp_start, n2_rp_start)
                return (max(n1_lp_last, n2_lp_last) + min(n1_rp_start, n2_rp_start)) / 2
            elif n1_lp_last > n2_rp_start:
                r = m1 - 1
            else:
                l = m1 + 1

        return float(-1)