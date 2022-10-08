#LeetCode Problem 4 Median of Two Sorted Arrays


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r =  nums1 + nums2
        r.sort()
        rl = len(r)
        if rl % 2 == 1:
            return r[rl//2]
        else:
            return (r[rl//2 - 1] + r[rl//2])/2