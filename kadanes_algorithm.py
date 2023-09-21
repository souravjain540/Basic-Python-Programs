"""
This algorithm is used to find the largest sum in the given array in O(n) Time complexity
"""

arr=[-1,0,3,4,2,6,-10,5,-9]

max_sum=0
curr_sum=0

for i in arr:
    curr_sum += i
    max_sum=max(max_sum,curr_sum)
    
    if curr_sum<0:
        curr_sum=0


print(max_sum)