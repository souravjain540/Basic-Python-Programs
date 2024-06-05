
def firstMissingPositive(nums):
    i = 0
    while i < len(nums):
        correct_ind = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct_ind]:
            nums[i], nums[correct_ind] = nums[correct_ind], nums[i]
        else:
            i += 1

    for index in range(len(nums)):
        if nums[index] != index+1:
            return index+1
    return len(nums) + 1

num = [3,4,-1,1]
print(firstMissingPositive(num))
