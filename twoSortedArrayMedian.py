# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:33:29 2022

@author: INAKKAM
"""

def median(arr1,arr2):
    arr=arr1+arr2
    arr.sort()
    print(arr)
    length=len(arr)
    if length%2==0:
        return (arr[int(length/2)]+arr[int(length/2)-1])/2
    else:
        return arr[int(length/2)]
        
    
print(median([3,4,5,7,9,0], [-1,-4,24,22,10]))