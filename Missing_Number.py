
def missingNumber(nums):
    i = 0
    while i < len(nums):
        corrrect_ind = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[corrrect_ind]:
            nums[i], nums[corrrect_ind] = nums[corrrect_ind], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)

num = [3,0,1]
print(missingNumber(num))
