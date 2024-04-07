# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# example 1
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

#Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

#nums1 and nums2 are 2 sorted arrays
def findMedianSortedArrays(A, B):
        
        med1 = med2 = i = j = 0
        n = len(A) + len(B)
        
        while (i + j) <= n / 2:
            if i < len(A) and j < len(B):
                med2 = med1
                if A[i] < B[j]:
                    med1 = A[i]
                    i += 1
                else:
                    med1 = B[j]
                    j += 1
            elif i < len(A):
                med2 = med1
                med1 = A[i]
                i += 1
            elif j < len(B):
                med2 = med1
                med1 = B[j]
                j += 1

        if n % 2 == 0:
            return (med1 + med2) / 2.0
        else:
            return med1



