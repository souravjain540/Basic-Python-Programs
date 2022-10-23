# This function takes 2 parameters the numbers array and the target
# If the target is found it returns the indices of the numbers which add up to the target
# If not found, it returns [-1,-1]

# Time Complexity for this is O(NlogN) due to sorting
# Space Complexity is O(1) because we are not using any additional space

def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1

    while l < r:
        cur_sum = nums[l] + nums[r]
        if cur_sum < target:
            l += 1
        elif cur_sum > target:
            r -= 1
        else:
            return [l, r]

    return [-1, -1]
