class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not len(nums1) and not len(nums2):
            return -1

        A, B = nums1, nums2
        if B < A:
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            m1 = (r + l) // 2
            m2 = half - m1 - 2

            A_lp_last = A[m1] if m1 >= 0 else float('-inf')
            A_rp_first = A[m1 + 1] if m1 + 1 < len(A) else float('inf')  
            B_lp_last = B[m2] if m2 >= 0 else float('-inf')
            B_rp_first = B[m2 + 1] if m2 + 1 < len(B) else float('inf')

            if A_lp_last <= B_rp_first and B_lp_last <= A_rp_first:
                if total % 2:
                    return min(A_rp_first, B_rp_first)
                else:
                    return (max(A_lp_last, B_lp_last) + min(A_rp_first, B_rp_first)) / 2
            elif A_lp_last > B_rp_first:
                r = m1 - 1
            else:
                l = m1 + 1

                



            

