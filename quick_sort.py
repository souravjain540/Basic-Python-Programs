#!/usr/bin/env Python3

def partition(array,low,high):

    pivot=array[high]

    i=low-1
    
    for j in range(low,high):
        if array[j] <= pivot:
           i+=1
           array[i],array[j] = array[j],array[i]
        

    array[i+1],array[high] = array[high],array[i+1]

    return i+1


def quick_sort(array,low,high):
    if low < high:
       pi=partition(array,low,high)
       quick_sort(array,low,pi-1)
       quick_sort(array,pi+1,high)
       
    
        
array=[1,7,45,32,99,56,32,45,67,34,35,12,13,16,45,4795,19,15,6,2,63]

quick_sort(array,0,len(array) -1)

print(array)

 

    
    
