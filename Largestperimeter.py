def largestperimeter(nums):

    nums.sort()
    a, b, c = nums.pop(), nums.pop(), nums.pop()
    while b + c <= a:
        if not nums:
            return 0
        a, b, c = b, c, nums.pop()
    return a + b + c
