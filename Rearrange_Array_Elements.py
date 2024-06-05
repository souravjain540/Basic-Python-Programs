
def rearrangeArray(nums):
    pos = 0
    neg = 1
    ans = [0] * len(nums)
    for num in nums:
        if num > 0:
            ans[pos] = num
            pos += 2
        else:
            ans[neg] = num
            neg += 2

    return ans


num = [3,1,-2,-5,2,-4]
print(rearrangeArray(num))
