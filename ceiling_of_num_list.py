# In this problem we have to find a number equal to or the smallest greatest number to the given target number.

#     so we use binary search for this
#     case 1: mid==target
#         so we have found a number equal to the target. problem solved
#     case 2 : element is not in the array
#         in this case we would reach the start>end and the while loop would stop.
#         and the next greater element would be pointed at by the start.
#         so the ceiling of the number would be arr[start].

arr =[1,2,3,4,8,9,10,15,19,23,27,29,34,39,45,46,55,59,60,63,68,69]
target = int(input("Enter the target element->"))
start = 0
end = len(arr)-1

while(start<end):
    mid = int(start + (end - start) / 2)
    if target == arr[mid]:
        print(f"The ceiling of the element is {arr[mid]}")
        break
    elif target<arr[mid]:
        end=mid-1
    elif target>arr[mid]:
        start=mid+1
else:
    print(f"The ceiling of the element is {arr[start]}")    
