 
def majorityElement(nums):
    Ele = 0
    Count = 0

    for num in nums:

        if Count == 0:
            Ele = num

        if Ele == num:
            Count += 1
        else:
            Count -= 1

    return Ele

NUM =  [2,2,1,1,1,2,2]
print(majorityElement(NUM))
