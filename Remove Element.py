def removeElement(nums, val):
        newnum = []
        for i in range(0, len(nums)):
            newnum.append(nums[i])
        nums = []

        for i in range(0, len(newnum)):
            if newnum[i] != val:
                nums.append(newnum[i])
            k = len(nums)
        return k

#Given an array nums and a value val, remove all instances of that value in-place and return the new length.



#eg：nums = [3,2,2,3]
#val = 2

#aa=removeElement(nums, val)
#print(aa)
#it will print 2. Becuase after remove 2, nums=[3,3] and there are 2 elements in nums