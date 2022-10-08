class Result(object):

    def MaxSubArray(self, numbers):
        overall_max = float('-inf')
        max_ending = 0

        for num in numbers:
            if max_ending > 0:
                max_ending += num
            else:
                max_ending = num
            overall_max = max(overall_max, max_ending)

        return overall_max 

obj1 = Result()

"""
Example test case -->
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
"""

print(obj1.MaxSubArray(numbers= [-2,1,-3,4,-1,2,1,-5,4]))

"""
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""