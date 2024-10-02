def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example Usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))  # Output: 6
